'''
INPUT
Hello wORld
OUTPUT
hello world
INPUT
How ARE You
OUTPUT
HOW ARE YOU
'''
s=input()
uc=0
lc=0
for i in s:
    if i.isupper():
        uc+=1
    elif i.islower():
        lc+=1
if uc>lc:
    print(s.upper())
else:
    print(s.lower())


Hello wORld
hello world

How ARE You
HOW ARE YOU
