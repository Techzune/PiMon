import time
from sys import argv
from threading import Thread

from flask import Flask, render_template, Response
from flask_assets import Environment, Bundle

import test

# create Flask application
app = Flask(__name__)

# render SCSS
scss = Bundle('site.scss', filters='libsass', output='site.css')
assets = Environment(app)
assets.url = app.static_url_path
assets.register('scss_all', scss)

# open log file for display
LOG_FILE_NAME = "_std.log"
log_file = None


@app.route('/')
def home():
    """Page: home of site"""
    return render_template('index.jinja2')


@app.route("/stream/console")
def console_stream():
    """Stream: continuous stream of pipeline"""
    # log_file is global
    global log_file

    # if the log_file has not been opened
    if log_file is None:
        try:
            # try to open LOG_FILE_NAME
            log_file = open(LOG_FILE_NAME)
        except FileNotFoundError:
            # something went wrong
            return Response("Nothing to show.")

    def stream():
        # go to last line of file
        log_file.seek(0, 2)
        # loop indefinitely
        while True:
            # read a line
            line = log_file.readline()
            # if line didn't exist
            if not line:
                # wait
                time.sleep(0.1)
                continue
            # yield the line
            yield line

    return Response(stream(), mimetype='text/html')


# if main process, run the Flask app
if __name__ == '__main__':
    # test mode starts a thread for log
    if 'test' in argv:
        sensor_debug_thread = Thread(target=test.populateLogFileTester,
                                     args=(LOG_FILE_NAME,))
        sensor_debug_thread.daemon = True
        sensor_debug_thread.start()

    # run app on 0.0.0.0 to accept all connections
    app.run(host='0.0.0.0')
