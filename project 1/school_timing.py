import time
hour = time.localtime().tm_hour

if 6 <= hour < 8 :
    print("Get read for school")

elif 8 <= hour < 14 :
    print("You are in school")

elif 14 <= hour < 17 :
    print("Do your Homework")

elif 17 <= hour < 21 :
    print("play and relax")

else :
    print("Sleep")