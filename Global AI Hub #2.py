#!/usr/bin/env python
# coding: utf-8

# # Logical Operations

# In[1]:


t,f = True, False
print(type(t))


# In[2]:


print(t or f)


# In[3]:


print(t and f)


# In[4]:


print(not t)


# In[6]:


print(t !=f)


# In[9]:


print(1 != 1)


# In[8]:


print(t==f)


# # Printing Strins 

# In[14]:


hello = "Hello"
world = "World"


# In[20]:


print(world,",",len(world)) # buradaki gibi farklı tipler arasına , getirilerek aynı printte basılabilir.


# In[21]:


#s is used as a placeholder for string values you want to inject into a formatted string.
#%d is used as a placeholder for numeric or decimal values

"""
The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size limit), together with a format string,
with a format string, which contains normal text together with "argument specifiers " ,
special symbols like "%s" and "%d".

"""


# In[22]:


world2= "%s %d" % (world, len(world))


# In[24]:


print(world2)


# In[26]:


print(world+" "+str(len(world))) #aralarına boşluktan olusan bir string de koyduk.


# In[27]:


print(hello[0])


# In[29]:


print(hello[1])


# In[28]:


print(hello[-1])


# In[30]:


print(world[-1])


# In[32]:


print(world[-3]) # w 0 dan baslıyım geriye dogru sayıyoruz.


# In[34]:


hello[2:4]


# In[35]:


world[1:4]


# In[36]:


print(world[3:5])


# In[39]:


print(world[3:]) # sayı yazılmazsa belirtilen sayıdan baslayıp sonuna kadar yazar.


# In[41]:


hello[:4] # ikinci yazılana kadar olanı verir (ikinci sayı dahil olmaz)


# In[42]:


hello[:]


# In[43]:


hello[::-1] # TERS ÇEVİRMEK İÇİN.


# In[44]:


world[:-3]


# In[45]:


hello[2:len(world)]


# In[48]:


world[2:4:1]


# In[50]:


world[1::2] #: : :n --- n adım sayısı.


# In[51]:


city = "istanbul"
city[0:6:2]


# In[52]:


"t" in city


# In[56]:


"y" in city


# In[53]:


"anb" in city


# In[54]:


"snl" in city


# In[57]:


n=10  #integeri stringe çevirme
print(n)
str(n)


# In[58]:


s="13" #Stringi integar a çevirme
s
int(s)


# In[60]:


m=8
print(float(m))
m


# In[61]:


ai= "artifical" + " " + "intelligence"
print(ai)


# In[63]:


ai


# In[64]:


word = "machine learning"
print(word.capitalize())  #capitalize harfi capital yapar.


# In[65]:


print(word.upper())


# In[67]:


print(word.replace("machine","artificial")) # machine stringini bul artificial ile değiştir demek replace().


# In[68]:


word


# In[69]:


word2="            artificial general       intelligence"


# In[70]:


word2


# In[71]:


print(word2.strip()) #delete spaces in the beginning and end


# In[72]:


y= input("Please enter a city name :") #input takes string as a parameter


# In[73]:


print(y)


# In[79]:


type(y)


# In[74]:


x=int(input("Please enter an integer: "))
print(x)


# In[75]:


month =12
day=365


# In[77]:


print("A year consist of ",month, "months and ",day,"days.")


# In[86]:


print("A year consists of "+ str(month) + " months and "+ str(day)+ "days.") 
#stringler veya tipler arasına , veya + ile ayırma yapılmalıdır


# # Lists 

# In[80]:


"""
A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
Each element or value that is inside of a list is called an item. Just as strings are defined as characters
between quotes, lists are defined by having values between square brackers [ ].
"""


# In[134]:


mylist=[3,5,6,7] #creating lists


# In[105]:


print(mylist)


# In[84]:


print(mylist[2])


# In[85]:


print(mylist[-1])


# In[87]:


print(mylist[-3])


# In[106]:


mylist[2] = "python" # lists can contain different data types
print(mylist)


# In[107]:


mylist.append("course") #we can add items to the end of list .append()
print(mylist)


# In[108]:


mylist.append("course")
mylist.append("course")
print(mylist)


# In[109]:


thelast= mylist.pop() #pop() gets rid of the last element of the list
#önce elemenı çıkarıp daha sonra thelastın içine koyar.
print(thelast)


# In[110]:


print(mylist)


# In[111]:


mylist.index("python") #.index() fonks. belirtinen obj lokasyonunu bildirir.


# In[112]:


mylist.index("course")


# In[113]:


mylist.count("course") #.count() belirtinen objeden kaç tane oldugunu döndürür.


# In[114]:


mylist.remove("course")
print(mylist)


# In[115]:


l=[1,6,3]
l.sort() #.sort() küçükten büyüğe sıralar HEPSİ STRİNG YA DA HEPSİ İNT OLMALI.
l


# In[116]:


mylist.remove("course")
mylist.remove("python")
print(mylist)


# In[135]:


mylist.reverse()
mylist


# In[136]:


mylist2= ["course","hello","python"]
mylist2.sort()
mylist2


# In[137]:


mylist


# In[138]:


mylist3=[1,11,111,1111]
mylist.extend(mylist3)
mylist


# In[139]:


mylist4=[1,11,111,1111]
mylist.append(mylist4)
print(mylist)


# In[140]:


mylist.insert(5,55)
print(mylist)


# In[127]:


numbers=list(range(8))
print(numbers)


# In[141]:


number2 = list(range(2,14,3))
print(number2)


# In[142]:


print(number2[2:5])


# In[131]:


number2[5:8]=[10,11,12] #5 6 7 yi belirtilen elemanlarla değiştirdik.
numbers


# In[132]:


12 in numbers


# In[133]:


15 in numbers


# In[143]:


[1,2,3] + [4,5]


# In[144]:


[1,2,3 ]*3


# In[146]:


list1=[[1,2],3,[4,5,6]] 
list1[2][1] # 2. elamanının 1. elemanını bastır.


# # If/Else Conditions

# In[148]:


course = "python"
s= input ("Please enter a letter: ")
if s in course:
    print("Exists!")
else:
    print("Not exist")


# In[149]:


course = "python"
s= input ("Please enter a letter: ")
if s in course:
    print("Exists!")
else:   
    print("Not exist")


# In[150]:


course = "python"
s= input ("Please enter a letter: ")
if s not in course: #not in !=
    print("Not exist")    
else:   
    print("Exists!")


# In[ ]:




