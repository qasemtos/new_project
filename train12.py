class test:

    def __init__(self):
        print('new object created')

    def __del__(self):
        print('current object deleted')

t1=test()
del t1

class employee:
    city='jaba'
    name='empty'
    pass

emp=employee()
print(getattr(emp,'name'))
setattr(emp,'name','amr')
print(hasattr(emp,'city'))
#emp.name='ahmad'
delattr(emp,'name')
print(emp.name)


class otherdata:
    email='name@gmail.com'
    phone='0000000000000'


class person:
    name = 'person'
    address = 'jaba'

    def printdata(self):
        print(self.name+' ; '+self.address)

class employee(person,otherdata):
    pass

emp=employee()
print(emp.name)
print(emp.address)
print(emp.email)
print(emp.phone)
print('============')
emp.printdata()


class anything:
    'this is an anything class'
    name='empty'

    def printname(self):
        print(self.name)

print(anything.__dict__)
#any1=anything()

#any1.city='jaba'
#print(any1.__dict__)

class name:
    pass
print(name.__module__)
print('========')

import myfile
print(myfile.person.__name__)
print(myfile.person.__module__)

class other:
    pass
class person:
    name=''
    address=''
class employee(person,other):
    pass
class doctor(employee):
    pass
print(employee.__base__)
print(doctor.__base__)
print(person.__base__)
print('==============')

class other:
    pass
class person:
    pass
class employee(person,other):
    pass
import inspect
print(inspect.getmro(employee))
#print(employee.__base__)
print('===============')

class others:
    pass
class otherdata:
    email=''
    phone=''
class person:
    name=''
    address=''
class employee(person,otherdata,others):
    employeeid=0
class doctor(employee):
    pass
print(otherdata.__bases__)
print('-------')
print(employee.__bases__)
print('------')
print(doctor.__bases__)

class person:
    def printtyype(self):
        print('person')
class customer(person):
    def printtyype(self):
        print('customer')
    pass
class employee(person):
    def printtyype(self):
        print('employee')
    pass
class doctor(employee):
    def printtyype(self):
        print('doctor')
    pass
p=person()
c=customer()
e=employee()
d=doctor()
print('========')
p.printtyype()
c.printtyype()
e.printtyype()
d.printtyype()



class person:
    def printtyype(self):
        print(self.__class__.__name__)
class customer(person):
    pass
class employee(person):
    pass
class doctor(employee):
    pass
p=person()
c=customer()
e=employee()
d=doctor()
print('%%%%%%%%%%%%%%%%%')
p.printtyype()
c.printtyype()
e.printtyype()
d.printtyype()



input('press enter to exit...')