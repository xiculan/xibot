#!/bin/python
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

import sys,os
import select 
import tty,time
import termios


  

def isData():
  return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

old_settings = termios.tcgetattr(sys.stdin)
try:
  pause=0.1
  tty.setcbreak(sys.stdin.fileno())
  i = 0
  right=0
  left=0
  forward=0

  max_right=50
  max_left=50
  max_front=50

  #keys definition
  front_key='o'
  right_key='p'
  left_key='i'
  stop_key='l'

  while 1:
    os.system('clear')
    print('********** bot control ***************')

    print i
    i += 1
    print (max_front)
    print('movement: left->' + str(left) + '  forward->' + str(forward)  + '  right->' + str(right))
#    print('max_front=' + str(max_front))
    if isData():
      c = sys.stdin.read(1)
      if c == '\x1b':         # x1b is ESC
        break

      elif c == front_key:
        if forward < max_front:
          print('accelerating')
          forward=forward+2

      elif c == left_key:
        #print(
        right=0
        left=left+3
        forward=forward+2

      elif c == right_key:
        left=0
        right=right+3
        forward=forward+2

      elif c == stop_key:
        print('stop robot')
        forward=0
        left=0
        right=0
      elif c == 'q':
        print('Exiting program')
        break
    if forward > 0:
      print('restem move')
      forward=forward-1

    if right > 0:
      right=right-1

    if left > 0:
      left=left-1

    time.sleep(pause)

finally:
  termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)