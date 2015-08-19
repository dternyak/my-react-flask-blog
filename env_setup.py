import os
import sys
from google.appengine.api.app_identity import get_application_id
from google.appengine.api import apiproxy_stub_map
import webapp2

from webapp2_extras import jinja2

def get_project_root():
    basedir = os.path.abspath(os.path.dirname(__file__))
    return basedir


def setup():
    """Adds <project_root>/lib/ to the python path."""
    project_root = get_project_root()
    if os.path.exists(project_root):
        lib_path = os.path.join(project_root, 'lib')
        if lib_path not in sys.path:
            sys.path.insert(0, lib_path)

def jinja2_factory(app):
    """method for attaching additional globals/filters to jinja2"""

    j = jinja2.Jinja2(app)
    j.environment.globals.update({
        'uri_for': webapp2.uri_for,
    })
    return j

class BetterHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(factory=jinja2_factory, app=self.app)

    def render_template(self, _template, **context):
        ctx = {}
        ctx.update(context)
        rv = self.jinja2.render_template(_template, **ctx)
        self.response.write(rv)


"""
The ``agar.env`` module contains a number of constants to help determine which environment code is running in.
"""

server_software = os.environ.get('SERVER_SOFTWARE', '')
have_appserver = bool(apiproxy_stub_map.apiproxy.GetStub('datastore_v3'))

appid = None
if have_appserver:
    appid = get_application_id()
else:
    try:
        project_dirname = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        project_dir = os.path.abspath(project_dirname)
        from google.appengine.tools import dev_appserver
        appconfig, matcher, from_cache = dev_appserver.LoadAppConfig(project_dir, {})
        appid = appconfig.application
    except ImportError:
        dev_appserver = None
        appid = None

#: ``True`` if running in the dev server, ``False`` otherwise.
on_development_server = bool(have_appserver and (not server_software or server_software.lower().startswith('devel')))
#: ``True`` if running on a google server, ``False`` otherwise.
on_server = bool(have_appserver and appid and server_software and not on_development_server)
#: ``True`` if running on a google server and the application ID ends in ``-int``, ``False`` otherwise.
on_integration_server = on_server and appid.lower().endswith('-int')
#: ``True`` if running on a google server and the application ID does not end in ``-int``, ``False`` otherwise.
on_production_server = on_server and not on_integration_server
