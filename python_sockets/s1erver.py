import socket

mi_socket = socket.socket()
mi_socket.bind(('localhost',8000))  
mi_socket.listen(5) #cantidad peticiones en cola

print "servidor iniciado"

while True:
  conexion, addr = mi_socket.accept()  #aceptamos las peticiones, retorna dos valores
  print "Nueva conexion establecida!"
  print addr

  peticion = conexion.recv(1024)
  print peticion

  conexion.send("hola, te saludo desde el servidor!")




conexion.close()  #cerramos la conexion
