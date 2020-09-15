#!/usr/bin/env python
# coding: utf-8

# # Functions
# 
# Functions are blocks of code that can be used over and over again to perform a specific action.
# 
# As we know, in Python, there are print (), len () etc. Many available functions are defined.
# 
# We can use it in our own code by providing access to functions defined in libraries, modules and packages. These are called predefined functions, embedded functions (built-in) or library functions. We can use ready-made functions as well as create our own functions. (User-defined)
# 
# 
# Functions prevent code repetition and our code stays more modular and organized.
# 
# 
# *****
# 
# def "function_name"(parameter1,parameter2,..):
# 
# 
# > "Do something"
# 
#   return "return something"  (depends on functionality) 
# 
# 
# 

# In[2]:


def hello():
  print("Hello Everyone!!")


# In[3]:


hello()#calling the func   #the functions don't have any parameters


# In[5]:


def hello(name):
  print("Hello " + name)


# In[6]:


hello("Dogukan")


# In[12]:


def func1():
  print("Hello World!!")


func1()
print("Dogukan Kaan Bozkurt")
func1()


# In[13]:


def summ(a,b):
  sum1 = a + b
  print(sum1)


# In[14]:


summ(6,7)


# In[15]:


t = summ(8,9)
print(t)


# In[16]:


def func(x,y):
  summ = x + y
  multip = x * y
  return (summ,multip)


# In[17]:


t,c = func(23,45)

print(t,c)


# In[18]:


func(3,5)


# In[19]:


x = 5 
y = 4
x,y = y,x
print(x,"and",y)


# In[20]:


print("Sum of the values: " + str(t) + ", Multiplying of the values: " + str(c))


# In[21]:


#Let's write a function that it will square the entered number, but will be terminated when you enter the number 5 and give us an error message.

def sqr(x):
  if x == 5:
    return ("Terminated because you entered 5")

  result = x **2
  return (result)


# In[25]:


def sqr1(x):
  if x == 5:
    return (len("Terminated because you entered 5"))

  result = x **2
  return (result)


# In[26]:


# Let's write a function that tells you whether the entered number is positive, negative or zero.


def func(x):
  if x > 0:
    return ("Positive")
  elif x < 0:
    return ("Negative")
  else:
    return ("Zero")


# In[27]:


for i in [-2,5,6,0,-4,-7]:
  print(func(i))


# In[28]:


# factorial calculation


def factorial(num):
  factorial = 1
  if (num == 0 or num == 1):
    print("Factorial: ", factorial)
  else:
    while (num >= 1):
      factorial = factorial * num
      num -= 1 
    print("Factorial: ", factorial)



# In[29]:


factorial(5)


# In[30]:


# 5* 4* 3* 2* 1 = 120


# In[31]:


#using for loop

def factorial2(num2):
  factorial2 = 1
  if (num2 == 0 or num2 == 1):
    print("Factorial: ", factorial2)
  else:
    for i in range(factorial2, num2+1):
       factorial2 = factorial2 * i      
    print("Factorial: ", factorial2)


# In[32]:


x = factorial2(5)
x


# In[33]:


for i in range(0,10):
    print(i)


# In[34]:


def factorial3(nums):
  factorial3 = 1
  if (nums == 0 or nums == 1):
    return ("Factorial: ", factorial3)
  else:
    for i in range(factorial3, nums+1):
       factorial3 *= i      
    return ("Factorial: ", factorial3)


# In[35]:


x = factorial3(6)
print(x)


# In[36]:


def hello2(name, capLetter = False):
  if capLetter:
    print("Hello " + name.upper())
  else:
    print("Hello " + name)


# In[37]:


hello2("Asli")


# In[38]:


hello2("Asli", capLetter= True)


# In[39]:


def multp(*args):
  result = 1
  for i in args:
    result = result * i
  print(result) 


# *args keeps the data as tuple type.


# In[40]:


multp(4,5,6,7,8)


# In[41]:


multp(2,3,4,5)


# In[42]:


def salaryCalc(salary):

  if salary < 0:
    return("Invalid value")
  else:
    if 0 < salary <= 1000:
      salary = salary + salary * 0.15
    elif salary <= 2000:
      salary = salary + salary * 0.1
    elif salary <= 3000:
      salary = salary + salary * 0.05
    else:
      salary = salary + salary * 0.025

    return ("New salary: ", salary)


# In[43]:


salaryCalc(-5)


# In[44]:



def salaryCalc2():

  salary = float(input("Please enter your current salary: "))

  if salary < 0:
    return("Invalid value")
  else:
    if 0 < salary <= 1000:
      salary = salary + salary * 0.15
    elif salary <= 2000:
      salary = salary + salary * 0.1
    elif salary <= 3000:
      salary = salary + salary * 0.05
    else:
      salary = salary + salary * 0.025

    return ("New salary: ", salary)
 


# In[45]:


new_salary = salaryCalc2() 
print(new_salary)


# In[46]:


def carpma(x,y):
    return x * y

carpma(3,5)


# In[47]:


def func_args(*numbers):
    print(numbers)

func_args(5,6,7,8,9)
func_args(100,"Global AI Hub")


# In[48]:


def func_args(*args):
    for i in args:
        print(i)

liste = [10,4.4,'Ahmet',True,"Istanbul",33,9.8]
func_args(liste)


# In[49]:


#kwargs
def func_kwargs(**number):
    print(number)
    
func_kwargs(num1 = 'Ankara', num2 = 'Kocaeli', num3 = True, num4 = 3.14)


# ### Let's write a function that returns a random word from a list.
# 
# ### Modules

# In[51]:


import numpy as np

import tensorflow as tf

import myModules as my_mod

myModules.myFunc()

from myModules import *

myFunc()


# In[52]:


#calling a function from myModules
my_mod.sum()
my_mod.multiple()


# In[53]:


words = ["artificial","intelligence","machine","learning","python","programming"]


#from random import *
import random as rnd

def randomWord(words):
  index = rnd.randint(0, len(words)-1)
  return words[index]
  


# In[54]:


len(words)


# In[55]:


word = randomWord(words)
print(word)


# ###Global & Local Variables

# In[56]:


x = 5

print(x)


# In[57]:


def display():
  x = 4
  return(x)


# In[58]:


display()


# In[59]:


print(x)


# ## Methods
# 
# Functions are called by name, it can take parameters inside and optionally the resulting value can be used outside of the function.
# 
# 
# Methods are also called by name, in many ways they are like functions, but calling is performed through an object such as a String or list.
# 
# 
# object.methodName(parameter)

# In[60]:


s = input("Please enter a name: ")

upper = s.capitalize()

print(upper)


# In[61]:


#return the index of the element with the highest value in a given list.

myList = [45,7,23,6,12,78]

maxElement = max(myList)

print(maxElement)

maxIndex = myList.index(maxElement)

print(maxIndex)

