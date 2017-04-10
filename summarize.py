#!/usr/bin/env python3

import datetime
import os
from collections import Counter

from pymodoro import PYMODORO_DIR 
from pymodoro import DATETIMEFORMAT

def main():
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
        print("%d-%02d-%02d\t%d" % (y, m, d, by_day[key]))

if __name__ == "__main__": main()
