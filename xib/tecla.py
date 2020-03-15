#!/bin/python
#t6ecla.py -funciona 2/2/2020
#t7ecla.py
#Real non-blocking console input
#If your program must be console based, you have to switch your terminal
# out of line mode into character mode, and remember to restore it before 
#your program quits. There is no portable way to do this across operating systems.
#
#Python non-blocking console input on Linux
#The tty module has an interface to set the terminal
# to character mode, the termios module allows you to save and 
#restore the console setup, and the select module lets you 
#know if there is any input available.

#problemes t5ecla.py:
#quan apretem la tecla continuament, perdem el control perque el buffer
#queda ple i fins que no acaba de escriure no para de incrementar
#els valors
#******** diario ***********
#enero 2020
#por hacer : calcular el fwd i el turn para enviarselo a los servos
#crear funcion e saber.py que se llame drive, i que envie el fwd i el turn
#--------------------------------
#para enviar los valores al bot, tenemos que oprimir la tecla f
#y queremos que se ponga automaticamente
#-------------------------------------
#implementar un demonio que lea un buffer automaticamente y lo mande
#al bot (gpio)
#*************************************************
#https://rico-schmidt.name/pymotw-3/select/index.html
import sys,os
import select
import tty,time
import termios
import saber

def calc_fwd(forward):
  
  return fwd

#claulamos el valor de turn a partir de los valores de lefti i right
def calc_turn(left,right):
  return turn

#function that stops all the paremeters of the bot
def stoping_bot():
  saber.send_fwd(0)    #movemos
  saber.send_turn(0,0)

def isData():
#  return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
  return select.select([sys.stdin], [], [], 0.5) == ([sys.stdin], [], [])

old_settings = termios.tcgetattr(sys.stdin)
try:
  pause=0.1
  tty.setcbreak(sys.stdin.fileno())
  i = 0
  right=0
  left=0
  forward=0
  speed=0
  last_speed=0

  max_right=100
  max_left=100
  max_speed=100

  acc=0   #accelerating flag: 0.deaccelerating 1.maintain speed 2.accelerating
  #keys definition
  front_key='o'
  right_key='p'
  left_key='i'
  stop_key='l'
  accelerate_key='t'
 

  while 1:
    os.system('clear')
    print('********** bot control ***************')

    print i
    i += 1
    print ('max values: '+str(max_speed))
    print ('control keys: i-left  o-front  p-right  t-accelerate  l-stop')
    print ('movement: left->' + str(left) + '  forward->' + str(speed)  + '  right->' + str(right))
#    print('max_front=' + str(max_front))
    if isData():
      c = sys.stdin.read(1)
      if c == '\x1b':         # x1b is ESC
        break

      elif c == front_key:
#        speed=last_speed
        acc=1

      elif c == accelerate_key:
        acc=2
        if speed < max_speed:
          speed=speed+10
          print('accelerating')

      elif c == left_key:
        #print(
        right=0
        left=left+10
#        forward=fo+5

      elif c == right_key:
#         saber.hola()

        left=0
        right=right+10
#        forward=forward+5

      elif c == stop_key:  #stop_key: l
        print('stop robot')
        speed=0
        left=0
        right=0
      elif c== 'f':
        saber.send_fwd(speed)    #movemos
        saber.send_turn(left,right)

      elif c == 'q':
        print('Exiting program')
        stoping_bot()
        break

    if speed > 0:
#      last_speed=speed
      if acc == 0:
        print('decreassing speed')
        speed=speed-5
      acc=0     #restart acc variable

    if right > 0:
      right=right-5

    if left > 0:
      left=left-5

    #altura del while, aqui enviem la senyal pwm

    time.sleep(pause)

finally:
  termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
