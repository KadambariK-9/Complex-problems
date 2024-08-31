'''
INPUT
6(N)
8 10 6 2 9 7
OUTPU 3
'''
a=[int(x) for x in input().split()]
s=a[-1]
c=1
i=len(a)-2
while i>=0:
    if a[i]>s:
        c+=1
        s=a[i]
    i-=1
print(c)


8 10 6 2 9 7
3
