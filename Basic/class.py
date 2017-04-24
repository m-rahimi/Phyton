# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 09:53:50 2017

@author: Amin
"""

"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def getClassiness(self):
        classiness = 0
        if len(self.items) > 0:
            for item in self.items:
                if item == "tophat":
                    classiness += 2
                elif item == "bowtie":
                    classiness += 4
                elif item == "monocle":
                    classiness += 5
        return classiness

# Test cases
me = Classy()

# Should be 0
print me.getClassiness()

me.addItem("tophat")
# Should be 2
print me.getClassiness()

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print me.getClassiness()

me.addItem("bowtie")
# Should be 15
print me.getClassiness()

###############################################
""" Calculate angle between two planes defined by four points"""
import math
class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        x = self.x - no.x
        y = self.y - no.y
        z = self.z - no.z
        return Points(x, y, z)

    def dot(self, no):
        x = self.x * no.x
        y = self.y * no.y
        z = self.z * no.z
        return x + y + z

    def cross(self, no):
        x = self.y * no.z - self.z * no.y
        y = self.z * no.x - self.x * no.z
        z = self.x * no.y - self.y * no.x
        return Points(x, y, z)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


points = list()
for i in range(4):
    a = map(float, raw_input().split())
    points.append(a)

A, B, C, D = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
X = (B - A).cross(C - B)
Y = (C - B).cross(D - C)
angle = math.acos(X.dot(Y) / (X.absolute() * Y.absolute()))

print "%.2f" % math.degrees(angle)

##################################################################################
""" Operation in two complex number """
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)

    def __div__(self, no):
        x = float(no.real ** 2 + no.imaginary ** 2)
        y = self * Complex(no.real, -no.imaginary)
        real = y.real / x
        imaginary = y.imaginary / x
        return Complex(real, imaginary)

    def mod(self):
        real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(real, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


C = map(float, raw_input().split())
D = map(float, raw_input().split())
x = Complex(*C)
y = Complex(*D)
print '\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))
######################################################################
# inheritance
class Pet(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)
    
class Dog(Pet):

    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats
    
class Cat(Pet):

    def __init__(self, name, hates_dogs):
        Pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs

    def hatesDogs(self):
        return self.hates_dogs
    
mister_pet = Pet("Mister", "Dog")
mister_dog = Dog("Mister", True)

#The function used below, isinstance, is a special function that checs to see 
#if an instance is an instance of a certain type of class.

isinstance(mister_pet, Pet)
isinstance(mister_pet, Dog)
isinstance(mister_dog, Pet)
isinstance(mister_dog, Dog)

fido = Dog("Fido", True)
rover = Dog("Rover", False)
mittens = Cat("Mittens", True)
fluffy = Cat("Fluffy", False)
print fido

print rover

print mittens

print fluffy

print "%s chases cats: %s" % (fido.getName(), fido.chasesCats())

print "%s chases cats: %s" % (rover.getName(), rover.chasesCats())

print "%s hates dogs: %s" % (mittens.getName(), mittens.hatesDogs())

print "%s hates dogs: %s" % (fluffy.getName(), fluffy.hatesDogs())
