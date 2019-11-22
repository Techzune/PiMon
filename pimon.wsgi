activate_this = '/home/pi/.local/share/virtualenvs/PiMon-KQG44wUy/bin/activate_this.py'
exec(compile(open(activate_this,"rb").read(),activate_this, 'exec'), dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)

sys.path.append('/home/pi/.local/share/virtualenvs/PiMon-KQG44wUy/lib/python3.5/site-packages')
sys.path.append('/home/pi/PiMon')

from multiprocessing import Queue
queue = Queue()

# run the serial handler in a separate process :)
import serialHandler
from multiprocessing import Process
s_handler_process = Process(target=serialHandler.setupSerialHandlers, args=(queue,))
s_handler_process.start()

from app import create_app
application = create_app(queue)
