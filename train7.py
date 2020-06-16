emp=set()
emp.add('ahmad')
emp.add('ali')
emp.add(77)
emp.add(True)
print(emp)
#emp.clear()                    #حذف جميع العناصر مرة وحدة
print(emp)
emp.remove(77)
print(emp)
emp.discard('ali')
emp.discard(99)
print(emp)
c1=['ahmad','amr','adel','ehab']
c2=['ali','yaser','ahmad','amr']
com1=set(c1)
com2=set(c2)
print(com1)
print(com2)
print(com1.union(com2))
print(com1.intersection(com2))
import csv
f=open('E:\pycharm\my folder\info.csv')
r=csv.reader(f)
g1=next(r)
print(g1)
g2=next(r)
print(g2)
g3=next(r)
print(g3)
f.close()
def f1():
    print('hello world')
    print('hello every one')
f1()
def f2():
    print('welcome to jaba')
f2()
def hi(name):
    print('hello'+' '+name)
hi('ahmad')
def add(num1,num2):
    print(num1+num2)
add(7,7)
def cal(num1,num2,ope):
    if ope=='+':
        print(num1+num2)
    elif ope=='-':
        print(num1-num2)
    elif ope=='*':
        print(num1*num2)
    else:
        if num2==0: num2=1
        print(num1/num2)
cal(7,3,'+')
cal(7,3,'-')
cal(7,3,'*')
cal(6,0,'/')








print('press enter to exit')





























