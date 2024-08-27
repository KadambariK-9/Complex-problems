'''
INPUT
3 2 11 7 6 5 6 1
OUTPUT
2 1 7 6 5 1 1 -1
'''
a=[int(x) for x in input().split()]
#a=list(map(int,input().split()))
l=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j] <a[i]:
            l.append(a[j])
            break
    else:
        l.append(-1)
print(*l)


3 2 11 7 6 5 6 1
2 1 7 6 5 1 1 -1
