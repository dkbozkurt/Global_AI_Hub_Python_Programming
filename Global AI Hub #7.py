#!/usr/bin/env python
# coding: utf-8

# ### Tek satır if (One-liner if)

# In[ ]:


koşul = 3

if koşul > 5:
    kelime = "Elma"
elif koşul > 7:
    pass
else:
    kelime = "Armut"
    print(kelime)


# In[ ]:


kelime = "Elma" if koşul else "Armut" if koşul > 5 else "Çilek"


# ### Tek satır fonksiyon Lambda (One-liner function Lambda)

# In[ ]:


def hello_world():
    return "Hello World"

hello_world()


# In[ ]:


def kare_alma(x):
    x = x ** 2
    return x

kare_alma(5)


# In[ ]:


kare_al = lambda x: x**2
kare_al(5)


# ### map, reduce, filter, zip fonksiyonları

# In[ ]:


sayılar = [1, 2, 3, 4, 5, 6, 7]
sayıların_kareleri = []

for sayı in sayılar:
    sayıların_kareleri.append(kare_al(sayı))
print(sayıların_kareleri)


# In[ ]:


liste = [2,3,4]

def kare_al2(sayi23):
    return sayi **2

result = map(kare_al2,liste)
print(result)


# In[ ]:


#map(function,iteration) 
sayıların_kareleri =  map(kare_al, sayılar)
print(sayıların_kareleri)
for sayı in sayıların_kareleri:
    print(sayı)


# In[ ]:


from functools import reduce

sayılar = [1, 6, 3, 7, 10, 0]
print(reduce(lambda x,y: x if x > y else y, sayılar))


# In[ ]:


def beşten_uzun(kelime):
    if len(kelime) > 5:
        return True
    else:
        return False
isimler = ['Oğuz', 'Ahmet', 'Necati', 'Ali', 'Mehmet', 'Ziya']
uzun_isimler = filter(beşten_uzun, isimler)
print(uzun_isimler)
for isim in uzun_isimler:
    print(isim)


# In[ ]:


sayılar = [0, 1, 2, 3, 4, 5]
isimler = ['Oğuz', 'Ahmet', 'Necati', 'Ali', 'Mehmet', 'Ziya']


for i, j in zip(sayılar, isimler):
    print(i,j)


# ### Assert anahtar kelimesi ( Assert keyword )

# In[ ]:


yaş = input("Yaşınız:")
assert int(yaş) >= 0, "Yaşınız negatif olamaz"


# ### Üreteçler (Generators)

# In[ ]:


def generator():
    i = 1
    print('Öncelikle bu basıldı')
    yield i

    i += 1
    print('Sonra bu')
    yield i

for eleman in generator():
    print("For döngüsü içinde:", eleman)


# In[ ]:


a = 5

def outer():
    a = 3
    def inner():
        nonlocal a
        a += 5
        print("inner fonksiyon:", a)
    print("outer fonksiyon:", a)
    return inner()

outer()
inner()
print("global:", a)


# ### Decorators

# In[1]:


#especially It is used for Flask and Django Framework
from datetime import datetime

def show_time(func):
    def wrapper(name):
        print("Time:", datetime.now().time())
        func(name)
    return wrapper

@show_time
def say_hi(name="John"):
    print("Hi {}!".format(name))

say_hi("Dogukan")


# In[ ]:


import time 
def calculate_time(func):
    def wrapper(numbers):
        start = time.time()
        end = time.time()
        result = func(numbers)
        print(func.__name__ + " " + str(end - start) + "HAHA")
        return result
    return wrapper

@calculate_time
def kare_al_wrapper(numbers):
    result = []
    for i in numbers:
        result.append(i ** 2)
    return result

@calculate_time
def kup_al_wrapper(numbers):
    result = []
    for i in numbers:
        result.append(i ** 3)
    return result

print(kare_al_wrapper(range(100)))
print(kup_al_wrapper(range(100)))


# # Numpy
# 
# 
# 
# * Basic library used in scientific calculations
# 
# * Linear algebra, machine learning, data science
# 
# * Multi-dimensional arrays
# 
# * Fast access to multidimensional arrays
# 
# * The difference from the lists is having a fixed size.

# ![Scalar Vector Matrix Tensor](https://res.cloudinary.com/practicaldev/image/fetch/s--oTgfo1EL--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://raw.githubusercontent.com/adhiraiyan/DeepLearningWithTF2.0/master/notebooks/figures/fig0201a.png)

# In[ ]:


import numpy as np


# In[ ]:


a = np.array([10, 20, 30, 40, 50, 60])
print(type(a))
print(a.shape)


# In[ ]:


liste= [1,2,3,4,5]
liste[3]


# In[ ]:


print(a[3])


# In[ ]:


type(a[3])


# In[ ]:


a[2] *= 2
print(a[2])


# In[ ]:


a


# In[ ]:


x = np.array([1,2,3])
y = x
z = np.copy(x)
z


# In[ ]:


x[0] = 10
x[0] == y[0]
x[0] == z[0]
z


# In[ ]:


b = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(b)
print(b.shape)
print(b.dtype)
print(type(b))


# In[ ]:


a = np.array([10, 20, 30, 40, 50, 180])
np.sin(a)


# In[ ]:


np.cos(a)


# In[ ]:


np.log(a)


# In[ ]:


#Calculate the exponential of all elements in the input array
np.exp(a)


# In[ ]:


c = np.array([10, 20, 100, 40, 10, 60])
c


# In[ ]:


np.max(c)


# In[ ]:


np.min(c)


# In[ ]:


#found the index of maximum element
np.argmax(c)


# In[ ]:


np.mean(c)


# In[ ]:


np.median(c)


# In[ ]:


#standard deviation
np.std(c)


# In[ ]:


b


# In[ ]:


# axis=1 => Row
# axis=0 => Column
np.sum(b, axis = 0)


# In[ ]:


zeros = np.zeros((3, 3))
print(zeros)


# In[ ]:


ones = np.ones((3, 3))
print(ones)


# In[ ]:


full = np.full((3, 3), 5)
print(full)


# In[ ]:


#Identity matrix n*n
eye = np.eye(5)
print(eye)


# In[ ]:


arange = np.arange(7)
print(arange)

arange = np.arange(0, 10)
print(arange)

arange = np.arange(0, 10, 2)
print(arange)


# In[ ]:


# Create randint
random = np.random.random((3, 3))
print(random)


# In[ ]:


arr = np.random.randint(20, size=(5, 5))
print(arr)


# In[ ]:


zeros*6


# In[ ]:


arr


# In[ ]:


arr[3,2]


# In[ ]:


arr[0:3, ::]
#arr[satır, sütun]


# In[ ]:


arr[0:3, :2]


# In[ ]:


arr[arr > 10]


# In[ ]:


np.where(arr > 10)


# In[ ]:


np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]).reshape(2,6).shape


# In[ ]:


#inverse in lineer algebra
c = np.random.randint(10, size=(3, 3))
print(c)
c_inv = np.linalg.inv(c)
print(c_inv)


# ## İç Çarpım (Dot product)
# ![Dot product](https://algebra1course.files.wordpress.com/2013/02/slide10.jpg)
# 
# credit: https://algebra1course.files.wordpress.com/

# In[ ]:


a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(a.shape)


# In[ ]:


b = np.array([
    [7, 8, 9],
    [10, 11, 12]
])
print(a.shape)


# In[ ]:


axb = np.dot(a, b)


# In[ ]:


# Transpose
(b.T).shape


# In[ ]:


axb = np.dot(a, b.T)
print(axb)
print(axb.shape)


# #### Doğukan Kaan Bozkurt
