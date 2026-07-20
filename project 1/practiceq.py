import time 

hour = time.localtime().tm_hour

if 5 <= hour < 8 :
    print("Wake up and exercise")

elif 8 <= hour < 12 :
    print("Study")

elif 12 <= hour < 17 :
    print("Work Hard ")

elif 17 <= hour < 22 :
    print("Relax")

else :
    print("Go to sleep")