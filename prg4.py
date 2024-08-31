'''
fav song is a
so make substring of into x parts and see no of a
print max a
if no a in string print 0
INPUT
ABCACA
3
OUTPUT
2
INPUT
DEFGHUGF
3
OUTPUT
0

a=input()
n=len(a)
x=int(input())
if n%x==0:
    print(n//x)
else:
    print(0)

'''
s=input()
k=int(input())
m=0
for i in range(len(s)-k+1):
    c=s[i:i+k].count('a')
    if c>m:
        m=c
print(m)










'''
abcaca
3
2

defghugh
3
0


'''

