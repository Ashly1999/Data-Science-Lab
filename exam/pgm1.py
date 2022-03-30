# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n=int(input("enter the value of n:"))
a=0
b=1
sum=0
count=1
print("fibonacci series")
while(count<=n):
    print(sum,end="")
    count=count+1
    a=b
    b=sum
    sum=a+b
