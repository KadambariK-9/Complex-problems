'''
N=4
1
2 3
4 5 6
7 8 9 10

n=int(input())
c=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c,end='')
        c+=1
    print()


4
1
23
456
78910
'''
n=int(input())
c=65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(c),end='')
        c+=1
    print()




4
A
BC
DEF
GHIJ

