'''
INPUT
7
OUTPUT
3

l=[1]
c=0
n=int(input())
l=[2**i for i in range(1,(n//2)+1)]
for i in range(1,n+1):
    if i in l:
        c+=1
print(c)
'''
n=int(input())
c=str(bin(n))
print(c.count('1'))


7
3
