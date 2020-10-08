#pip3 install sports.py
#pip3 install py-notifier

import time
import sports
from pynotifier import Notification
while(True):
    matchinfo = sports.get_sport("CRICKET")
    Notification(title = "IPL Live Score Update",description = str(matchinfo),duration = 10).send()
    time.sleep(1200)  #Notify after every 20 minutes
