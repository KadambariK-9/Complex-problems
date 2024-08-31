'''
INPUT
4
OUTPUT 1
INPUT 5
OUTPUT 2
'''
n=int(input())
c=0
for i in range(1,n+1):
    k=str(bin(i))[2:]
    l=list(k)
    for i in range(len(l)):
        if l[i]=='0':
            l[i]='1'
        elif l[i]=='1':
            l[i]=2
    sum=0
    for i in l:
        sum+=int(i)
    if sum%2==1:
        c+=1
print(c)


4
1

5
2
