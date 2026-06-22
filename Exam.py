'''class A:
    def __init__(self):
        self.name=input('Enter your name=')
        self.age=int(input('Enter your age='))
        self.Branch=input('Enter your Branch=')
    def student_data(self):
        print('student name=',self.name)
        print('student age=',self.age)
        print('student branch=',self.Branch)
obj1=A()
obj2=A()
obj1.student_data()
obj2.student_data()'''
'''class Animal:
    def fun1(self):
        print('Parent class')
class Dog(Animal):
    def fun2(self):
        print('child class')
obj1=Dog()
obj1.fun1()
obj2=Animal()
obj2.fun1()'''
'''class number:
    def __init__(Q,value):
        Q.value=value
    def __add__(Q, other,w):
        return (Q.value+other.value+w.value)
obj11=number(10)
obj12=number(20)
obj13=number(30)
print(obj11.__add__(obj12,obj13)) '''
class hi():
    def __init__(self):
        self.__salary=1000
    def see(self):
        print('salary',self.__salary)
obj1=hi()
print(obj1._hi__salary)
