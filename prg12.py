'''
INPUT
10 20 30 40 50 60
6
OUTPUT 120
INPUT 21 24 67 13 24 27
OUTPUT 4
'''
a=list(map(int,input().split()))
a.reverse()
n=int(input())
s=0
for i in range(n):
    print(i,'',a[i])
    if i%2==0:
        s+=a[i]
print(s)


10 20 30 40 50 60
6
0  60
1  50
2  40
3  30
4  20
5  10
120.....................ans









