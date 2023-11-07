#!/usr/bin/env python
from tvDatafeed import TvDatafeed, Interval

tv = TvDatafeed()
data = tv.get_hist(symbol='ACIO',exchange='BATS',interval=Interval.in_daily,n_bars=457)
print(data)
