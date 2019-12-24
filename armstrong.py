# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:49:16 2019

@author: Pranshul Singla
"""
sum=0
no=int(input("Enter number:"))
org=no
while(no>0):
    digit=no%10
    sum+=digit**3
    no//=10
if(sum==org):
    print("Armstrong No",sum)
else:
    print("Not an Armstrong No")