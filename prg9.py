'''
INPUT
[4,5,0,1,9,0,5,0]
OUTPUT
[4,5,1,9,5,0,0,0]
'''
a=list(map(int,input().split()))
r1=[]
r2=[]
for i in a:
    if i==0:
        r1.append(i)
    else:
        r2.append(i)
r=r2+r1
print(r)

4 5 0  9 0 5 0
[4, 5, 9, 5, 0, 0, 0]
