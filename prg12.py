'''
INPUT
ABC
OUTPUT
2
INPUT
CDF
OUTPUT
6
'''
a=input().lower()
s='bcdfghjklmnpqrstvwxyz'
c=0
for i in a:
    if i in s:
        c+=1
print(c)


abc
2

CDF
3
