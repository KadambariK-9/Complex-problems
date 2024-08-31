'''
INPUT
8
1 2 3 4 4 5 5 5
OUTPUT
2
INPUT
5
5 5 5 5 5
OUTPUT
0
'''
n=int(input())
a=[int(x) for x in input().split()]
m=a[-1]
for i in range(n-1,0,-1):
    if a[i]<m:
        m=a[i]
        print(a.count(a[i]))
        break
else:
    print(0)


8
1 2 3 4 4 5 5 5
2
