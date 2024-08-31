'''
Input
abd
aabccad
output 4
'''
a=input()
s=input()
l=list(s)
for i in l:
    if i in a:
        l.remove(i)
print(len(l))


abd
aabccad
4
