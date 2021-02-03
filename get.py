#!/usr/bin/python3

# get all files from given date through today
# get.py

import os
import requests
import sys
from datetime import datetime, timedelta

u = "http://regsho.finra.org/CNMSshvol{}.txt"

# only goes back to 20180801, everything else is 404
# if someone knows of a filename change or something
# around that time, let me know and i can fix this up
# to get older stuff
d_string = "20180801"

d = datetime.strptime(d_string, '%Y%m%d')

while d < datetime.today():
  if d.weekday() not in [5,6]:
    d_string = d.strftime('%Y%m%d')

    url = u.format(d_string)
    file = url.split('/')[-1]
    if not os.path.exists(os.path.join("txt", file)):
      print(url)
      r = requests.get(url)
      if (r.status_code == 200):
        with open(os.path.join("txt", file), 'wb') as f:
          f.write(r.content)

  d = d + timedelta(days=1)
