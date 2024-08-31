'''
INPUT
[73,74,75,71,69,72,76,73]
OUTPUT
[1,1,4,2,1,1,0,0]
'''
t=list(map(int,input().split()))
res=[0 for i in range(len(t))]
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[j]>t[i]:
            res[i]=j-i
            break
print(res)


73 74 75 71 69 72 76 73
[1, 1, 4, 2, 1, 1, 0, 0]
