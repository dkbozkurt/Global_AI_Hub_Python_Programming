#!/usr/bin/env python
# coding: utf-8

# # Modules

# In[2]:


#Guessing game

import random as rnd

secret = rnd.randint(1,100) #.randint(a,b) fonksyonu a ve b arasındaki tüm sayıları alıp arasından random bir sayı seçiyor.

check=False

#guess = int(input("Guess a number : "))

for x in range(5):
    guess = int(input("Guess a number from 0 to 100: "))
    if guess==secret:
        print("Congratulations !")
        check = True
        break
    elif guess < secret:
        print("Enter a greater value than your guess : ")
    else:
        print("Enter a smaller value than your guess : ")
        
if not check:    # if not check - eğer check false ise demek.
    print("You could not find, the determined number is:",secret)


# # Dictionary (Sözlükler)

# -Python'daki bir veri tipidir.
# 
# -Sözlükler,anahtarlar(keys) tarafından indexlenir ve bu anahtarlar string ve sayı tipinde olabilir.
# 
# -key:value şeklinde yazılır ve keyler benzersiz değerlerdir.
# 
# -{}

# In[3]:


d={}

print(d)


# In[4]:


d={"python":1,"course":2}
print(d)


# In[34]:


d2={"machine":"learning","artificial":"intelligence"}
print(d2)


# In[8]:


d2["artificial"]


# In[9]:


d["course"]


# In[35]:


d2["deep"]="learning" #Yeni bir key:value çifti olusturuyor.
print(d2)


# In[12]:


print(d.keys())


# In[13]:


d2.values()


# In[14]:


d2.items()


# In[15]:


for k in d2.keys():
    print(k)


# In[16]:


for v in d.values():
    print(v)


# In[17]:


for k,v in d2.items():
    print(k,v)


# In[19]:


for k,v in d.items():
    if v==2:
        print(k)


# In[18]:


d


# In[20]:


d["a"]=[3,4,5]
d


# In[21]:


d.pop("python") #.pop(x) x i ve valuesini d dicten çıkarır.
print(d)


# In[23]:


len(d)


# In[24]:


"a" in d


# In[25]:


"python" in d


# In[26]:


d2


# In[27]:


d2.get("artificial") #.get(x) key i x olan dictionarynin valuesini verir.


# In[36]:


del d2["deep"]  # del dictionary["x"] key i deep olan key:valueyi siler.
d2


# In[41]:


d4={"insan":2,"kedi":4,"örümcek":8}        #***************

for i in d4:
    ayak=d4[i]
    print("%s canlısının %d adet ayağı bulunur." %(i,ayak)) #%s string %d int belirtir. #Birinci tip
    print(str(i) + " canlısının " + str(ayak) + " adet ayağı bulunur.") #İkinci tip.


# In[43]:


d4={"insan":2,"kedi":4,"örümcek":8}

for i,ayak in d4.items():
    print(str(i) + " canlısının " + str(ayak) + " adet ayağı bulunur.")


# In[44]:


ilceler = {"İstanbul":["Bostancı","Beşiktaş","Kadıköy"],
           "Ankara":["Çankaya","Gölbaşı","Kızılcahamam"],
           "İzmir":["Çeşme","Bornova","Foça"]}


# In[45]:


ilceler["İstanbul"]


# In[46]:


type(ilceler)


# In[48]:


type(ilceler["Ankara"])


# In[49]:


ilceler["İzmir"][0]


# # Sets ( Kümeler )

# -Bir küme, listelerden farklı olarak, belli bir sırası bulunmayan bir veri topluluğudur;elemanlarına indexleme ile erişilemez.
# 
# -Tıpkı matematiksel kümeler gibi, aynı elemandan birden fazla barındıramaz.
# 
# -Kümeler içerisine bir öğe ancak bir defa eklenebilir. Yani bir küme iki aynı elemana sahip olamaz.
# 
# -Boş küme oluşturmak için set() fonk. kullanıyoruz.

# In[50]:


s={"python",5,6,7,8,5,6,"abc","python"}
print(s)


# In[51]:


bos=set()
type(bos)


# In[52]:


bos2={}
type(bos2)


# In[53]:


s2= set(["python",5,6,8,5,6,"abc","python"])
print(s2)
type(s2)


# In[54]:


an= set("ananas")
print(an)


# In[60]:


an= set(["ananas"])
print(an)


# In[55]:


y= {"a","b",[1,2,3],5,6} # içinde list int ve string var b yüzden küme olusturulamıyor. listeyi bu şekilde koyamıyoruz.
print(y)


# In[57]:


s2


# In[58]:


6 in s2


# In[61]:


9 in s2


# In[62]:


len(s2)


# In[64]:


s2.add("ai") #.add(x) bir değeri daha sets e ekler
print(s2)


# In[65]:


s2.add("ai") 
print(s2)
len(s2)


# In[66]:


s2.remove("ai")
print(s2)


# In[70]:


from math import sqrt

#import math

print([sqrt(x) for x in list(range(10))])


# # Tuples (Demetler)

# Sıralı veri yapısıdır, listeler gibi index değerine sahiptir.Tümveri tiplerini içerisinde barındırabilir.
# 
# Listelerden farklı olarak,değiştirilemeyen bir yapıları vardır.Elimizde birden fazla değiştirilemez değerimiz var ise, bunları bir demet içinde toplayabiliriz.

# In[68]:


demet=(1,2,3,4,5)
print(demet)
print(type(demet))


# In[69]:


demet2=()
type(demet2)


# In[71]:


print(demet[3])


# In[72]:


print(demet[-2])


# In[73]:


print(demet[:4])


# In[74]:


dm3=("dogukan",5,8,"temmuz")
dm3.index("temmuz")


# In[75]:


dm3.count(5) #.count() 


# In[76]:


dm4=("elma","armut","çilek")
dm4[0]="kiraz" #Değiştirilemiyor buradaki gibi.


# In[77]:


dm4.remove("armut") #.remove(x) #Tuplelarda .remove kullanılamaz.

