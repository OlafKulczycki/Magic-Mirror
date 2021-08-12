#Imports
import RPi.GPIO as GPIO
import time
import subprocess

#GPIOs mit GPIO-Nummer ansprechen Modus
GPIO.setmode(GPIO.BCM)
#Variablen
SHUTOFF_DELAY = 300#Sekunden
PIR_Sensor = 4

#Methoden
def main():
    GPIO.setup(PIR_Sensor, GPIO.IN) #Input definieren
    turned_off = False
    last_motion_time = time.time()

    while True:
        if GPIO.input(PIR_Sensor):
            last_motion_time = time.time()
            print("Bewegung erkannt")
            print("Monitor wird eingeschaltet.")
            time.sleep(1)
            turned_off = False
            turn_on() 
                
        else:
           if not turned_off and time.time() > (last_motion_time + SHUTOFF_DELAY):
                print("Monitor wird ausgeschaltet.")
                turned_off = True
                turn_off()
        time.sleep(1)
        
def turn_on():
    subprocess.call("/home/pi/Desktop/MonitorPir/monitor_on.sh", shell=True)
    
def turn_off():
    pass
    #subprocess.call("/home/pi/Desktop/MonitorPir/monitor_off.sh", shell=True)
            
#Main starten
if __name__ == '__main__':
    try:
        print("Programm wird gestartet.") 
        main()
            
    #Programm beenden mit STRG + c
    except KeyboardInterrupt:
        turn_on()
        print("Programm wird beendet.")
        GPIO.cleanup()
