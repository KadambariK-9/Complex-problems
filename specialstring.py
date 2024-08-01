#SPECIAL STRING
'''
A=65
Z=90
a=97
z=122
INPUT
abcd
xyz
OUTPUT
86



a=input()
s=input()
total=0
for i in a:
    if i not in s:
        temp=125
        for j in s:
            d=abs(ord(i)-ord(j)))
            if d<temp:
                temp=d
            total+=temp
        print(total)














a1=input()
a2=input()
mn=999
s=0
for i in range(len(a1)):
    for j in range(len(a2)):
        d=abs(ord(a1[i])-ord(a2[j]))
        if mn>d:
            mn=d
            s+=mn
print(s)



abcd
xyz
86

abcd
efg
10
'''
