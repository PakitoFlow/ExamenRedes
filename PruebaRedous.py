#1) Realizar un programa socket server y un socker client de coneccion basica, que solo envie un string en forma bidireccional, ingresado por teclado
#2) El programa servidor debe tener una lista o diccionario con nombres de usuario y contraseña. Cuando el cliente envie /login/contraseña, el server lo debera corroborar en el diccionario, e imprimir y enviar bienvenido "nombre de usuario" o conexion rechazada y cierra el socket
#   En el arranque el servidor tiene q decir "el servidor esta escuchando en el puerto X"
import socket as s
import threading as t
import sys
import os
import time


cliente = []
usuarios = []
# Defino el puerto 
server = ("127.0.0.1", 64777)

socket = s.socket(s.AF_INET, s.SOCK_STREAM)


print("El servidor esta listo para recibir peticiones")

def findCommand(s):
    if s[0] == "/":  
        cmd = s.split()[0].lstrip("/")
        msg = s.split(cmd , 1)[1].lstrip()
        if cmd == "servermsg":
            servermsg(msg)
        if cmd == "whisper":
            destinatary = msg.split()[0].lstrip()
            content = msg.split(destinatary, 1)[1].lstrip()
            whisper(destinatary, content)
    else:
        return (msg)

def handle(client):
    while True: 
        try:
            message = client.recv(1024)
            findCommand(message)
        except:
            index = cliente.index(client)
            cliente.remove(client)
            client.close()
            username = usuarios[index]
            broadcast('{} se ha desconectado'.format(username).encode('ascii'))
            usuarios.remove(username)
            break

        def broadcast(msg):
            for client in cliente:
                client.send(msg)

def servermsg(msg):
    print("(SERVER-DM) Mensaje a servidor: {} ", format((msg)))

def whisper(destinatary, msg):
    c_index = usuarios.index(destinatary)
    c = cliente[c_index]
    c.send(msg)

