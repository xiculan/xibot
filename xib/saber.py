#s2aber.py ..
from curtsies import Input
import sys,os,time
import RPi.GPIO as GPIO
from time import sleep

#I connected the servo motor to pin 11 (BCM GPIO17) on the Raspberry Pi.
fwd_pin=11
turn_pin=12

#configuracion *************************************
#set gpio modes
GPIO.setmode(GPIO.BOARD)
GPIO.setup(fwd_pin, GPIO.OUT)
GPIO.setup(turn_pin, GPIO.OUT)


def hola():
  print('hola')

def saber(turn,fwd):
  print('turn: '+turn+'  fwd: '+fwd)



#*********
#funcion parea pasar de grados a duty_cible

def calcula_dc(grados):
  while True:
    if grados >= 0 and grados <= 90:
       nms = grados * 0.0101 + 0.5
       dc = (nms * 100)/20
    elif grados >90 and grados <= 180:
       nms = grados * 0.0104 + 0.5
       dc = (nms * 100)/20

    return dc

#*****************

def move_servo(pin,value,start_value):
      pwm=GPIO.PWM(pin, 50)
      pwm.start(start_value)
#    max_percent=100
#    min_percent=0
#    if min_percent<=percent<=max_percent:
#      print('funcion change_pwm_value - pin: '+str(pin)+'  value: '+str(value)+'  dc: '+str(dc))
#      dc=calcula_dc(value)
      GPIO.output(pin, True)
      pwm.ChangeDutyCycle(value)
      sleep(1)
      GPIO.output(pin, False)
      pwm.ChangeDutyCycle(value)
      #GPIO.cleanup()

def calcula_duty(percent):
  value=percent
  return value

#*************************************************************************
#funcion que entramos porcentaje i mueve el servo
def move_input_value():
    value=0
    duty=0
    val_anterior=2.5
    while 1:
      os.system('clear')
      print('value: '+str(value)+'  duty: '+str(duty))
      print('++++++++cheking servo+++++++++++++++')
      val_anterior=value
      value=int(input("Enter the value:"))
      pin=11
#      value=percent_to_angle(value)  #convertimos de percent a angulo
#      value=calcula_dc(value)  #convertimos de grados a dc
#      #def move_servo(pin,value,start_value):
#      move_servo(pin,value,val_anterior)
      move_servo_percent(pin,value)

#*************************************************************************
#funcion que entramos porcentaje i mueve el servo
#90 grados es parado, 0 grados es atras a tope i 180 grados es adelante a tope
#por tanto, en porcentaje: 50 es parado i 100 es adelante a tope
def send_fwd(fwd):
  print('fwd function: fwd = '+str(fwd))
  pin=11
#      value=percent_to_angle(value)  #convertimos de percent a angulo
#      value=calcula_dc(value)  #convertimos de grados a dc
#      #def move_servo(pin,value,start_value):
#      move_servo(pin,value,val_anterior)

  #convertimos para que el valor sea solo de 
  fwd=50+fwd*0.5
  move_servo_percent(pin,fwd)



#*************************************************************************

def send_turn(left,right):
  pin=12
  turn=50
  print('funcition send_turn: left= '+str(left)+'  right= '+str(right))
  if left>0:
    right=0
    turn=50-left*.5
  if right>0:
    left=0
    turn=50+right*0.5

  move_servo_percent(pin,turn)

#funcion que entramos porcentaje i mueve el servo
def move_servo_percent(pin,percent):
    duty=0
    val_anterior=2.5
    angle=percent_to_angle(percent)  #convertimos de percent a angulo
    dc=calcula_dc(angle)  #convertimos de grados a dc
    #def move_servo(pin,value,start_value):
    move_servo(pin,dc,val_anterior)


def percent_to_angle(percent):
  angle=0
  angle=percent*1.8
  return angle

def setAngle(angle):
    print('funcion setAngle')
    duty = angle / 18 + 3
    GPIO.output(fwd_pin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(fwd_pin, False)
    pwm.ChangeDutyCycle(duty)

def calcula_angle(percent):
    angle = percent /18 + 3
    return angle

def main():
  with Input(keynames='curses') as input_generator:
    for e in input_generator:
      print(repr(e))
      os.system('clear')
      print('control sabertooth:')
      if e == 'm':
        print('movemos:')
#        saber('100','60')
#        setAngle(90)
        change_pwm_value(turn_pin,90)
        change_pwm_value(fwd_pin,90)
        time.sleep(3)
        change_pwm_value(turn_pin,120)
        change_pwm_value(fwd_pin,120)

      if e == 'q':
        print('exiting')
        break

if __name__ == '__main__':
#    main()
     move_input_value()



#https://www.learnrobotics.org/blog/raspberry-pi-servo-motor/

#********************
#https://www.nociones.de/controlar-un-servo-con-rasperry-pi-usando-rpio-pwm-y-dma/
# testservo.py
#
#import time
#
#import pigpio
#
#pi = pigpio.pi() # Connect to local Pi.
#
## set gpio modes
#pi.set_mode(2, pigpio.OUTPUT)
# 
# 
## start 1500 us servo pulses on gpio2
#pi.set_servo_pulsewidth(2, 1500)
#time.sleep(1)
#for _i in range(5): #loop between -90 and 90 degrees
#pi.set_servo_pulsewidth(2,2500)
#time.sleep(1)
#pi.set_servo_pulsewidth(2,600)
#time.sleep(1)
#pi.set_servo_pulsewidth(2, 1500)
#time.sleep(1)
# 
#pi.set_servo_pulsewidth(2, 0) # stop servo pulses
# 
#pi.stop() # terminate connection and release resources
