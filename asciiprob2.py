'''
INPUT : ABCD
OUTPUT : ZYXW

// ONLY FOR UPPER CASE
a=input()
c=''
for j in a:
    c+=chr(ord('A')+ord('Z')-ord(j))
    #s+=chr(c)
print(c)



ABCD
ZYXW
'''

#FOR BOTH UPPER AND LOWER

a=input().upper()
s=''
c=''
for j in a:
    c+=chr(ord('A')+ord('Z')-ord(j))
    #s+=chr(c)
print(c)


abcd
ZYXW
