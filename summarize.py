#!/usr/bin/env python3

import datetime
import os
import sys
from collections import Counter

from pymodoro import PYMODORO_DIR 
from pymodoro import DATETIMEFORMAT

def main():
    all_days = True
    if len(sys.argv) >= 2 and sys.argv[1] == "today":
        all_days = False

    home = os.path.expanduser("~")
    worklogfn = os.path.join(home, PYMODORO_DIR, "worklog")

    by_year = Counter()
    by_month = Counter()
    by_day = Counter()

    prefix = "PYMODORO at "
    with open(worklogfn) as infile:
        for line in infile:
            line = line.strip()
            if line.startswith(prefix):
                date_string = line[len(prefix):]
                dt = datetime.datetime.strptime(date_string, DATETIMEFORMAT)
                by_year[dt.year] += 1
                by_month[(dt.year, dt.month)] += 1
                by_day[(dt.year, dt.month, dt.day)] += 1
    for key in sorted(by_day.keys()):
        y, m, d = key
        if all_days:
            print("%d-%02d-%02d\t%d" % (y, m, d, by_day[key]))

    now = datetime.datetime.now()
    today_key = (now.year, now.month, now.day)
    print("TODAY %d-%02d-%02d\t%d" % (now.year, now.month, now.day,
                                      by_day[today_key]))


if __name__ == "__main__": main()
