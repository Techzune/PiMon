activate_this = '/home/pi/.local/share/virtualenvs/PiMon-KQG44wUy/bin/activate_this.py'
exec(compile(open(activate_this,"rb").read(),activate_this, 'exec'), dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)

sys.path.append('/home/pi/.local/share/virtualenvs/PiMon-KQG44wUy/lib/python3.5/site-packages')
sys.path.append('/home/pi/PiMon')

from app import app as application
