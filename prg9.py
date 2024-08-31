'''
xor used to toggle
clear the kth bit of a number
'''
n=int(input())
k=int(input())
r=n&(~(1<<(k-1)))
print(r)


11
2
9
