import time
import threading

def brush_up(name):
    time.sleep(8)
    print(f"Wake Up and brush up{name}")
def go_out():
    time.sleep(2)
    print("Go out !!!")
def complete_assign():
    time.sleep(3)
    print("Complete the Assignment")


chore1=threading.Thread(target=brush_up,args=("Parth",))
chore1.start()
chore2=threading.Thread(target=go_out)
chore2.start()
chore3=threading.Thread(target=complete_assign)
chore3.start()
print("Complete all the chores")
chore1.join()
chore2.join()
chore3.join()
