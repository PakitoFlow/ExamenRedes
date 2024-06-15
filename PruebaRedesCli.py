#1) Realizar un programa socket server y un socker client de coneccion basica, que solo envie un string en forma bidireccional, ingresado por teclado
#2) El programa servidor debe tener una lista o diccionario con nombres de usuario y contraseña. Cuando el cliente envie /login/contraseña, el server lo debera corroborar en el diccionario, e imprimir y enviar bienvenido "nombre de usuario" o conexion rechazada y cierra el socket

import socket as s
import threading as t
import sys
import os

# Aca creo el sistema para inciar sesion :3
option = False
selection = 0
while option == False:   
    print("1 Inicio Sesion")
    print("2 Crear Usuario")
    selection = input("Ingrese Numero ")
# Aca defino los casos
    if selection == "1" or selection == "2":
        option = True
        break
# Aca defino que pasa si no se cumpklen los casos prpuestos
    else:
        option = False
        os.system('cls')
        print("Ingrese 1 o 2 por favor")

# Defino al puerto q see enviara el emnsaje
cliente = s.socket(s.AF_INET, s.SOCK_STREAM)
cliente.connect(('127.0.0.1', 64777))

# Lo que pasa si se cumple el caso 1
if selection == "1":
    os.system('cls')
    print("Inicie su sesion")
    cliente.send(selection.encode('ascii'))
    username = input("Nombre de usuario: ")
    cliente.send(username.encode('ascii'))
    password = input("Contraseña: ")
    cliente.send(password.encode('ascii'))
    os.system('cls')
# El caso 2
if selection == "2":
    os.system('cls')
    print("Cree su cuenta")
    cliente.send(selection.encode('ascii'))
    username = input(" Nombre Usuario ")
    cliente.send(username.encode('ascii'))
    password = input("Contraseña ")
    cliente.send(password.encode('ascii'))
    os.system('cls')
    
# para recibir un mensaje del servi
def recibir_msg():
    while True:
        try:
            message = cliente.recv(1024).decode('ascii')
            if message == 'pep':
                cliente.send(username.encode('ascii'))
            else:
                print(message)
        except:
            
            print("Error de Conexion")
            cliente.close()
            break
# mandar mensaje al servi :v     
def enviar_msg():
    while True:
        mensaje = '{}: {}'.format(username, input(''))
        cliente.send(mensaje.encode('ascii'))

receive_thread = t.Thread(target=recibir_msg)
receive_thread.start()

write_thread = t.Thread(target=enviar_msg)
write_thread.start()
