#!/usr/bin/env python3

import datetime
import os
import sys

import pymodoro

def main():
    all_days = True
    if len(sys.argv) >= 2 and sys.argv[1] == "today":
        all_days = False

    by_day = pymodoro.load_counts()
    for key in sorted(by_day.keys()):
        y, m, d = key
        if all_days:
            print("%d-%02d-%02d\t%d" % (y, m, d, by_day[key]))

    now = datetime.datetime.now()
    today_key = (now.year, now.month, now.day)
    print("TODAY %d-%02d-%02d\t%d" % (now.year, now.month, now.day,
                                      by_day[today_key]))


if __name__ == "__main__": main()
