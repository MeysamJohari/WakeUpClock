import winsound
import time
def wakeup():
    for i in range(5):
        for j in range(2):
            winsound.Beep(400,200)
        time.sleep(1)    
    
wakeup()
    
