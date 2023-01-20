#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 17:07:27 2022

@author: michalskalsky
"""

import datetime

date = datetime.datetime(2022, 10, 10)
print(f'{date:%A}')

res = 0
for i in range(1901, 2001):
  for j in range(1, 13):
    date = datetime.datetime(i, j, 1)
    if f'{date:%A}' == "Sunday":
      res += 1

print(res)