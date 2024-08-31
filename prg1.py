'''
NEXT DECREASING ELEMENT
INPUT
7
5 6 4 5 2 3 4
OUTPUT
2
INPUT
5
5 4 3 2 1
OUTPUT
4
'''
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n-1):
    if a[i+1]<a[i]:
        c+=1
print(c)



7
5 6 4 5 2 3 4
2


5
5 4 3 2 1
4
