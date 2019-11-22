activate_this = '/home/pi/.local/share/virtualenvs/PiMon-KQG44wUy/bin/activate_this.py'
exec(compile(open(activate_this,"rb").read(),activate_this, 'exec'), dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)

sys.path.append('/home/pi/.local/share/virtualenvs/PiMon-KQG44wUy/lib/python3.5/site-packages')
sys.path.append('/home/pi/PiMon')

# run the serial handler in a separate process :)
import serialHandler
from multiprocessing import Process
s_handler_process = Process(target=serialHandler.setupSerialHandlers, args=(LOG_FILE_NAME,))
s_handler_process.start()

from app import app as application
