import sys
from datetime import datetime
from time import sleep

# output to file
sys.stdout = open('_std.log', 'wt')

while True:
    # print current time
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # flush to file
    sys.stdout.flush()
    # sleep
    sleep(1)
