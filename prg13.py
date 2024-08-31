'''
INPUT
[5,5,5,10,20]
OUTPUT
TRUE
'''
a=[int(x) for x in input().split()]
c={5:0,10:0,20:0}
for x in a:
    c[x]+=1
    ch=x-5
    if ch==15:
        if c[10]>0:
            c[10]-=1
            ch-=10
    c[5]-=ch//5
if c[5]<0:
    print(False)
else:
    print(True)

5 5 5 10 20
True
