#!/home/pi/.local/share/virtualenvs/PiMon-KQG44wUy/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)

sys.path.append('/home/pi/.local/share/virtualenvs/PiMon-KQG44wUy/lib/python3.5/site-packages')
sys.path.append('/home/pi/PiMon')

from app import app as application