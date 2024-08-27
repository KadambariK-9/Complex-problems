'''
INPUT
12axy44
OUTPUT
56
INPUT
24ab7hg27
58'''

s=input()
num=0
res=0
for i in s:
    if i.isdigit():
        num=num*10+int(i)
    else:
        res+=num
        num=0
res+=num
print(res)



12cs44
56
'''

a=input()
n=len(a)
l=[]
for i in range(n-1):
    s=''
    c=0
    if a[i].isdigit() and a[i+1].isdigit():
        s+=a[i]
        s+=a[i+1]
        c=int(s)
        l.append(c)
    elif a[i].isdigit():
        l.append(int(a[i]))
print(l)

s=0
for j in l:
    s+=j
print(s)        




LOGIC FOR REVERSING
REV=0
TEMP=NUM
WHILE NUM!=0:
    REM=NUM%10
    SUM=SUM*10+REM
    NUM=NUM//10
PRINT(SUM)'''
    
