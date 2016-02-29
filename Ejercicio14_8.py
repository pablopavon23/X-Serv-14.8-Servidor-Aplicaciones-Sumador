#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import random

class WebApp:

    def parse(self,solicitud):
        return None

    def process(self,parsedRequest):
        return ("200 OK","<html><body><h1>It works!</h1></body></html>")

    def _init_(self,hostname,port):


    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    mySocket.bind((hostname, port))

    # Queue a maximum of 5 TCP connection requests

    mySocket.listen(5)

    # Accept connections, read incoming data, and answer back an HTML page
    #  (in an infinite loop)

    sumandos = 0 #si no lo inicializo no entra al if
    try:
        while True:
            print 'Waiting for connections'
            (recvSocket, address) = mySocket.accept()
            print 'Request received:'
            solicitud = recvSocket.recv(2048)
            try:
                (parsedRequest,sumandos) = self.parse(solicitud,sumandos)
            except ValueError:
                continue
            (returnCode,htmlAnswer) = self.process(parsedRequest)
            print 'Answering back...'
            recvSocket.send("HTTP/1.1" + returnCode + "\r\n\r\n" +
                            htmlAnswer + "\r\n")
            recvSocket.close()
    except KeyboardInterrupt:
    	print "Closing binded socket"
    	mySocket.close()


class SumaSimple(WebApp):

    def parse(self,solicitud,sumando):
        numero = int(respuesta.split()[1][1:])
            if (sumandos == 0):
                sumandos = numero;
                resultado = "Dame otro numero, por favor";
            else:
                suma = numero + sumandos;
                resultado = "El resultado de la suma es:" + str(numero) + "+" + str(sumandos) + "=" + str(suma);
                sumandos = 0;
            return(resultado,sumandos)

    def process(self,parsedRequest):
        resultadofinal = "<html><body><h1>" + parsedRequest + "</h1></body></html>" + "\r\n"
        return("200 OK",resultadofinal)

if _name_ == "_main_":
    pruebaWebApp = SumaSimple('localhost',1234)
