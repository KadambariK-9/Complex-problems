'''
binary if we use odd no  & 1  output is 1
even & 1==0
'''
#find even or odd using bitwise
n=int(input())
if(n&1):
    print('odd')
else:
    print('even')
