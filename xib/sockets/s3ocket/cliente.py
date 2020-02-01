#!/usr/bin/env python

#http://developeando.net/sockets-python/

#importamos el modulo para trabajar con sockets
import socket,sys


def envia_valor(ip_servidor,puerto,valor):
#  print('aixo es una proba')
#  sys.exit(0)

  s1 = socket.socket()
  s1.connect((ip_servidor,puerto))
  i=0
  while i < 3:
    s1.send(valor)
    i=i+1
  
  print('enviamos orden de close al servidor')
  s1.send('close')
  print('paramos programa cliente')
  s1.close()




def say_hello():
  print('hello folks')

def main():

  print('aixo es una proba')
  sys.exit(0)

  #Creamos un objeto socket para el servidor. Podemos dejarlo sin parametros pero si 
  #quieren pueden pasarlos de la manera server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s = socket.socket()

  #Nos conectamos al servidor con el metodo connect. Tiene dos parametros
  #El primero es la IP del servidor y el segundo el puerto de conexion
  s.connect(("localhost", 9999))

  #Creamos un bucle para retener la conexion
  while True:
    #Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
    op = raw_input("Que quieres hacer? (1.Iniciar_servidor 2.Parar servidor 3.enviar mensaje servidor close.cerrar programa")
    if op==str(3):
      mensaje = raw_input("Mensaje a enviar >> ")

      #Con la instancia del objeto servidor (s) y el metodo send, enviamos el mensaje introducido
      s.send(mensaje)

    #Si por alguna razon el mensaje es close cerramos la conexion
    if op == "close":
      break


  #Imprimimos la palabra Adios para cuando se cierre la conexion
  print "Adios."

  #Cerramos la instancia del objeto servidor
  s.close()


if __name__ == "__main__":
    main()
