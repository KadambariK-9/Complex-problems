'''
for n=3
333222111
332211
321
'''
n=int(input())
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print((str(j)+'')*i,end='')
    print()


3
333222111
332211
321

