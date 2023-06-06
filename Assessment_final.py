#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Q1)Write a program that takes a string as input, and counts the frequency of each word in the string, there might
be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
highest-frequency word."""
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    max_value,max_key=max(counts.values()),max(counts,key=counts.get)
    print("freq of each word in string \n",counts)
    print("length of High occurance string")
    return len(max_key)


# In[2]:


word_count("Hi Hi Hi baby baby where are your your dddddd dddddd dddddd dddddd are not here")


# In[19]:


word_count("write write write all the number number number number number from from from from 1 to 100")


# In[10]:


"""Q2:Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
he can remove just one character at the index in the string, and the remaining characters will occur the same
number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO"""
a=str(input("Enter string which needs to validate: "))
check=0
for i in a:
    if a.count(i)==1:
        check=check+0
    else:
        check=check+1
if check>1:
          print("string not valid")
else:
        print("string valid")
        


# In[9]:


"""Q3.Write a program, which would download the data from the provided link, and then read the data and convert
that into properly structured data and return it in Excel format."""


# In[14]:


a=pd.read_json("https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json")
df1=pd.DataFrame(a.pokemon.values.tolist())
df1.to_excel(r"C:/Users/surya/Neeraj/python/Assesment/pokemandata.xlsx",index=False)
#In read and write operation of Json and from Dataframe to excel you need to provide your own path


# In[ ]:




