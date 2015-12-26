from flask import Flask
import FlaskDeferredHandler
from main import api
from flask.ext.cors import CORS

app = Flask(__name__)
app.register_blueprint(api)
FlaskDeferredHandler.register(app)
CORS(app)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
