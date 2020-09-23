# -*- coding: utf-8 -*-
"""


@author: saurav
"""
i=0
ch = input()
num = len(ch)
while i<num:
    if ch[i] != "G" and ch[i] !="C" and ch[i] !="T" and ch[i] !="A":
        print("Invalid Input")
        break
    if ch[i] == "G":
        print('C', end = '')
    elif ch[i] =="C":
        print('G', end = '')
    elif ch[i] =="T":
        print('A', end = '')
    elif ch[i] =="A":
        print('U', end = '') 
    else:
        print("Invalid Input")
        break   
    i+=1