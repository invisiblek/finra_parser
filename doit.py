#!/usr/bin/python3

# parse data of given symbol
# doit.py GME

import os
import sys

count = 1
average_percent = 0

for file in sorted(os.listdir("txt")):
  if file.split('.')[-1] == "txt":
    with open(os.path.join("txt", file)) as f:
      for line in f.readlines():
        s = line.split('|')
        if len(s) > 1 and s[1] == sys.argv[1]:
          count += 1
          percent = int(s[2]) / int(s[4]) * 100
          average_percent = ((average_percent * (count-1)) + percent) / count
          print("{} - {} vol - {} shorted - {} % - {}".format(s[0], s[4].rjust(10), s[2].rjust(10), '{:.4f}'.format(round(percent,4)), "x" * int(percent)))

print("{}: {} %".format(sys.argv[1], round(average_percent,4)))
