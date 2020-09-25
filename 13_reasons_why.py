# -*- coding: utf-8 -*-
"""


@author: saurav
"""
A,B,C=map(int,input().split())
NA = int(A)
B = int(B)
C = int(C)
D = A
A = B
B = D

A = C*A
B = B+C
print(A,B)