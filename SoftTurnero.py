#En cmd se ejecuta con los siguientes comandos
#py -3.1 "C:\Users\juanz\Google Drive\Semestre 6\Laboratorio Electronica Digital\ProyectoTurnero\SoftTurnero.py"

import sys
import time
import serial
import pygame
import Clases
from pygame.locals import *
pygame.init()

SizeDisplay = [1000, 600]
Blanco = [255,255,255]
Rojo = [255,0,0]
Azul = [0,0,255]
Negro = [0,0,0]

pantalla = pygame.display.set_mode(SizeDisplay, RESIZABLE)
pantalla.fill(Blanco)

#--------------------------------------------------------------------------

class ClasePantallaPrincipal():
	def __init__(self, pantalla):
		self.Historial = []
		self.pantalla = pantalla
		self.pantalla.fill(Blanco)
		#-------------------------------------------------------------------
		self.Mensaje1 = pygame.font.Font(None, 60)
		self.TextoMensaje1 = self.Mensaje1.render("Por favor espere su turno", True, Negro, Blanco)
		self.RectTextoMensaje1 = self.TextoMensaje1.get_rect()
		self.RectTextoMensaje1.centerx = pantalla.get_rect().centerx
		self.RectTextoMensaje1.y = 5
		self.pantalla.blit(self.TextoMensaje1, self.RectTextoMensaje1)
		#-------------------- Turno Principal -------------------------------
		self.TurnoPrincipal = pygame.font.Font(None, 90)
		self.TextoTurnoPrincipal = self.TurnoPrincipal.render("Turno : ", True, Negro, Blanco)
		self.RectTextoTurnoPrincipal = self.TextoTurnoPrincipal.get_rect()
		self.RectTextoTurnoPrincipal.x = 65
		self.RectTextoTurnoPrincipal.y = 130
		self.pantalla.blit(self.TextoTurnoPrincipal, self.RectTextoTurnoPrincipal)
		#-------------------- Numero Turno Principal ------------------------
		self.NumeroTurnoPrincipal = pygame.font.Font(None, 250)
		self.stringTextoNumeroTurnoPrincipal = "00"
		self.TextoNumeroTurnoPrincipal = self.NumeroTurnoPrincipal.render(self.stringTextoNumeroTurnoPrincipal, True, Rojo, Blanco)
		self.RectTextoNumeroTurnoPrincipal = self.TextoNumeroTurnoPrincipal.get_rect()
		self.RectTextoNumeroTurnoPrincipal.x = 310
		self.RectTextoNumeroTurnoPrincipal.y = 85
		self.pantalla.blit(self.TextoNumeroTurnoPrincipal, self.RectTextoNumeroTurnoPrincipal)
		#-------------------- Numero Mesa Principal -------------------------
		self.MesaPrincipal = pygame.font.Font(None, 50)
		self.stringTextoMesaPrincipal = "en la mesa numero 0"
		self.TextoMesaPrincipal = self.MesaPrincipal.render(self.stringTextoMesaPrincipal, True, Negro, Blanco)
		self.RectTextoMesaPrincipal = self.TextoMesaPrincipal.get_rect()
		self.RectTextoMesaPrincipal.x = 550
		self.RectTextoMesaPrincipal.y = 145
		self.pantalla.blit(self.TextoMesaPrincipal, self.RectTextoMesaPrincipal)
		#-------------------- Fuente Turno ----------------------------------
		self.Turno = pygame.font.Font(None, 45)
		#-------------------- Fuente Numero Turno ---------------------------
		self.NumeroTurno = pygame.font.Font(None, 125)
		#-------------------- Fuente Numero Mesa ----------------------------
		self.Mesa = pygame.font.Font(None, 30)
		#-------------------- Turno 1 ---------------------------------------
		self.TextoTurno1 = self.Turno.render("Turno : ", True, Negro, Blanco)
		self.RectTextoTurno1 = self.TextoTurno1.get_rect()
		self.RectTextoTurno1.x = 240
		self.RectTextoTurno1.y = 305
		self.pantalla.blit(self.TextoTurno1, self.RectTextoTurno1)
		#-------------------- Numero Turno 1 --------------------------------
		self.stringTextoNumeroTurno1 = "00"
		self.TextoNumeroTurno1 = self.NumeroTurno.render(self.stringTextoNumeroTurno1, True, Rojo, Blanco)
		self.RectTextoNumeroTurno1 = self.TextoNumeroTurno1.get_rect()
		self.RectTextoNumeroTurno1.x = 360
		self.RectTextoNumeroTurno1.y = 280
		self.pantalla.blit(self.TextoNumeroTurno1, self.RectTextoNumeroTurno1)
		#-------------------- Numero Mesa 1 ---------------------------------
		self.stringTextoMesa1 = "en la mesa numero 0"
		self.TextoMesa1 = self.Mesa.render(self.stringTextoMesa1, True, Negro, Blanco)
		self.RectTextoMesa1 = self.TextoMesa1.get_rect()
		self.RectTextoMesa1.x = 480
		self.RectTextoMesa1.y = 310
		self.pantalla.blit(self.TextoMesa1, self.RectTextoMesa1)
		#-------------------- Turno 2 ---------------------------------------
		self.TextoTurno2 = self.Turno.render("Turno : ", True, Negro, Blanco)
		self.RectTextoTurno2 = self.TextoTurno2.get_rect()
		self.RectTextoTurno2.x = 240
		self.RectTextoTurno2.y = 405
		self.pantalla.blit(self.TextoTurno2, self.RectTextoTurno2)
		#-------------------- Numero Turno 2 --------------------------------
		self.stringTextoNumeroTurno2 = "00"
		self.TextoNumeroTurno2 = self.NumeroTurno.render(self.stringTextoNumeroTurno2, True, Rojo, Blanco)
		self.RectTextoNumeroTurno2 = self.TextoNumeroTurno2.get_rect()
		self.RectTextoNumeroTurno2.x = 360
		self.RectTextoNumeroTurno2.y = 380
		self.pantalla.blit(self.TextoNumeroTurno2, self.RectTextoNumeroTurno2)
		#-------------------- Numero Mesa 2 ---------------------------------
		self.stringTextoMesa2 = "en la mesa numero 0"
		self.TextoMesa2 = self.Mesa.render(self.stringTextoMesa2, True, Negro, Blanco)
		self.RectTextoMesa2 = self.TextoMesa2.get_rect()
		self.RectTextoMesa2.x = 480
		self.RectTextoMesa2.y = 410
		self.pantalla.blit(self.TextoMesa2, self.RectTextoMesa2)
		#-------------------- Turno 3 ---------------------------------------
		self.TextoTurno3 = self.Turno.render("Turno : ", True, Negro, Blanco)
		self.RectTextoTurno3 = self.TextoTurno3.get_rect()
		self.RectTextoTurno3.x = 240
		self.RectTextoTurno3.y = 505
		self.pantalla.blit(self.TextoTurno3, self.RectTextoTurno3)
		#-------------------- Numero Turno 3 --------------------------------
		self.stringTextoNumeroTurno3 = "00"
		self.TextoNumeroTurno3 = self.NumeroTurno.render(self.stringTextoNumeroTurno3, True, Rojo, Blanco)
		self.RectTextoNumeroTurno3 = self.TextoNumeroTurno3.get_rect()
		self.RectTextoNumeroTurno3.x = 360
		self.RectTextoNumeroTurno3.y = 480
		self.pantalla.blit(self.TextoNumeroTurno3, self.RectTextoNumeroTurno3)
		#-------------------- Numero Mesa 3 ---------------------------------
		self.stringTextoMesa3 = "en la mesa numero 0"
		self.TextoMesa3 = self.Mesa.render(self.stringTextoMesa3, True, Negro, Blanco)
		self.RectTextoMesa3 = self.TextoMesa3.get_rect()
		self.RectTextoMesa3.x = 480
		self.RectTextoMesa3.y = 510
		self.pantalla.blit(self.TextoMesa3, self.RectTextoMesa3)
		pygame.display.flip()

	def update(self):
		self.pantalla.blit(self.TextoMensaje1, self.RectTextoMensaje1)
		#-------------------- Turno Principal -------------------------------
		self.pantalla.blit(self.TextoTurnoPrincipal, self.RectTextoTurnoPrincipal)
		#-------------------- Numero Turno Principal ------------------------
		self.TextoNumeroTurnoPrincipal = self.NumeroTurnoPrincipal.render(self.stringTextoNumeroTurnoPrincipal, True, Rojo, Blanco)
		self.pantalla.blit(self.TextoNumeroTurnoPrincipal, self.RectTextoNumeroTurnoPrincipal)
		#-------------------- Numero Mesa Principal -------------------------
		self.TextoMesaPrincipal = self.MesaPrincipal.render(self.stringTextoMesaPrincipal, True, Negro, Blanco)
		self.pantalla.blit(self.TextoMesaPrincipal, self.RectTextoMesaPrincipal)
		#-------------------- Turno 1 ---------------------------------------
		self.pantalla.blit(self.TextoTurno1, self.RectTextoTurno1)
		#-------------------- Numero Turno 1 --------------------------------
		self.TextoNumeroTurno1 = self.NumeroTurno.render(self.stringTextoNumeroTurno1, True, Rojo, Blanco)
		self.pantalla.blit(self.TextoNumeroTurno1, self.RectTextoNumeroTurno1)
		#-------------------- Numero Mesa 1 ---------------------------------
		self.TextoMesa1 = self.Mesa.render(self.stringTextoMesa1, True, Negro, Blanco)
		self.pantalla.blit(self.TextoMesa1, self.RectTextoMesa1)
		#-------------------- Turno 2 ---------------------------------------
		self.pantalla.blit(self.TextoTurno2, self.RectTextoTurno2)
		#-------------------- Numero Turno 2 --------------------------------
		self.TextoNumeroTurno2 = self.NumeroTurno.render(self.stringTextoNumeroTurno2, True, Rojo, Blanco)
		self.pantalla.blit(self.TextoNumeroTurno2, self.RectTextoNumeroTurno2)
		#-------------------- Numero Mesa 2 ---------------------------------
		self.TextoMesa2 = self.Mesa.render(self.stringTextoMesa2, True, Negro, Blanco)
		self.pantalla.blit(self.TextoMesa2, self.RectTextoMesa2)
		#-------------------- Turno 3 ---------------------------------------
		self.pantalla.blit(self.TextoTurno3, self.RectTextoTurno3)
		#-------------------- Numero Turno 3 --------------------------------
		self.TextoNumeroTurno3 = self.NumeroTurno.render(self.stringTextoNumeroTurno3, True, Rojo, Blanco)
		self.pantalla.blit(self.TextoNumeroTurno3, self.RectTextoNumeroTurno3)
		#-------------------- Numero Mesa 3 ---------------------------------
		self.TextoMesa3 = self.Mesa.render(self.stringTextoMesa3, True, Negro, Blanco)
		self.pantalla.blit(self.TextoMesa3, self.RectTextoMesa3)
		pygame.display.flip()

	def anadir(self,Turno,Mesa):
		self.Historial.append([Turno,Mesa])
		self.stringTextoMesa3 = self.stringTextoMesa2
		self.stringTextoNumeroTurno3 = self.stringTextoNumeroTurno2
		self.stringTextoMesa2 = self.stringTextoMesa1
		self.stringTextoNumeroTurno2 = self.stringTextoNumeroTurno1
		self.stringTextoMesa1 = self.stringTextoMesaPrincipal
		self.stringTextoNumeroTurno1 = self.stringTextoNumeroTurnoPrincipal
		self.stringTextoMesaPrincipal = "en la mesa numero "+str(Mesa)
		if Turno < 10:
			self.stringTextoNumeroTurnoPrincipal = "0"+str(Turno)
		else:
			self.stringTextoNumeroTurnoPrincipal = str(Clases.ValueTo100(Turno))
		self.update()

	def remover(self,Turno):
		for i in self.Historial:
			if i[0] == Turno:
				pos = self.Historial.index(i)
				if pos >= len(self.Historial) - 4:
					temp = len(self.Historial)-pos
					if(temp == 1):
						self.stringTextoMesaPrincipal = self.stringTextoMesa1
						self.stringTextoNumeroTurnoPrincipal = self.stringTextoNumeroTurno1
						self.stringTextoMesa1 = self.stringTextoMesa2
						self.stringTextoNumeroTurno1 = self.stringTextoNumeroTurno2
						self.stringTextoMesa2 = self.stringTextoMesa3
						self.stringTextoNumeroTurno2 = self.stringTextoNumeroTurno3
						if len(self.Historial) > 4:
							self.stringTextoMesa3 = "en la mesa numero "+str(self.Historial[-5][1])
							TurnoTemp = self.Historial[-5][0]
							if TurnoTemp < 10:
								self.stringTextoNumeroTurno3 = "0"+str(self.Historial[-5][0])
							else:
								self.stringTextoNumeroTurno3 = str(Clases.ValueTo100(self.Historial[-5][0]))
						else:
							self.stringTextoMesa3 = "en la mesa numero 0"
							self.stringTextoNumeroTurno3 = "00"
					self.Historial.remove(i)
				else:
					self.Historial.remove(i)
		self.update()

if __name__ == '__main__':
	TurnosDisponibles = Clases.ClassTurnosDisponibles()
	COM2 = Clases.ComunicacionGeneradorTurnos("COM4")
	COM1 = Clases.Comunicacion("COM6","1")
	COM3 = Clases.Comunicacion("COM5","2")
	COM4 = Clases.Comunicacion("COM7","3")

	PantallaPrincipal = ClasePantallaPrincipal(pantalla)

	while True:
		pantalla.fill(Blanco)
		PantallaPrincipal.update()
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				sys.exit()
			if event.type == KEYDOWN and event.key == K_n:
				TurnosDisponibles.LimiteTurnos += 1
				print("Se añadio el turnos numero = %d" % TurnosDisponibles.LimiteTurnos)
				#COM2.EntroDato(dato)

		if COM1.COM.inWaiting() > 0:
			datoCOM1 = COM1.COM.read()
			COM1.EntroDato(datoCOM1, TurnosDisponibles, PantallaPrincipal)

		if COM2.COM.inWaiting() > 0:
			datoCOM2 = COM2.COM.read()
			#print("llego el dato " + str(datoCOM2) + " en COM2")
			COM2.EntroDato(datoCOM2,TurnosDisponibles)

		if COM3.COM.inWaiting() > 0:
			datoCOM3 = COM3.COM.read()
			COM3.EntroDato(datoCOM3, TurnosDisponibles, PantallaPrincipal)

		if COM4.COM.inWaiting() > 0:
			datoCOM4 = COM4.COM.read()
			COM4.EntroDato(datoCOM4, TurnosDisponibles, PantallaPrincipal)