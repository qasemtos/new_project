my='hello amr and welcome back'
i=my.find('ahmad')
print(i)
i=my.find('amr')
print(i)
print(my[i:])
print('abcnkadsh'.isalpha()) #هل هذه حروف
print('abcjdshoKGJ897'.isalnum()) #هل هذه حروف وارقام
print('29387592'.isdecimal())#هل هذه ارقام
print('97493797'.isdigit())#هل هذه ارقام
print('84397'.isnumeric())#هل هذه ارقام
print(' '.isspace()) #هل هذه مسافات
my6='hello ahmad\n'
my7='welcome ahmad\n'
my=my6+my7
my8=my.replace('ahmad','qasem')
print(my8)
str1='ali,ahmad,omar,qasem'
str2=str1.split(',')
print(str2[3])
my='hello'
my2='-'.join(my)
print(my2)
my=['ahmad','ali','omar','ameer']
my2='-'.join(my)
my3='\n'.join(my)
print(my2)
print(my3)
file=open('myfile.txt','r')
text=file.read()
#print(text)
#book=['ali\n','ahmad\n','omar']
#file.writelines(book)
file.seek(0)
mylines=file.readlines()
print(mylines)
file.close()
file=open('qaem.txt','a')
file.write('welcome\n')
file.close()
print('press enter to exit')
'''
file=open('horse','rb')                       القراءة من ملف باينري
file=open('horse','wb')                               #الكتابة على ملف باينري
text=file.read()
print(text)
'''
with open('myfile.txt','w') as file:
    file.write('hello\n')
    file.write('welcome\n')
    file.write('hi\n')
import os
#os.mkdir('my folder')
os.makedirs('my folder 2')




















