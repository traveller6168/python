#!/usr/bin/env python3

class Person:
    def __init__(self,name = '',age = 0):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @age.setter
    def age(self,age):
        if 0 < age <= 150:
            self.__age =age

    @name.setter
    def name(self,name):
        self.__name = name

    def display(self):
        print(self)

    def __str__(self):
        return "Person('%s',%s)" % (self.__name,self.__age)

    def __repr__(self):
        return str(self)

p = Person('Lisa',10)
print(p)
p._Person__age = 30
p._Person__name = 'UU'
print(p)
print(p)