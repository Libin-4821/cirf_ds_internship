# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 19:21:54 2024

@author: USER
"""

import time
import webbrowser
set_alarm = input("Set the website alarm as H:M:S ")
url = input("Enter the website you want to open ")
actual_time = time.strftime("%H:%M:%S")
while(actual_time != set_alarm):
    print("The time is" + actual_time)
    actual_time = time.strftime("%H:%M:%S")
    time.sleep(1)
if(actual_time == set_alarm):
    print("You should see your webpage now:")
    webbrowser.open(url)