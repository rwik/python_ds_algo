#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Rwik"
__version__ = "0.1.0"
__license__ = "MIT"

def max_sum(arr):

    n = len(arr)
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, n):
        current_sum = max(current_sum + arr[i], arr[i])
        max_sum = max(max_sum, current_sum)

    return  max_sum

ar1 = [3,-94,1,2]


print (max_sum(ar1))
