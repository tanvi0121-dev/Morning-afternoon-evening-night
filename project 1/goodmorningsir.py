#Create a python program capable of greeting you with good morning, good afternoon an goodevenning.
# your program should use time module to get the current hour 

import time 

hour = time.localtime().tm_hour

if 5 <= hour < 8 :
    print("Good Morning")

elif 13 <= hour < 15 :
    print("Good Afternoon")

elif 15 <= hour < 21 :
    print("Good evening ")

else :
    print("Good night")