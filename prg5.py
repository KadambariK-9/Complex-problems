'''
INPUT
7
-7 1 5 2 -4 3 0
OUTPUT
3
INPUT
3
1 2 3
OUTPUT
-1
'''
n=int(input())
a=list(map(int,input().split()))
r=sum(a)
l=0
for i in a:
    r=r-i
    if r==l:
        print(a.index(i))
        break
    l=l+i
else:
    print(-1)

7
-7 1 5 2 -4 3 0
3

3
1 2 3
-1














'''
s=0
ss=0
ans=0
if n%2!=0:
    for i in range(n//2):
        s+=a[i]
        ss=a[(n//2)+1:]
        if s==ss:
            ans=n//2
        else:
            ans=-1
print(ans)


'''
