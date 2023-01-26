#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:26:50 2023

@author: michalskalsky
"""

from problem2 import fibonacciGenerator

fibNum = fibonacciGenerator()
result = 0
idx = 0
while len(str(result)) < 1000:
    result = fibNum.__next__()
    idx += 1

print(idx)
    