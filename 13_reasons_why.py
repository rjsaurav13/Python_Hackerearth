# -*- coding: utf-8 -*-
"""


@author: saurav
"""

A = int(input())
B = int(input())
C = int(input())
D = A
A = B
B = D
A = C*A
B = B+C
print(A)
print(B)