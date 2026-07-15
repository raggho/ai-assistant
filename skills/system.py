"""
system.py
Windows system controls for Babo.
"""

import os
import ctypes
import pyautogui
from datetime import datetime


def shutdown():
    os.system("shutdown /s /t 5")
    return "Shutting down your computer in 5 seconds."


def restart():
    os.system("shutdown /r /t 5")
    return "Restarting your computer in 5 seconds."


def cancel_shutdown():
    os.system("shutdown /a")
    return "Shutdown cancelled."


def lock_pc():
    ctypes.windll.user32.LockWorkStation()
    return "Locking your computer."


def logoff():
    os.system("shutdown /l")
    return "Logging off."


def sleep():
    ctypes.windll.powrprof.SetSuspendState(False, True, False)
    return "Going to sleep."


def take_screenshot():

    filename = datetime.now().strftime(
        "Screenshot_%Y%m%d_%H%M%S.png"
    )

    pyautogui.screenshot(filename)

    return f"Screenshot saved as {filename}"