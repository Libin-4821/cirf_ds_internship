# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 19:45:24 2024

@author: USER
"""

import pyautogui
import time
import subprocess

def open_alarms_and_clock():
    # Open the Alarms & Clock app
    subprocess.Popen(['start', 'ms-clock:', ''], shell=True)
    time.sleep(5)  # Wait for the app to open

def set_alarm(hour, minute):
    # Open the Alarms tab
    pyautogui.click(100, 200)  # Adjust these coordinates based on your screen resolution
    time.sleep(1)
    
    # Click the 'Add new alarm' button
    pyautogui.click(150, 250)  # Adjust these coordinates based on your screen resolution
    time.sleep(1)
    
    # Set the hour
    pyautogui.click(200, 300)  # Adjust these coordinates based on your screen resolution
    pyautogui.typewrite(str(hour).zfill(2))
    time.sleep(1)
    
    # Set the minute
    pyautogui.click(300, 300)  # Adjust these coordinates based on your screen resolution
    pyautogui.typewrite(str(minute).zfill(2))
    time.sleep(1)
    
    # Save the alarm
    pyautogui.click(300, 700)  # Adjust these coordinates based on your screen resolution
    time.sleep(1)

if __name__ == "__main__":
    open_alarms_and_clock()
    set_alarm(7, 30)  # Set the alarm to 07:30
