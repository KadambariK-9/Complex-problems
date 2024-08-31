'''
INPUT 43
OUTPUT YES
INPUT 123
OUTPUT NO
'''
n=int(input())
k=str(n)
sum=0
for i in k:
    sum+=int(i)
for i in range(2,sum//2):
    if sum%i==0:
        print('NO')
        break
    else:
        print('YES')


43
YES

123
NO
