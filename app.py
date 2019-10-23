import time
import threading

from flask import Flask, render_template, Response
from flask_assets import Environment, Bundle

#DEBUG THREAD: populates log file
def sensorDataDebug():
    for x in range(1, 10000):
        logFile = open(LOG_FILE_NAME, "a")
        logFile.write("This is a test: "+str(x)+"\n")
        logFile.close()
        time.sleep(0.2)
#DEBUG THREAD /

# create Flask application
app = Flask(__name__)

# render SCSS
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('site.scss', filters='libsass', output='site.css')
assets.register('scss_all', scss)

# open log file for display
LOG_FILE_NAME = "_std.log"
log_file = None

#DEBUG THREAD: start
sensorDataDebugThread = threading.Thread(target=sensorDataDebug)
sensorDataDebugThread.daemon = True
sensorDataDebugThread.start()
#DEBUG THREAD /

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
            return Response("could not open log")

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
    app.run(host='0.0.0.0')