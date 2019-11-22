import os
import sys

from flask import Flask, render_template, Response, send_from_directory, current_app, Blueprint
from flask_assets import Environment, Bundle

main = Blueprint('main', __name__)

# route to favicon
@main.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


@main.route('/')
def home():
    """Page: home of site"""
    return render_template('index.jinja2')


@main.route("/stream/console")
def console_stream():
    """Stream: continuous pipeline stream
    This stream is connected to by client via Javascript to constantly download messages (Responses) from the server.
    See ./templates/index.jinja2 for Javascript code.

    """
    def stream():
        queue = current_app.config['queue']
        yield queue.get()

    return Response(stream(), mimetype='text/html')


def create_app(queue):
    # use error as stdout
    sys.stdout = sys.stderr

    # create Flask application
    app = Flask(__name__)
    app.register_blueprint(main)

    # render SCSS
    scss = Bundle('site.scss', filters='libsass', output='site.css')
    assets = Environment(app)
    assets.url = app.static_url_path
    assets.register('scss_all', scss)

    app.config['queue'] = queue
    return app
