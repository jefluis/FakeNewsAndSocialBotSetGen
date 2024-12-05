# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:22:25 2018

@author: Samir Ramos
"""

t = [3, 5, 8, 12, 15, 24]
j = len(t)
newt = []
while j>1:
    delta = t[j-1] - t[j-2]
    newt.append(delta)
    j = j-1
newt.reverse()
print(newt)
