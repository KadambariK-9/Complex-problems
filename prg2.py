'''
toggling all bits
constraints  1<=n<=100
input
10
output
5
note use only bitwise operators

'''
'''
INPUT 10
OUTPUT 5'''
from math import log2
n=int(input())
k=int(log2(n))+1
res=n^((1<<k)-1)
print(res)

10
5

12
3
