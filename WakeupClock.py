import winsound
import time
t = int(input("Enter the time in seconds: "))
while t > 0:
    min , sec = divmod(t,60)
    timer = str(min) + ":" + str(sec)
    print(timer, end="\r ")
    time.sleep(1)
    t -= 1

def wakeup():
    for i in range(5):
        for j in range(2):
            winsound.Beep(400,200)
        time.sleep(1)    

wakeup()
    
