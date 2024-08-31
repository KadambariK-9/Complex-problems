'''
INPUT
APPLES
A
P
OUTPUT
PAALES
'''
a=input()
ch1=input()
ch2=input()
l=list(a)
for i in range(len(l)):
    if l[i]==ch1:
        l[i]=ch2
    elif l[i]==ch2:
        l[i]=ch1
print(''.join(l))


apples
a
p
paales
