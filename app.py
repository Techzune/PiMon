import time

from flask import Flask, render_template, Response
from flask_assets import Environment, Bundle

# create Flask application
app = Flask(__name__)

# render SCSS
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('site.scss', filters='libsass', output='site.css')
assets.register('scss_all', scss)

# open log file for display
input_log = open('_std.log')


@app.route('/')
def home():
    """Page: home of site"""
    return render_template('index.jinja2')


@app.route("/stream/console")
def console_stream():
    """Stream: continuous stream of pipeline"""

    def stream():
        # go to last line of file
        input_log.seek(0, 2)
        while True:
            line = input_log.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line

    return Response(stream(), mimetype='text/html')


# if main process, run the Flask app
if __name__ == '__main__':
    app.run()
