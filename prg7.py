'''
INPUT
11101111011111
OUTPUT
CDE
'''
s=input()
res=''
l=s.split('0')
for i in l:
    res+=chr(i.count('1')+64)
print(res)




11101101111
CBD
