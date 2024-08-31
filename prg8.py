'''
9--> 1001 & 0001==>1
10-->1010 & 0001==>0
1001-->1011=11
11-->1011
12-->1100


1001
0001
------
1000

TOGGLE THE KTH BIT OF NUMBER
using bitwise XOR(^)
'''
n=int(input())
k=int(input())
r=n^(1<<(k-1))
print(r)


9
2
11
