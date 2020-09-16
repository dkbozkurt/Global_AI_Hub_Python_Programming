#!/usr/bin/env python
# coding: utf-8

# # Exceptions 
# 
# * Programmer Errors 
# * Program Bugs 
# * Exceptions
# 
# 
# 

# In[1]:


# error example,SyntaxError.

print "Hello World!"   


# In[2]:


#bug example.

num1 = input("Enter the first integer: ")
num2 = input("Enter the second integer: ")

print(num1, "+", num2, "=", num1 + num2)


# In[ ]:


#exception example, TypeError.

num3 = int(input("First integer: "))
num4 = int(input("Second integer: "))

print(num3, "/",num4, "=", num3 / float(num4))


# In[ ]:


int(3)


# In[ ]:


#ValueError
int("Hello World")


# In[ ]:


# ZeroDivisionError.


num3 = int(input("First integer: "))
num4 = int(input("Second integer: "))

print(num3, "/",num4, "=", num3/num4)


# In[ ]:


3 + 5


# In[ ]:


#bug example.

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

print(num1, "+", num2, "=", num1 + num2)


# ##Exception Handling
# 
# 
# try:
# 
# 
# > the situations where we can get exceptions
# 
# except "Exception Name":
# 
# 
# > the operations in case of exceptions
# 
# 
# 
# 

# In[ ]:


x = "Alan Turing"

int(x)


# In[ ]:


try:
  int(x)

except ValueError:
  print("Please enter an integer value!!!")


# In[ ]:


num3 = input("First integer: ")
num4 = input("Second integer: ")

try:
  num3_int = int(num3)
  num4_int = int(num4)

  print(num3_int, "/",num4_int, "=", num3_int/num4_int)

except ValueError:
  print("Please enter an integer value!!!")


# In[ ]:


num3 = input("First integer: ")
num4 = input("Second integer: ")

try:
  num3_int = int(num3)
  num4_int = int(num4)

  print(num3_int, "/",num4_int, "=", num3_int/num4_int)

except ZeroDivisionError:
  print("Please enter the second input different than 0 value!!!")


# In[ ]:


num3 = input("First integer: ")
num4 = input("Second integer: ")

try:
  num3_int = int(num3)
  num4_int = int(num4)

  print(num3_int, "/",num4_int, "=", num3_int/num4_int)

except ValueError:
  print("Please enter an integer value!!!")
except ZeroDivisionError:
  print("Please enter the second input different than 0 value!!!")
except:
  print("Unknown error...")


# In[ ]:


num3 = input("First integer: ")
num4 = input("Second integer: ")

try:
  num3_int = int(num3)
  num4_int = int(num4)

  print(num3_int, "/",num4_int, "=", num3_int/num4_int)

except (ValueError, ZeroDivisionError):
  print("Error!!!")


# In[ ]:


#try/except/as


num3 = input("First integer: ")
num4 = input("Second integer: ")

try:
  num3_int = int(num3)
  num4_int = int(num4)

  print(num3_int, "/",num4_int, "=", num3_int/num4_int)

except ValueError as error:
  print("Error!!!")
  print("Error message: ", error)


# In[ ]:


#exception handling in loop structure


while True:
    num1 = input("First number: (Press q for quit the program): ")

    if num1 == "q":
        break

    num2 = input("Second number: ")

    try:
        num1_int = int(num1)
        num2_int = int(num2)
        print(num1_int, "/", num2_int, "=", num1_int / num2_int)
    except (ValueError, ZeroDivisionError):
        print("Error!")
        print("Please try again!")


# In[ ]:


"""
exception handling in functions
using raise command
"""


def reverse(s):

    if (type(s) != str):
        raise ValueError("Please enter a String type.")
    else:
        return s[::-1]


# In[ ]:


reverse("python")


# In[ ]:


reverse(12)


# In[ ]:


#finally
try:
    a = int(input("number1:"))
    b = int(input("number2:"))
    print(a/b)
except ValueError:
    print("Please Check value out")
except ZeroDivisionError:
    print("it cannot be divided by zero")
finally:
    print("show must go on")
    print("Hello world")


# # Intro to Object Oriented Programming
# 
# Every entity we see around us is an object.
# Each object has its own attributes and a set of functions (methods) they perform.
# 
# The concept we call class is also the data types that enable us to generate objects.
# 
# 

# In[ ]:


sesli_harfler = 'aeıioöuü'
sayac = 0
def kelime_al():
    return input('Bir kelime giriniz:')

def sesli_harf(harf):
    return harf in sesli_harfler

def artır(sayac,kelime):
    for harf in kelime:
        if sesli_harf(harf):
            sayac = sayac + 1
    return sayac

def ekrana_bas(kelime):   
    mesaj = '{} kelimesinde {} sesli harf var.'
    print(mesaj.format(kelime,artır(sayac,kelime)))
    
def calıstır():
    kelime = kelime_al()
    ekrana_bas(kelime)

calıstır()


# In[ ]:


class HarfSayacı:
    def __init__(self):
        self.sesli_harfler = 'aeıioöuü'
        self.sayaç = 0

    def kelime_sor(self):
        return input('Bir kelime girin: ')

    def seslidir(self, harf):
        return harf in self.sesli_harfler

    def artır(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayaç += 1
        return self.sayaç

    def ekrana_bas(self):
        mesaj = "{} kelimesinde {} sesli harf var."
        sesli_harf_sayısı = self.artır()
        print(mesaj.format(self.kelime, sesli_harf_sayısı))

    def çalıştır(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

if __name__ == '__main__':
    sayaç = HarfSayacı()
    sayaç.çalıştır()


# In[ ]:


class Worker():
    pass


"""
class Worker:
    pass
"""


# In[ ]:


#class attributes
class Car():
  colour = "yellow"
  brand = "xyz"
  door = 4


# In[ ]:


#instantiation
car1 = Car()

print(car1)


# In[ ]:


print(car1.colour)
print(car1.brand)
print(car1.door)


# In[ ]:


car2 = Car()

car2.colour


# In[ ]:


#We can also call attributes over the class without creating an object.

Car.door


# In[ ]:


Car.brand


# In[ ]:


dir(car1)


# In[ ]:


"""
In order to create each object with different values at the beginning,
we need to send the values of the objects.
For this, we use a special method: __init () __

The init () method is defined as a constructor function.

It is the first function that is automatically called up while creating our objects.

By defining this method specially, we can create our objects with different values.

"""



# In[ ]:


class Car2():

  def __init__(self): 
    print("init function calling...")


# In[ ]:


car_init = Car2()
car_init


# In[ ]:


"""

self= to access any variable or other methods in the defined class.

"""


# In[ ]:


car = Car2()


# In[ ]:


class Car3():

  def __init__(self,colour,brand,door):
    print("Hello Car world")
    self.colour = colour
    self.brand = brand
    self.door = door
    print(self.colour,self.brand,self.door)


red_car = Car3("red", "abc",2)

yellow_car = Car3("yellow", "xyz", 4)

print(red_car.colour)
print(yellow_car.brand)


# In[ ]:


blue_car = Car3("black","34abc23",5)
print(blue_car)


# In[4]:


class Person():
  name = ""
  age = 0
    
  def __init__(self, personName, personAge):
    self.name = personName
    self.age = personAge


  def welcomePerson(self):
    print("Hello " + self.name)

  
  def showAge(self):
    print(self.age)


# In[5]:


person1 = Person ("Dogukan Kaan", 22)

person1.welcomePerson()


# In[6]:


person1.showAge()


# In[8]:


class Person3():

  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.language = []
 


  def welcomePerson(self):
    print("Hello " + self.name)

  
  def showAge(self):
    print(self.age)


  def addLang (self, new_lang):
    print("Adding new language..")
    self.language.append(new_lang)

  
  def showInfo(self):
    print("{} is {} years old and can speak these languages: ".format(self.name,self.age))
    for i in self.language:
      print(i)
        
        

        
        


# In[10]:


person3 = Person3("dogukan",22)


# In[11]:


person3.welcomePerson()


# In[12]:


person3.showAge()


# In[13]:


person3.addLang("korean")


# In[14]:


person3.showInfo()


# In[15]:


person3.addLang("english")


# In[16]:


person3.showInfo()


# ##### Dogukan Kaan Bozkurt
