import numpy
import pyautogui
import cv2
import time
import keyboard
from time import gmtime, strftime
from datetime import datetime
import random
import win32gui


    
#tags    
flag = False
netzwurf = False
balken1 = None
abbruchcount = 0
countnetz = 0
countfish = 0




#rüstung kaputt
def armorred():
    print ("rüstung")
    
    
    if pyautogui.locateOnScreen('redarmor4.png', confidence=0.9, region=(1400, 60, 196, 105)) is not None or pyautogui.locateOnScreen('graufisch.png', confidence=0.93, region=(770, 971, 67, 63)) is not None:
            
        print("rüstung kaputt")
        time.sleep(random.uniform(2, 4))
        pyautogui.keyDown('7')
        time.sleep( random.uniform( 0.05, 0.1 ))
        pyautogui.keyUp('7')
        time.sleep( random.uniform(1.0, 1.5)) 
        print("nicht gehabt", abbruchcount)
        print("fischfang", countfish)
        print("fisch netz", countnetz)
        print("wie lange laeufts", td_mins)
        exit()
        



if __name__ == "__main__":

    

    print(strftime("%H:%M:%S", gmtime()), "starting a bot")
    print("wait 10sec")
    time.sleep(3)
    

    #Zeitunterschied dingens
    fmt = '%Y-%m-%d %H:%M:%S'
    dt = datetime.now().isoformat(' ', 'seconds')
    tstamp1 = datetime.strptime(dt, fmt)

    
    while keyboard.is_pressed('q') == False:


        #rüstung checker
        armorred()
        
        
        # zeitdingens
        dt2 = datetime.now().isoformat(' ', 'seconds')
        tstamp2 = datetime.strptime(dt2, fmt)
        td = tstamp2 - tstamp1
        td_mins = int(round(td.total_seconds() / 60))
        

        
        # netzwurf wenn fähigkeit da
        netzf = pyautogui.locateOnScreen('netzfaehigkeitr.png', confidence=0.99, region=(833, 1006, 76,69))
        
        # schwimmer rausgenommen
        if netzf is not None and flag == False  and netzwurf == False:
            print("netz werfen")
            netzwurf = True
            pyautogui.keyDown('f')
            time.sleep( random.uniform( 0.05, 0.1 ))
            pyautogui.keyUp('f')
        else:
            print ("netzwurf", netzwurf)
            print ("netzwurfddddd", netzwurf)

        
        if (netzwurf == True):
            yb=0
            yp=0
            yp1=0
            count=0
            range = random.uniform( 12, 17 ) 
            
            # warten bis oranger balken zusehen ist
            while True:
                balken1 = pyautogui.locateOnScreen('balkengelb.png', confidence=0.9, region=(491, 109, 33, 451))
               
                if balken1 is not None:
                    
                    xb, yb, cb, zb = balken1
                    print("sehe orange balken", balken1)
                    break
                    
                count += 1
                if count > 1000:
                    count = 0
                    netzwurf = False
                    break
        
            # pfeil verfolgen und lertaste drücken wenn er im orangen bereich ist
            while True:
        
                pfeil = pyautogui.locateOnScreen('pfeil.png', confidence=0.5, region=(515, 140, 37, 377))
                if pfeil is not None:
                    yp1= yp
                    xp, yp = pyautogui.center(pfeil)
                    if yp1==yp:
                        count+=1
                    else:
                        count=0
                    print("sehe pfeil", xp,yp)
                            
                else:
                    print("sehe kein pfeil")
                    yp = 0
            

                if yb+range < yp and count < 1:
                
                    print("leertaste")
                    #zulangsam
                    # pyautogui.keyDown('space')
                    # time.sleep( random.uniform( 0.01, 0.05 )) # vorher (0.05, 0.1)
                    # pyautogui.keyUp('space')
            
                    pyautogui.press('space')

        
                # abbruch, wenn kein balken zusehen ist oder taste "L" gedrück ist
                balkenn = pyautogui.locateOnScreen('balkenorange.png', confidence=0.9, region=(491, 109, 33, 451))
                if balkenn is None:
                    print("beende netz")

                    countnetz += 1
                    print("nicht gehabt", abbruchcount)
                    print("fischfang", countfish)
                    print("fisch netz", countnetz)
                    print("wie lange laeufts", td_mins)
                    #after 19min and finished net, it stopped
                    if td_mins >= 19 :
                        print("fertig. min:", td_mins)
                        time.sleep(random.uniform(12, 18))
                        pyautogui.keyDown('7')
                        time.sleep( random.uniform( 0.05, 0.1 ))
                        pyautogui.keyUp('7')
                        time.sleep( random.uniform(1.0, 1.5)) 
                        exit()
                        
                    

                    time.sleep(random.uniform(6, 8))
                    netzwurf = False
                    break
            
                if keyboard.is_pressed('l') == True:
                    
                    netzwurf = False
                    break
           

        #  timeout for failed detection case.
        
        timeout = random.uniform( 12, 16 ) 
        print("Running1")
        print(abbruchcount)



        #rüstung checker
        armorred()
        
        if flag == False:
            print(strftime("%H:%M:%S", gmtime()), "throwing a fishing rod [1]")
            pyautogui.keyDown('e')
            time.sleep( random.uniform( 0.05, 0.1 ))
            pyautogui.keyUp('e')
            #starting time
            timeout_start = time.time()
            flag = True
            checker=0
            time.sleep( random.uniform(2.5, 4.5))        
         

        while(flag == True):
            
      
            if checker < 3:
            #rüstung checker
                armorred()
                checker += 1

            
            print("angeln")
            ausrufe = pyautogui.locateOnScreen('template4.png', confidence=0.8, region=(943, 455, 40, 70))
            keinfisch = pyautogui.locateOnScreen('fischaktiv.png', confidence=0.7, region=(764, 964, 82, 75))
            
               
            if ausrufe is not None:
            
            #if pyautogui.locateOnScreen('template2.png', confidence=0.7, region=(943, 455, 40, 70)) !=None:
                countfish += 1
                print(strftime("%H:%M:%S", gmtime()), "Time to fish!")
                time.sleep(random.uniform(0.2, 0.6))
                pyautogui.keyDown('e')
                time.sleep( random.uniform( 0.05, 0.1 ))
                pyautogui.keyUp('e')
                flag = False
                time.sleep(random.uniform(6.0, 7.0))
                # time.sleep(random.uniform(7.0, 8.5))
                
                
            #abbruch falls nichts gefunden wird 

               
            elif keinfisch is  None:
                print ("abbruch")
                abbruchcount += 1
                time.sleep(random.uniform(0.2, 1.0))
                pyautogui.keyDown('e')
                time.sleep( random.uniform( 0.05, 0.1 ))
                pyautogui.keyUp('e')
                flag = False
                time.sleep(random.uniform(6.0, 7.5))


        print(strftime("%H:%M:%S", gmtime()), "Not time yet!")
        

            