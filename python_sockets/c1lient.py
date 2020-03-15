import socket
import time

mi_socket = socket.socket()   #creamos un nuevo objeto socket
mi_socket.connect(('localhost',8000))  #le pasamos una tupla con la direccion i el puerto


while True:
  mi_socket.send("hola desde el cliente!")

  respuesta = mi_socket.recv(1024)  #buffer de 1024 bytes

#  valor = input("enter value:")
#  print valor
#  mi_socket.send("hello")
  time.sleep(0.5)

  print respuesta

mi_socket.close()
