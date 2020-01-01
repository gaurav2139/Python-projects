#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
n = random.randint(1,1000)
think_input = int(input("Enter an integer from 1 to 1000: "))
while n!= "think_input":
    print
    if think_input<n:
        print("Your guess is low")
        think_input = int(input("Enter an integer from 1 to 1000: "))
    elif think_input>n:
        print("Your guess is high")
        think_input = int(input("Enter an integer from 1 to 1000: "))
    else:
        print("You guessed it right!")
        break
    print

