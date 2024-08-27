'''
INPUT
BALLARI
OUTPUT
B=1
A=2
L=2
R=1
I=1

s=input()
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d:
    print(i,'=',d[i])


ballari
b = 1
a = 2
l = 2
r = 1
i = 1


'''


s=input()
for i in s:
    if i not in s:
        s+=i
for i in s:
    c=s.count(i)
    print(i,':',c)




    khushi
k : 1
h : 2
u : 1
s : 1
h : 2
i : 1


