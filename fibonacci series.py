# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 21:02:29 2019

@author: Pranshul Singla
"""

# 0 1 1 2 3 5 8 13
nthTerm=int(input("Enter nth term to be displayed:"))
first,second=0,1
third=first+second
print(first,second,third,end=' ')
for i in range(4,nthTerm+1):
    first=second
    second=third
    third=first+second
    print(third,end=' ')