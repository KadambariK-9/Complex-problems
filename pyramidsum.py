#PYRAMID SUM
'''
                1
              2 1 2
            3 2 1 2 3
          4 3 2 1 2 3 4
        5 4 3 2 1 2 3 4 5
     N________2 1 2________N

input 3....1+...2+1+2....3+2+1+2+3
=17
     
INPUT
3
OUTPUT
17
'''
s=0
r=int(input())
for i in range(2,r+1):
    n=i
    while n>1:
        s+=2*n
        n=n-1
s+=r
print(s)

'''
1
1

3
17

4
36
'''




