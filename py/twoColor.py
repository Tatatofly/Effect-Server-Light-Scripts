#!/usr/bin/python
# -*- coding: utf-8 -*-

# Instanssi tapahtuman tehostepalvelimelle tehty scripti joka vaihtaa valoja kahden värin välillä matomaisesti.
# lapCount arvolla määritetään kierrosten lukumäärä jonka jälkeen jätetään aina yksi valo enemmän ensimmäisen värin arvoon.
#
# Versio: 1 [2018]
# Tekijä: Tatu Toikkanen
# 
# Ohje:
# Määritä serverin IP-osoite ja portti
# Aseta valojen ja kierrosten lukumäärä
# Aseta molempien värien RGB arvot
# 
# Esimerkissä valoja on 24 ja valot vaihtuvat sinisen ja punaisen välillä 10 kierrosta.

import socket
import time

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverIP = '192.168.69.10'		# Valopalvelimen IP
serverPort = 9909				# Valopalvelimen portti

lightCount = 24					# Valojen määrä
lapCount = 10					# Kierrosten määrä

colR1 = 0						# Ekan värin R arvo
colG1 = 0						# Ekan värin G arvo
colB1 = 255						# Ekan värin B arvo

colR2 = 255						# Toisen värin R arvo
colG2 = 0						# Toisen värin G arvo
colB2 = 0						# Toisen värin B arvo

# Näihin ei tarvitse koskea
lightCount2 = lightCount - 2
lapCount2 = lapCount + 1

i = 0
x = 0
y = 0
z = 1

while(i < lightCount):

	packet = bytearray([
		1, # Speksin versio aina yksi

		1, # Tehosteen tyyppi on yksi eli valo
		i, # Valon indeksi, alkaa nollasta
		0, # Valon tyyppi on nolla eli RGB
		colR1, # R
		colG1, # G
		colB1, # B
	])

	udp_socket.sendto(packet, (serverIP, serverPort))
	time.sleep(.10)
	i+=1
	
	packet = bytearray([
		1, # Speksin versio aina yksi
		
		1, # Tehosteen tyyppi on yksi eli valo
		i, # Valon indeksi, alkaa nollasta
		0, # Valon tyyppi on nolla eli RGB
		colR2, # R
		colG2, # G
		colB2, # B
	])
	
	udp_socket.sendto(packet, (serverIP, serverPort))
	time.sleep(.10)
	i+=1
	
	if(y < lapCount2 and i > lightCount2):
		if(z > 0):
			i = 1
			z = 0
		else:
			i = 0
			z = 1
		y+=1

	if(x < lightCount and i > lightCount2):
		i = x
		x+=1
udp_socket.close()
