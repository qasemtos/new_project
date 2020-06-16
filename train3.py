'''

r1=range(ord('a'),ord('z')+1)
print(chr(r1[25]))
for x in range(2,11,2):
    print(x)
for x in range(ord('A'),ord('Z')):
    print(x)
    print(chr(x))
'''
names=['amr','ahmad','ali','qasem']
for name in names:
    print('hello' + ' ' +name)
l1=[77,True,99,5.5,'hello',False,77.7,'welcome']
for v in range(len(l1)):
    print(l1[v])
    print(type(v))
l1=(77,True,99,5.5,'hello',False,77.7,'welcome')
for v in range(len(l1)):
    print(l1[v])
    print(type(v))
d1={'name':'ahmad','salary':34833,'city':'jaba'}
for v in d1:
    print(d1[v])

x=1
while x<=10:
    print(x)
    x +=1
else:
    print("end"+ " "+ str(x))

myt=('hello',55,True,'ahmad',False)
x=0
while x<len(myt):
    print(myt[x])
    x +=1
myt=['hello',55,True,'ahmad',False]
x=0
while x<len(myt):
    print(myt[x])
    x +=1
myd={'name':'ahmad','salary':5457,'city':'jaba'}
print(list(myd.keys())[0])
mykey=list(myd.keys())
x=0
while x<len(myd):
    print(myd[mykey[x]])
    x +=1
again='y'
while again=='y':
    num1=int(input('enter the first number'))
    num2=int(input('enter the second number'))
    r=num1+num2
    print(r)
    again=input('y or n')





































