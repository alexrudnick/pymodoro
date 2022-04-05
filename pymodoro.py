#!/usr/bin/env python3

WORKLENGTH = 15 # time in minutes
BREAKLENGTH = 5 # time in minutes
PYMODORO_DIR = "pymodoro"
DATETIMEFORMAT = "%Y-%m-%d %H:%M"

import datetime
import time
import os
from collections import Counter

def save_pomodoro():
    timestamp = datetime.datetime.now().strftime(DATETIMEFORMAT)
    home = os.path.expanduser("~")
    worklogfn = os.path.join(home, PYMODORO_DIR, "worklog")
    with open(worklogfn, "a") as outfile:
        print("PYMODORO at", timestamp, file=outfile)

def load_counts():
    """Returns a Counter mapping day tuples (Y, M, D) to counts of pymodoros."""
    by_year = Counter()
    by_month = Counter()
    by_day = Counter()

    prefix = "PYMODORO at "
    home = os.path.expanduser("~")
    worklogfn = os.path.join(home, PYMODORO_DIR, "worklog")
    with open(worklogfn) as infile:
        for line in infile:
            line = line.strip()
            if line.startswith(prefix):
                date_string = line[len(prefix):]
                dt = datetime.datetime.strptime(date_string, DATETIMEFORMAT)
                by_year[dt.year] += 1
                by_month[(dt.year, dt.month)] += 1
                by_day[(dt.year, dt.month, dt.day)] += 1
    return by_day

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
        by_day = load_counts()
        now = datetime.datetime.now()
        today_key = (now.year, now.month, now.day)
        print("TODAY %d-%02d-%02d\t%d" % (now.year, now.month, now.day,
                                          by_day[today_key]))
        for minutesleft in range(BREAKLENGTH, 0, -1):
            print("break for {} minutes".format(minutesleft))
            time.sleep(60)

if __name__ == "__main__": main()
