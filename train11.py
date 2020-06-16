
''''
class employee:
    objectscount = count(0)
    index        = 0
    empid        = 0
    empname      = ''
    empaddress   = ''
    empsalary    = 0




    def __init__(self,empid1,empname1,empadress1,empsalary1):
        print('new object from employee')
        self.empid      = empid1
        self.empname    = empname1
        self.empaddress = empadress1
        self.empsalary  = empsalary1

    def getdata(self):
        return str(self.empid)+' ; '+self.empname+' ; '+self.empaddress+' ; '+str(self.empsalary)

    def printdata(self):
        print(self.getdata())

emp1=employee(2323,'qasem','jaba',4500)
#emp1.empid=111
#emp1.empname='ahmad'
#emp1.empaddress='jaba'
#emp1.empsalary=7600
emp1.printdata()
'''
'''
from itertools import count

class employee:
    objectscount=count(0)
    index=0
    empid=0
    empname=''
    empadress=''
    empsalary=0

    def __init__(self):
        self.index=next(self.objectscount)

    def getdata(self):
        return str(self.empid)+' ; '+self.empname+' ; '+self.empadress+' ; '+str(self.empsalary)

    def printdata(self):
        print(self.getdata())

emp1=employee()
emp2=employee()
emp3=employee()

print(emp1.index)
print(emp2.index)
print(emp3.index)

print(emp1.objectscount)
'''
x=0
class employee:

    empid=0
    empname=''
    empadress=''
    empsalary=0
    #global x
    #x=7

    def __init__(self):
        global x
        x +=1

    def changex(self,num):
        global x
        x=num

    def getdata(self):
        return str(self.empid)+' ; '+self.empname+' ; '+self.empadress+' ; '+str(self.empsalary)

    def printdata(self):
        print(self.getdata())

print(x)
emp=employee()
print(x)









input('press enter to exit...')













