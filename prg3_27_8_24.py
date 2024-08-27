'''
INPUT
WORD
...... CONDITION   A->F B->G C->H D->I ........U->Z V->A W->B .......Z->E
OUTPUT
BTWI
'''
a=input().lower()
s=''
for i in a:
    if ord(i)<ord('v'):
        s+=chr(ord(i)+5)
    else:
        s+=chr(ord(i)+5-26)
print(s)



word
btwi
