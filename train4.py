emp={'id':111,'name':'amr','salary':85745,'city':'jaba'}
print(emp.items())
for k,v in emp.items():
    print(k)
    print(v)
    print(str(k)+' ; '+str(v))
    print('------')

x=1
while True:
    print(x)
    x+=1
    if x>100:
        break


from itertools import count
for x in count():
    print(x)
    if x==100:
        break

for x in range(1,11):
    print(x)
    if x==5:
        break
'''
count = int(input('enter numbers count: '))
summ=0
for x in range(count):
    num=int(input('enter new number'+str(x+1)+' ; '))
    if num==0:continue
    summ +=num
    print('ok')
print(summ)
'''
str1='hello \\ \' \"qasem\" world'
str2='welcome to jaba\rhello'
str3='hello\nworld'
str4="\a"
str5='hello\b\baa'
str6='hello\tworld'
str7='\x41   \101 \u0041'
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)

my='''hello ahmad 
hello omar
hello ali 
gjhfkjcfk
bjhvgkjch
'''
print(my*3)
str8='\N{copyright sign}'
str9='\N{registered sign}'
str10='\N{up down arrow}'
str11='\N{left right arrow}'
print(str8)
print(str9)
print(str10)
print(str11)
print(my[:-24])
my='hello %s fgjf'%'ahmad'
my='hello %d fgjf'%6876906
my2='num1%s,num2%s,num3%s'%(111,222,333)
print(my2)
print(my)
my='%c'%'A'
print(my)
my='%i'%5.5
print(my)
my='%E'%5.5
print(my)
my3='%X'%657986
print(my3)
my4='HELLO'
print(my4.lower())
my5='hello'
print(my5.isupper())





















































