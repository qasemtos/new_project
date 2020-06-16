"""class car:
    def __init__(self,givename):
        self.name=givename
        self._status="idle"
        self.__speed=0

    def set_status(self,st):
        self._status=st
    def get_status(self):
        return self._status
    def get_name(self):
        return self.name
    def set_speed(self,sp):
        self.speed=sp
    def get_speed(self):
        return self.speed
    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self,sp):
        self.__speed=sp

distance=((p2.x-p1.x)**2+(p2.y-p1.y)**2+(p2.z-p1.z)**2)**0.5
speed=property(get_speed,set_speed)
car1.set_speed(50)
print(car1.get_speed())
car1.speed=40
print(car1.speed+10)
car1=car('bora')
print(type(car1))
print(car1.get_name())
car1.set_speed(90)
print(car1.get_speed())
class car5:
    description="4-wheel vehicle"
    def __init__(self,givename):
        self.name=givename

c1=car5('bora')
c2=car5('bmw')
print(c1.name)
print(c2.name)
print(c1.description)
print(c2.description)
print(car5.description)
#car5.description='smart car'
c1.description='smart car'
print(c1.description)
print(c2.description)

class libraryitem:
    def __init__(self,id,title):
        self.id=id
        self.title=title
    def print_info(self):
        print('item id: '+str(self.id))
        print('title: '+self.title)
item1=libraryitem(656,'hello')
item1.print_info()

class book(libraryitem):
    def __init__(self,id,title,author,isbn):
        libraryitem.__init__(self,id,title)
        self.author=author
        self.isbn=isbn
    def print_info(self):
        libraryitem.print_info(self)
        print('author'+self.author)
        print('isbn'+str(self.isbn))
    def read(self):
        print('read: '+self.title+'  for u')
#print(isinstance(ab1,audiobook))
print(book.mro())
b1=book(112,'hello','ali',64874)
print(b1.author)
print(b1.isbn)
b1.print_info()
b1.read()
print(book.mro())
def print_info(self):
    super().print_info()

def __init__(self,**kwargs):
    self.id=kwargs['id']
    self.title=kwargs['title']

def __init__(self,**kwargs):
    super().__init__(**kwargs)
    self.isbn=kwargs['isbn']
    super().__init__(**kwargs)"""
class person:
    def __init__(self,age,name):
        self.age=age
        self.name=name

    def __lt__(self, other):
        return self.age<other.age
    def __str__(self):
        return 'student '+self.name+' is '+str(self.age)+' years old'
p1=person(10,'ali')
p2=person(20,'ahmad')
print(p1<p2)
if (p1<p2):
    print(p1.name+' is less than '+p2.name)
print(p1)
print(p2)


class vector(list):
    def __init__(self,lst):
        list.__init__(self,lst)
    def __add__(self, other):
        if len(self)!=len(other):
            return None
        result=list(self)
        for i in range(len(self)):
            result[i]=self[i]+other[i]
        return result
v1=[1,2,4,5]
v2=[6,7,8,9]
print(v1+v2)




