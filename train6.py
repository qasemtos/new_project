'''
import os
if not os.path.exists('my folder'):
    print('it is exist')
    os.mkdir('my folder')
if os.path.exists('myfile.txt'):
    print('yes')
else:
    print('no')
#os.remove('myfile.txt')
#os.rmdir('my folder')
#os.rmdir('my folder 2')

files=os.listdir('my files')
for file in files:
    if os.path.isfile('my files'+file):
        print(file)
#os.system('اسم الملف')
numbers=[num for num in range(11) if num%2==0]
print(numbers)
files=[f for f in os.listdir('my files') if os.path.isfile('my files'+f)]
for file in files: print(file)

import shutil
shutil.copy2('my files/اسم الملف','اسم المجلد اللي بدك تنسخ عليه الملف/اسم الملف اللي بدك تسجله')
shutil.move('....../....','...../....')
shutil.copytree('...../....','..../....')
'''
import datetime
dt=datetime.datetime.now()
d=datetime.datetime.now().date()
t=datetime.datetime.now().time()
myd=datetime.date(2000,1,31)
myt=datetime.time(15,20,10,123)
now=datetime.datetime.now()
d=now.day
m=now.month
y=now.year
h=now.hour
mi=now.minute
s=now.second
ms=now.microsecond
print(now)
print(myt)
print(myd)
print(t)
print(d)
print(dt)
print(str(d)+'/'+str(m)+'/'+str(y))
print(now.strftime('%a'))
print(now.strftime('%A'))
print(now.strftime('%b'))
print(now.strftime('%B'))
print(now.strftime('%c'))
print(now.strftime('%d'))
print(now.strftime('%H'))
print(now.strftime('%I'))
print(now.strftime('%j'))
print(now.strftime('%m'))
print(now.strftime('%M'))
print(now.strftime('%p'))
print(now.strftime('%S'))
print(now.strftime('%x'))
print(now.strftime('%X'))
print(now.strftime('%y'))
print(now.strftime('%Y'))
print(now.strftime('%I '))



import math
print(math.pi)
print(math.sqrt(81))
print(round(1.5))
print(math.ceil(1.1))
print(math.floor(1.99))
print(abs(-10))
print(math.fabs(-50))
print(pow(5,3))
print(math.factorial(5))
print(sum([1,2,3,4,5,6,7,9,8]))
print(math.fsum([1,2]))
s=[232,24,253,4646,36543,2]
print(sum(s)/len(s))
try:
    num1=2
    num2=0
    print(num1/num2)
except ZeroDivisionError as ex:
    print(ex)
except:
    print('an error')
finally:
    print('end')

