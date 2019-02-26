#!/usr/bin/env python3

WORKLENGTH = 25 # time in minutes
BREAKLENGTH = 5 # time in minutes
PYMODORO_DIR = "pymodoro"
DATETIMEFORMAT = "%Y-%m-%d %H:%M"

import datetime
import time
import os

def save_pomodoro():
    timestamp = datetime.datetime.now().strftime(DATETIMEFORMAT)
    home = os.path.expanduser("~")
    worklogfn = os.path.join(home, PYMODORO_DIR, "worklog")
    with open(worklogfn, "a") as outfile:
        print("PYMODORO at", timestamp, file=outfile)

def main():
    while True:
        print("now get back to work! (ctrl-c to exit)")
        input("pause: ")
        for minutesleft in range(WORKLENGTH, 0, -1):
            print("work for {} minutes".format(minutesleft))
            time.sleep(60)
        print("hit enter to log success and take a break! (ctrl-c to exit)")
        input("pause: ")
        save_pomodoro()
        for minutesleft in range(BREAKLENGTH, 0, -1):
            print("break for {} minutes".format(minutesleft))
            time.sleep(60)

if __name__ == "__main__": main()
