def hi(name1,name2):
    print('hello '+name1)
    print('hello '+name2)
hi('ahmad','amr')
from my import cal
from my import hiall
cal(7,3,'+')
cal(7,3,'-')
cal(7,3,'*')
cal(7,3,'/')
hiall('ahmad','ali','omar')
exec (open('my.py').read())

def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
print(fact(5))
import os
import sys
help(sys.path)
help(os)
print(dir())











input('press enter to exit...')
