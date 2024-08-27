'''
INPUT........MAN
OUTPUT 377
'''
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
s=input()
sum=0
for i in s.lower():
    v=fib(ord(i)-96)
    sum+=v
print(sum)


MAN
377
