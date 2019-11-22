import os
import sys
import time

from flask import Flask, render_template, Response, send_from_directory, request
from flask_assets import Environment, Bundle


def create_app(red):
    # use error as stdout
    sys.stdout = sys.stderr

    # create Flask application
    app = Flask(__name__)

    # render SCSS
    scss = Bundle('site.scss', filters='libsass', output='site.css')
    assets = Environment(app)
    assets.url = app.static_url_path
    assets.register('scss_all', scss)

    # app.config['queue'] = queue
    # app.app_context().push()

    # route to favicon
    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

    @app.route('/')
    def home():
        """Page: home of site"""
        return render_template('index.jinja2')

    @app.route("/stream/console")
    def console_stream():
        """Stream: continuous pipeline stream
        This stream is connected to by client via Javascript to constantly download messages (Responses) from the server.
        See ./templates/index.jinja2 for Javascript code.

        """
        def events():
            time.sleep(0.5)
            yield red.get('msg')
        return Response(events(), mimetype='text/html')

    return app
