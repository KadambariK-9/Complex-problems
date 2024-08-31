'''
INPUT
10
OUTPUT
3
INPUT 2
OUTPUT 1
'''
n=int(input())
b=str(bin(n))[2:]
str0='';
str1=''
for i in b:
    if i=='0':
        str0+=i
    else:
        str1+=i
res=str0+str1
k=0
sum=0
i=len(res)-1
while i>=0:
    sum+=int(res[i])*(2**k)
    k+=1
    i-=1
print(sum)
'''
print(int(res,2))

2
1

10
3
'''



