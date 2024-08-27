'''
INPUT
321
OUTPUT 380
'''
s=input()
sum=0
for i in range(len(s)):
    for j in range(i,len(s)):
        sum+=int(s[i:j+1])
        print(sum)
print(sum)

'''
321
380
'''
    
