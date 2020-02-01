#http://developeando.net/sockets-python/
#!/usr/bin/env python

#importamos el modulo para trabajar con sockets
import socket,sys
import cliente

cliente.say_hello()



cliente.envia_valor('localhost',4444,'jellou')
