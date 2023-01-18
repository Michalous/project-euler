#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 17:32:02 2022

@author: michalskalsky
"""
import math

ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

hundreds = ['', 'onehundred', 'twohundred', 'threehundred', 'fourhundred', 'fivehudnred', 'sixhundred', 'sevenhundred', 'eighthundred', 'ninehundred']
def number_to_units(num):
    onez = 0
    tenz = 0
    hundredz = 0
    if num / 100 >= 1:
        hundredz = math.floor(num / 100)
        num = num % 100
    if num / 10 >= 1:
        tenz = math.floor(num / 10)
        num = num % 10
    onez = num
    return [hundredz, tenz, onez]

def units_to_text(arr):
    string = ''
    if arr[0] > 0 and (arr[1] > 0 or arr[2] > 0):
        string += 'xxx'
    string += hundreds[arr[0]]
    if arr[1] == 1:
        string += teens[arr[2]]
    else:
        string += tens[arr[1]]
        string += ones[arr[2]]
    return string

def main():
    result = 11
    for i in range (1, 1000):
        arr = number_to_units(i)
        result += len(units_to_text(arr))
    return result

if __name__ == "__main__":
    print(main())     
        
        
        
        
        
        
        