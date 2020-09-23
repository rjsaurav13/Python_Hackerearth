# -*- coding: utf-8 -*-
"""


@author: saurav
"""

A = int(input())
B = int(input())

D = A
A = B
B = D
C = int(input())
A = C*A
B = B+C
print(A,B)
