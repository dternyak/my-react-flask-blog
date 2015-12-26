import logging
import re
import string

from datetime import date, datetime, time
from random import choice, randint, random, uniform

from google.appengine.api import lib_config
from google.appengine.api.users import User
from google.appengine.ext import ndb


class ConfigDefaults(object):
    """Configurable constants.

    To override builder configuration values, define values like this
    in your appengine_config.py file (in the root of your app):

        ae_test_data_STRING_LENGTH = 4
        ae_test_data_DEFAULT_CONSTRUCTOR = 'create_new_entity'
    """

    BLOB_LENGTH = 6
    BYTE_STRING_LENGTH = 6
    DOMAIN_LENGTH = 8
    FLOAT_MIN_RANGE = 0
    FLOAT_MAX_RANGE = 100
    INT_MIN_RANGE = 0
    INT_MAX_RANGE = 100000
    STRING_LENGTH = 6
    NAMESPACE = None

    #  TODO DEFAULT_CONSTRUCTOR solved an edge case, may remove in future release
    DEFAULT_CONSTRUCTOR = None
    REQUIRED_ONLY = True

    IGNORED_PROPERTIES = [
        'ComputedProperty',
    ]

    BUILDABLE_PROPERTIES = [
        'BlobProperty',
        'BooleanProperty',
        'DateProperty',
        'DateTimeProperty',
        'FloatProperty',
        'GeoPtProperty',
        'IntegerProperty',
        'JsonProperty',
        'PickleProperty',
        'StringProperty',
        'TextProperty',
        'TimeProperty',
        'UserProperty',
        # 'BlobKeyProperty',
        # 'GenericProperty',
        # 'KeyProperty',
        # 'LocalStructuredProperty',
        # 'StructuredProperty'
    ]

    @classmethod
    def check_for_repeated(cls, property_value, _property):
        if _property._repeated:
            return [property_value]

        return property_value

    def blob_property(_property):
        value = ''.join([choice(string.ascii_letters + string.digits) for i in xrange(config.BLOB_LENGTH)])
        if len(value) > 0:
            return '%s_%s' % (_property._name, value)
        else:
            return _property._name

    def boolean_property(_property):
        if random() < .5:
            property_value = True
        else:
            property_value = False

        return ConfigDefaults.check_for_repeated(property_value, _property)

    def date_property(_property):
        property_value = date.today()
        return ConfigDefaults.check_for_repeated(property_value, _property)

    def date_time_property(_property):
        now = date.today()
        property_value = datetime(now.year, now.month, now.day)
        return ConfigDefaults.check_for_repeated(property_value, _property)

    def float_property(_property):
        property_value = uniform(config.FLOAT_MIN_RANGE, config.FLOAT_MAX_RANGE)
        return ConfigDefaults.check_for_repeated(property_value, _property)

    def geo_pt_property(_property):
        # lat & lon of Mpls, MN
        property_value = ndb.GeoPt(44.88, lon=93.22)
        return ConfigDefaults.check_for_repeated(property_value, _property)

    def integer_property(_property):
        property_value = randint(config.INT_MIN_RANGE, config.INT_MAX_RANGE)
        return ConfigDefaults.check_for_repeated(property_value, _property)

    def json_property(_property):
        property_value = {'name': 'value'}
        return ConfigDefaults.check_for_repeated(property_value, _property)

    def pickle_property(_property):
        property_value = {'name': 'value'}
        return ConfigDefaults.check_for_repeated(property_value, _property)

    def string_property(_property):
        if _property._choices:
            property_value = choice(list(_property._choices))
        else:
            value = ''.join([choice(string.ascii_letters + string.digits) for i in xrange(config.STRING_LENGTH)])

            if len(value) > 0:
                property_value = '%s_%s' % (_property._name, value)
            else:
                property_value = _property._name

        return ConfigDefaults.check_for_repeated(property_value, _property)

    def text_property(_property):
        return ConfigDefaults.check_for_repeated(_property._name, _property)

    def time_property(_property):
        return ConfigDefaults.check_for_repeated(time(12, 0, 0), _property)

    def user_property(_property):
        return ConfigDefaults.check_for_repeated(User('user@gmail.com'), _property)

    def entity_builder():
        return {}

config = lib_config.register('ae_test_data', ConfigDefaults.__dict__)


def _convert(name):
    # http://stackoverflow.com/questions/1175208/does-the-python-standard-library-have-function-to-convert-camelcase-to-camel-case
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def _remove_kwarg_params(kwargs, cls_properties):
    for key in kwargs:
        if key in cls_properties:
            del cls_properties[key]


def _remove_unsupported_properties(cls_properties):
    for key, value in cls_properties.items():
        if value.__class__.__name__ not in config.BUILDABLE_PROPERTIES:
            del cls_properties[key]


def _populate_instance_params(cls, kwargs, cls_properties, required_only):
    params = {}

    for _property in cls_properties.values():
        if _property._required or not required_only:
            if _property._default is not None:
                params[_property._name] = _property._default
            else:
                try:
                    override_name = '%s_%s' % (cls.__name__, _property._name)
                    override_function = config.entity_builder().get(override_name)
                    if override_function:
                        params[_property._name] = override_function(_property)
                    else:
                        property_config_name = _convert(_property.__class__.__name__)
                        property_config_function = config.__getattr__(property_config_name)
                        params[_property._name] = property_config_function(_property)
                except AttributeError as e:
                    logging.info('Skipped %s, Property not supported ' % e)
                    # return

    params.update(kwargs)
    return params


def _call_constructor(cls, constructor, params, _put=True):
    if constructor is None and config.DEFAULT_CONSTRUCTOR is None:
        instance = cls(**params)
        if _put:
            instance.put()
        return instance
    else:
        if constructor is not None:
            _constructor = getattr(cls, constructor)
        else:
            _constructor = getattr(cls, config.DEFAULT_CONSTRUCTOR)

        instance = _constructor(**params)
        if _put and instance.key is None:
            instance.put()
        return instance


def build(cls, *args, **kwargs):
    """Instantiate and populate a ndb.Model

    Args:
       cls (ndb.Model):  The model to populate
       *args (positional args):  These are ignored

    Kwargs:
        Passed to the Model constructor after the builder kwargs are removed.

    Builder kwargs:
        constructor (str): Name of the classmethod to call to instantiate.
        required_only (bool): Default True.  False populate all model properties, regardless of required=True model property attribute
        _put (bool): Default True.  False returns the model instance without first calling instance.put()

    Returns:
       The populated instance of a Model.

    """
    cls_properties = cls._properties.copy()
    constructor = kwargs.pop('constructor', None)
    required_only_kwarg = kwargs.get('required_only')
    _put_kwarg = kwargs.get('_put')

    if required_only_kwarg is not None:
        required_only = bool(required_only_kwarg)
        del kwargs['required_only']
    else:
        required_only = config.REQUIRED_ONLY

    if _put_kwarg is None:
        _put = True
    else:
        _put = bool(_put_kwarg)
        del kwargs['_put']

    if 'namespace' in kwargs:
        namespace = kwargs.get('namespace')
        if not namespace:
            del kwargs['namespace']
    elif config.NAMESPACE:
        kwargs['namespace'] = config.NAMESPACE

    _remove_kwarg_params(kwargs, cls_properties)
    _remove_unsupported_properties(cls_properties)
    params = _populate_instance_params(cls, kwargs, cls_properties, required_only)
    return _call_constructor(cls, constructor, params, _put=_put)
