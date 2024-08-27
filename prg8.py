'''
INPUT
ABC
OUTPUT
ADBECFGH
'''
s=input()
t=input()
res=''
i=0
while i<len(s) or i<len(t):
    if i<len(s):
        res+=s[i]
    if i<len(t):
        res+=t[i]
    i+=1
print(res)



abc
defgh
adbecfgh
