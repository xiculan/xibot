#!/usr/bin/python
# _*_ coding: utf-8 _*_

#_______IMPORTAR LIBRERIAS_____

import RPi.GPIO as GPIO
import time

#_______CONFIGURAR GPIO'S______

GPIO.setmode(GPIO.BOARD)   #Numeración en modo BOARD
GPIO.setup(11,GPIO.OUT)    #Pin 11 como salida
servo = GPIO.PWM(11,50)    #Pin 11 en modo PWM a 50 Hz

servo.start(0.1)
time.sleep(0.5)
servo.ChangeDutyCycle((1.41 * 100)/20)       #Posicionamos el servo en 90º
input("____pulse enter para empezar____")


try:
    while True:
              grados = float(input("Introduzca un valor en grados entre 0 y 180: "))
              if grados >= 0 and grados <= 90:
                  nms = grados * 0.0101 + 0.5
                  dc = (nms * 100)/20
                  servo.ChangeDutyCycle(dc)
                  print(dc)
              elif grados >90 and grados <= 180:
                  nms = grados * 0.0104 + 0.5
                  dc = (nms * 100)/20
                  servo.ChangeDutyCycle(dc)
              else:
                  print("El valor introducido no se encuentra entre 0 y 180 subnormal")
 

except KeyboardInterrupt: #Si el usuario presiona "control + c";
    servo.stop() #paramos 
except:
    print("Error inesperado")
    servo.stop()
finally:
    GPIO.cleanup()
