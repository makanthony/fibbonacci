# -*- coding: utf-8 -*-
"""
Dec 2 2022

Anthony Mak
"""

def getNext(curr, prev):
    return curr + prev

fibo = [1, 1]
currNum = 1
prevNum = 1

while len(fibo) < 20:
    fibo.append(getNext(currNum, prevNum))
    currNum = fibo[len(fibo)-1]
    prevNum = fibo[len(fibo)-2]

print("The first 20 fibonacci numbers are: {}".format(fibo))