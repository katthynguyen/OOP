from random import randrange


class Employee:
    def __init__(self,first,last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
        # self.email = first + '.'+last+ str(symble)+'@email.com'

    @property
    def email(self):
        symble = randrange(100)
        return '{}{}{}{}'.format(self.first,self.last,symble,'@fpt.com.vn')

    @property    
    def fullname(self):
        return '{}'.format(self.first)+' '+'{}'.format(self.last)+ ' ' + '{}'.format(self.pay)
    
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None

    @classmethod
    def full_more(cls, str):
        if len(str) < 3:
            return cls.email
        first, last, pay = str.split()
        return cls(first,last,pay)

    def __repr__(self) -> str:
        return "Emplyee("'{}'.format(self.first)+' '+'{}'.format(self.last)+ ' ' + '{}'.format(self.pay) +")"
emp_1 = Employee('kat','nguyen',50)
# print(emp_1.full_more(emp_1.fullname()))
# print(emp_1.fullname)
# print(emp_1.email)

emp_1.fullname = 'Katthy nguyen'
print(emp_1.fullname)
del emp_1.fullname
# inheritated
class Manager(Employee):
    def __init__(self, first, last, pay,like):
        # super.__init__(first, last, pay)        
        Employee.__init__(self,first,last,pay)
        self.like = like


# # print(help(Manager))
ma = Manager('ji','hin',60,56)
print(ma.email)
print(ma.fullname())
print(ma.__dict__)
# print(ma.like)

# print(emp_1)