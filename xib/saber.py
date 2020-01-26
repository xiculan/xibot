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
#GPIO.setup(fwd_pin, GPIO.OUT)
#GPIO.setup(turn_pin, GPIO.OUT)

#pwm=GPIO.PWM(fwd_pin, 50)
#pwm=GPIO.PWM(turn_pin, 50)
#pwm.start(0)


def saber(turn,fwd):
  print('turn: '+turn+'  fwd: '+fwd)
#  driver.write(turn)
#  pwm.ChangeDutyCycle(5) # left -90 deg position
#  sleep(1)
#  pwm.ChangeDutyCycle(7.5) # neutral position
#  sleep(1)
#  pwm.ChangeDutyCycle(10) # right +90 deg position
#  sleep(1)

#  pwm.stop()
#  GPIO.cleanup()

def setAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(pwd_pin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(pwd_pin, False)
    pwm.ChangeDutyCycle(duty)


def main():
  with Input(keynames='curses') as input_generator:
    for e in input_generator:
      print(repr(e))
      os.system('clear')
      print('control sabertooth:')
      if e == 'm':
        print('movemos:')
#        saber('100','60')
        setAngle('90')

      if e == 'q':
        print('exiting')
        break

if __name__ == '__main__':
    main()



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
