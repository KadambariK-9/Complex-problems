'''
INPUT
7
5 6 4 5 2 3 4
OUTPUT
2
INPUT
5
5 4 3 2 1
OUTPUT 4
'''
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            c+=1
        break
print(c)


5
5 4 3 2 1
4
