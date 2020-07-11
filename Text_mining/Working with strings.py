#!/usr/bin/env python
# coding: utf-8

# ## Tweet text handling
# For the given text file whch contains a smaple tweet, 
# output
# Every word separately 
# Every sentence separately
# Every hastag
# Every call out (@CMO) but not standalone @ sign
# Every word with first letter capital
# Number of unique words in the file (#tags and @ excluded)

# In[1]:


import re


# ####  The Tweet

# In[2]:


f = open('C:/Users/Ranjeeth/Desktop/Tw_text.txt', 'r')
tweet = f.read()
print(tweet)


# #### Capitalized words

# In[3]:


print(set([e for e in tweet.split() if e.istitle()]))


# #### Seperate sentences

# In[4]:


t = tweet.splitlines()
for i in range(len(t)):
    print(t[i])


# #### Words seperated

# In[5]:


#q = [e for e in tweet.split() if e.isalnum()]
q = [r for r in tweet.split() if not re.search('[#, @]', r)]
print(q)


# #### Call-outs

# In[6]:


print([r for r in tweet.split() if re.search('@\w+', r)])


# #### Hashtags

# In[7]:


print([w for w in tweet.split() if w.startswith('#')])


# #### Unique words

# In[8]:


print(set([s.lower() for s in q]))


# In[ ]:




