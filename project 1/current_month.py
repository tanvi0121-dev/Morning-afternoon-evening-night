import time 
month = time.localtime().tm_mon

if 1 <= month < 3 :
    print("beginging of the year")

elif 4 <= month < 6 :
    print("Mid Year is coming")

elif 7 <= month < 9 :
    print("Second half of the year")

else :
    print ("Year ending soon")