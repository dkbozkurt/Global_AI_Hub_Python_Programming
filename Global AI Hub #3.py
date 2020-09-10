#!/usr/bin/env python
# coding: utf-8

# # If/Else Statement

# In[3]:


num= int(input("Enter a number: "))
if num<0:
    num*= -1 #num=num*-1

print("Result is : ",num)


# In[5]:


course = "python"
s= input("Please select a key : ")
if s in course:
    print("Available!")
else:
    print("Not available")


# #### If-Elif-Else

# else if olayı

# In[8]:


score= int(input("Please enter an exam score: "))

if score <35:
    print("FF")
elif score <=60:
    print("CC")
elif score <=90:
    print("AA")
else:
    print("Unvalid score")


# In[10]:


x=5

if x>4:
    x+=1
elif x>5:
    x+=2
elif x>7:
    x+=3
    
print("X's value is, ",x)


# In[11]:


x=5

if x>4:
    x+=1
if x>5:
    x+=2
if x>7:
    x+=3
    
print("X's value is, ",x)


# #### Soru
# 
# 

# Bir şirkette, çalışanların maaşları aşağıdaki formül kullanılarak hesaplanarak aşamalı olarak artırılır:
# 
# maaş = maaş + maaş x (artış yüzdesi)
# 
# Artışlar, işçinin mevcut maaşına göre aşağıda belirtildiği gibi önceden tanımlanmıştır. Örneğin işçinin cari maaşı 1000 TL veya daha az ise maaşı% 15 artırılır.
# 
# Aralık	Yüzdesi
# 0 < maaş ≤ 1000	15%
# 1000 < maaş ≤ 2000	10%
# 2000 < maaş ≤ 3000	5%
# 3000 < maaş	2.5%
# 
# Kullanıcıdan maaşını girmesini isteyen bir program yazın. Ardından programınız, kullanıcının artan maaşını hesaplamalı ve yazdırmalıdır.
# 
# Örnek Çıktılar:
# 
# Lütfen mevcut maaşınızı girin: 1000
# 
# Yeni maaşınız 1150.0.
# 
# Lütfen mevcut maaşınızı girin: 2500
# 
# Yeni maaşınız 2625.0.

# In[5]:


maas =float(input("Please enter your salary value: "))

if maas <0 :
    print("Unvalid salary value.")
else:
    
    if 0 < maas <=1000:
        maas=maas+maas*0.15
    elif maas <=2000:
        maas=maas+maas*0.1
    elif maas <=3000:
        maas=maas+maas*0.05
    else:
        maas=maas+maas*0.025
        
    print("Your expected salary would be ...", maas)


# # While

# In[18]:


sayi=0

while sayi <9 :
    print("Number's value is ",sayi)
    sayi+=1


# In[25]:


sayi2=0

while sayi2 !=20 :
    print("Number's value is ",sayi2)
    sayi2+=2


# In[21]:


sayi3= int(input("Please select a number from 1 to 10: "))

while sayi3 < 1 or sayi3 > 10:
    print("You selected an unvalid value.")
    sayi3= int(input("Please select a number from 1 to 10: "))
print("Congratulations! You choosed,",sayi3)


# In[22]:


t= [1,2,3,4,5,6]

i=0
while(i<len(t)):
    #i+=1
    print(i,". element is ",t[i])
    i+=1


# In[26]:


while True:
    a=input("Enter a value: ")
    if a=="Exit":
        break


# # For 

# In[27]:


for i in [2,45,57]:
    print(i)


# In[29]:


for i in range(5):
    print(i)


# In[32]:


for i in "Python Course":
    print(i)


# In[31]:


for i in "Python Course".split(): #split() boşluk görene kadar girder boşluk görünce ayırır.
    print(i)


# In[33]:


for i in range(10):
    if i ==5:
        break
    print(i)


# In[34]:


for i in range(10):
    if i ==5:
        continue #5 i atlayıp devam eder.
    print(i)


# In[35]:


numbers=list(range(8))

squares= []

for i in numbers:
    squares.append(i**2)
print(squares)


# In[46]:


numbers=list(range(8))

squares= [i**2 for i in numbers]
print(squares)


# In[38]:


numbers=list(range(8))

even_squares= [i**2
         for i in numbers
         if i % 2 ==0]

odd_cube= [i**3
         for i in numbers
         if i % 2 ==1]
print(even_squares)
print(odd_cube)


# In[39]:


mylist=[3,5,12,7,65,35]

sum=0
for i in mylist:
    sum=sum+i #sum+=i
print(sum)


# ### Greatest number in a list

# In[45]:


mylist=[3,5,12,7,65,35]
max=mylist[0]

for i in mylist:
    if i > max:
        max=i
print(max)


# ### Sum of lists

# In[6]:


list1= [1,2,3]
list2=[4,5,6]

list3=[a + b for a,b in zip(list1,list2)] 
#zip(a,b) iki liste üzerinden aynı anda gidilmek istenirse kullanılır.

print(list3)


# #### Soru#1

# Kullanıcıdan bir tamsayı değeri(stop_number) giren ve 0'dan stop_number'a kadar tüm sayıların toplamını yazdıran bir program yazın.

# #### Cevap 

# In[10]:


stop_number=int(input("Please select a stop value : "))
i=0
sum=0

while i<stop_number:
        sum=sum+i
        i+=1
print("Sum of the numbers is ",sum)


# #### Soru#2

# Programınızı, toplanacak sayıların başlangıç değerlerini de (star_number) girecek şekilde genişletin.Bu durumda programınız start_number dan stop_number a olan sayıları toplayacak.

# #### Cevap

# In[9]:


start_number=int(input("Please select a start value :"))
    
stop_number=int(input("Please select a stop value : "))

i=start_number
sum=0

while i<stop_number:
        sum=sum+i
        i+=1
        
print("Sum of the numbers is ",sum)


# #### Soru#3

# Programınızı, start_number ı 0 ile 100 arasında bir tamsayı olup olmadığını kontrol edecek şekilde genişletin. Eğer öyleyse, programınız ikinci girdiyi sormaya ve hesaplamaları yapmaya devam edecektir; aksi takdirde, bir hata yazdırır ve yürütmeyi durdurur.

# #### Cevap

# In[7]:


start_number=float(input("Please enter an integer from 0 to 100 :"))
while start_number>100 or 0>start_number:
    print("Please select a valid value ! ")
    start_number=int(input("Please select a start value :"))
    
stop_number=int(input("Please select a stop value : "))
while stop_number<=0:
    print("Please select a valid value ! ")
    stop_number=int(input("Please select a stop value : "))

i=start_number
sum=0

while i<stop_number:
        sum=sum+i
        i+=1
        
print("Sum of the numbers is ",sum)

