from datetime import datetime
from sortedcontainers import SortedSet

periods = [
    (5, datetime(2010, 9, 19, 0, 0, 0),    datetime(2010, 9, 19, 0, 5, 10)),
    (6, datetime(2010, 9, 19, 0, 0, 0),    datetime(2010, 9, 19, 12, 59, 59)),
    (4, datetime(2010, 9, 19, 10, 30, 17), datetime(2010, 9, 19, 20, 20, 59)),
    (6, datetime(2010, 9, 19, 14, 12, 0),  datetime(2010, 9, 19, 23, 59, 59)),
    (5, datetime(2010, 9, 19, 17, 0, 22),  datetime(2010, 9, 19, 19, 14, 20))
]

cutpoints = SortedSet()

for period in periods:
    cutpoints.add(period[1])
    cutpoints.add(period[2])

ranges = []

start_cutpoint = None
for end_cutpoint in cutpoints:

    if not start_cutpoint:  # skip first
        start_cutpoint = end_cutpoint
        continue

    cut_point_active_periods = []

    for period in periods:

        # check if period and cutpoint range overlap
        start_overlap = max(start_cutpoint, period[1])
        end_overlap = min(end_cutpoint, period[2])

        if start_overlap < end_overlap:
            cut_point_active_periods.append(period[0])

    ranges.append((cut_point_active_periods, start_cutpoint, end_cutpoint))
    start_cutpoint = end_cutpoint

for i in ranges:
    print (i)   