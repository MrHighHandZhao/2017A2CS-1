"""
S3C2 Harry Xue Alarm System
"""
import threading
def Active():
    while 1 == 1:
        print("Intruder Detected!!!!!!!!\n")
while 1 == 1:
    print("Start\n"+"System Inactive")
    SystemStatus = False
    
    ButtonPressed1 = int(input("Input 1 for button pressed, 2 for not pressed.\n"))
    if ButtonPressed1 == 1:
          print("System Active")
          SystemStatus = True
    else:
          print("")
          Pin = int(input("Enter the correct pin to deactivite system. Input 1 for correct pin, 2 for other cases.\n"))
          if  Pin == 1:
                print("System Inactive")
                SystemStatus = False
                break
          else:
                print("System Active")
                print("Sensor Activated")

              
                Pin2=int(input("Enter the correct pin. Input 1 for correct pin, 2 for other cases.\n"))
                if Pin2 == 1:
                    print("System Inactive")
                    SystemStatus = False
                    break
                else:
                    SystemStatus = True
                    print("System Active\n"+"After 2 mins, the bell will ring")
                    timer = threading.Timer(120,Active())
                    timer.start()
                    Pin3 = int(input("Enter the correct pin. Input 1 for correct pin, 2 for other cases.\n"))
                    if Pin3 == 1:
                        print("SystemInactive")
                        SystemStatus = False
                    else:
                        SystemStatus = True
                        BellRings = True
                
         

        
