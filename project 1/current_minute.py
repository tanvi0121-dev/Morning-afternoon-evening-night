import time
minute = time.localtime().tm_min

if 0 <= minute <= 29 :
    print ("First Half of the hour")

else :
    print ("second half of the hour")