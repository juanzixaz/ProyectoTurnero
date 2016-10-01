#En cmd se ejecuta con los siguientes comandos
#py -3.1 "C:\Users\juanz\Google Drive\Semestre 6\Laboratorio Electronica Digital\ProyectoTurnero\Clases.py"

import sys
import time
import serial
import pygame

#--------------------------------------------------------------
#---- Inicia --- ClassTurnosDisponibles -----------------------
class ClassTurnosDisponibles():
    """docstring for TurnosDisponibles
    Esta Clase va a administrar los turnos que se van a utilizar
    en el proyecto, tiene capacidad para 
    """
    ContadorTurnos = 0
    LimiteTurnos = 0
    def __init__(self):
        self.ListaTurnosDisponibles = []

    def UtilizarTurno(self):
        if len(self.ListaTurnosDisponibles) == 0:
            if self.ContadorTurnos < self.LimiteTurnos:
                self.ContadorTurnos += 1
                if str(self.ContadorTurnos)[-1] == "0":
                    if str(self.ContadorTurnos)[-2] == "0":
                        self.ContadorTurnos += 1
                return self.ContadorTurnos
            else:
                return 0
        else:
                return self.ListaTurnosDisponibles.pop(-1)
        #self.PrintEstado()

    def DevolverTurno(self, Turno):
        if Turno != 0:
            self.ListaTurnosDisponibles.append(Turno)

    def PrintEstado(self):
        print("ContadorTurnos = %d \nLimiteTurnos = %d \nListaTurnosDisponibles = %s" % (self.ContadorTurnos,self.LimiteTurnos,str(self.ListaTurnosDisponibles)))


#---- Termina --- ClassTurnosDisponibles ----------------------
#--------------------------------------------------------------

#--------------------------------------------------------------
#1 -> 1, 100 -> 1, 1000 -> 1, 10000 -> 1
def ValueTo100(valor):
    valorstr = str(valor)
    return int(valorstr[len(valorstr)-2:len(valorstr)])
#--------------------------------------------------------------

#--------------------------------------------------------------
def IntTo8Bytes(valor):
    VectorBytes = bytearray(8)
    valor_temp = valor
    Terminar = False
    if valor_temp==0 or valor_temp > 128:
        print("ERROR - El valor ingresado no es correcto " + str(valor))
    else:
        while not Terminar:
            if valor_temp == 0:
                Terminar = True
            if valor_temp < 128:
                if valor_temp < 64:
                    if valor_temp < 32:
                        if valor_temp < 16:
                            if valor_temp < 8:
                                if valor_temp < 4:
                                    if valor_temp < 2:
                                        if valor_temp == 1:
                                            VectorBytes[7] = 1
                                            valor_temp -= 1
                                        else:
                                            Terminar = True
                                    else:
                                        VectorBytes[6] = 1
                                        valor_temp -= 2
                                else:
                                    VectorBytes[5] = 1
                                    valor_temp -= 4
                            else:
                                VectorBytes[4] = 1
                                valor_temp -= 8
                        else:
                            VectorBytes[3] = 1
                            valor_temp -= 16
                    else:
                        VectorBytes[2] = 1
                        valor_temp -= 32
                else:
                    VectorBytes[1] = 1
                    valor_temp -= 64
            else:
                VectorBytes[0] = 1
                valor_temp -= 128
    return(VectorBytes)
#--------------------------------------------------------------

def IntToHexa(valor):
    if valor == 0:
            return b'\x00'
    elif valor == 0:
            return b'\x00'
    elif valor == 1:
            return b'\x01'
    elif valor == 2:
            return b'\x02'
    elif valor == 3:
            return b'\x03'
    elif valor == 4:
            return b'\x04'
    elif valor == 5:
            return b'\x05'
    elif valor == 6:
            return b'\x06'
    elif valor == 7:
            return b'\x07'
    elif valor == 8:
            return b'\x08'
    elif valor == 9:
            return b'\x09'
    elif valor == 10:
            return b'\x0A'
    elif valor == 11:
            return b'\x0B'
    elif valor == 12:
            return b'\x0C'
    elif valor == 13:
            return b'\x0D'
    elif valor == 14:
            return b'\x0E'
    elif valor == 15:
            return b'\x0F'
    elif valor == 16:
            return b'\x10'
    elif valor == 17:
            return b'\x11'
    elif valor == 18:
            return b'\x12'
    elif valor == 19:
            return b'\x13'
    elif valor == 20:
            return b'\x14'
    elif valor == 21:
            return b'\x15'
    elif valor == 22:
            return b'\x16'
    elif valor == 23:
            return b'\x17'
    elif valor == 24:
            return b'\x18'
    elif valor == 25:
            return b'\x19'
    elif valor == 26:
            return b'\x1A'
    elif valor == 27:
            return b'\x1B'
    elif valor == 28:
            return b'\x1C'
    elif valor == 29:
            return b'\x1D'
    elif valor == 30:
            return b'\x1E'
    elif valor == 31:
            return b'\x1F'
    elif valor == 32:
            return b'\x20'
    elif valor == 33:
            return b'\x21'
    elif valor == 34:
            return b'\x22'
    elif valor == 35:
            return b'\x23'
    elif valor == 36:
            return b'\x24'
    elif valor == 37:
            return b'\x25'
    elif valor == 38:
            return b'\x26'
    elif valor == 39:
            return b'\x27'
    elif valor == 40:
            return b'\x28'
    elif valor == 41:
            return b'\x29'
    elif valor == 42:
            return b'\x2A'
    elif valor == 43:
            return b'\x2B'
    elif valor == 44:
            return b'\x2C'
    elif valor == 45:
            return b'\x2D'
    elif valor == 46:
            return b'\x2E'
    elif valor == 47:
            return b'\x2F'
    elif valor == 48:
            return b'\x30'
    elif valor == 49:
            return b'\x31'
    elif valor == 50:
            return b'\x32'
    elif valor == 51:
            return b'\x33'
    elif valor == 52:
            return b'\x34'
    elif valor == 53:
            return b'\x35'
    elif valor == 54:
            return b'\x36'
    elif valor == 55:
            return b'\x37'
    elif valor == 56:
            return b'\x38'
    elif valor == 57:
            return b'\x39'
    elif valor == 58:
            return b'\x3A'
    elif valor == 59:
            return b'\x3B'
    elif valor == 60:
            return b'\x3C'
    elif valor == 61:
            return b'\x3D'
    elif valor == 62:
            return b'\x3E'
    elif valor == 63:
            return b'\x3F'
    elif valor == 64:
            return b'\x40'
    elif valor == 65:
            return b'\x41'
    elif valor == 66:
            return b'\x42'
    elif valor == 67:
            return b'\x43'
    elif valor == 68:
            return b'\x44'
    elif valor == 69:
            return b'\x45'
    elif valor == 70:
            return b'\x46'
    elif valor == 71:
            return b'\x47'
    elif valor == 72:
            return b'\x48'
    elif valor == 73:
            return b'\x49'
    elif valor == 74:
            return b'\x4A'
    elif valor == 75:
            return b'\x4B'
    elif valor == 76:
            return b'\x4C'
    elif valor == 77:
            return b'\x4D'
    elif valor == 78:
            return b'\x4E'
    elif valor == 79:
            return b'\x4F'
    elif valor == 80:
            return b'\x50'
    elif valor == 81:
            return b'\x51'
    elif valor == 82:
            return b'\x52'
    elif valor == 83:
            return b'\x53'
    elif valor == 84:
            return b'\x54'
    elif valor == 85:
            return b'\x55'
    elif valor == 86:
            return b'\x56'
    elif valor == 87:
            return b'\x57'
    elif valor == 88:
            return b'\x58'
    elif valor == 89:
            return b'\x59'
    elif valor == 90:
            return b'\x5A'
    elif valor == 91:
            return b'\x5B'
    elif valor == 92:
            return b'\x5C'
    elif valor == 93:
            return b'\x5D'
    elif valor == 94:
            return b'\x5E'
    elif valor == 95:
            return b'\x5F'
    elif valor == 96:
            return b'\x60'
    elif valor == 97:
            return b'\x61'
    elif valor == 98:
            return b'\x62'
    elif valor == 99:
            return b'\x63'
    elif valor == 100:
            return b'\x64'
    elif valor == 101:
            return b'\x65'
    elif valor == 102:
            return b'\x66'
    elif valor == 103:
            return b'\x67'
    elif valor == 104:
            return b'\x68'
    elif valor == 105:
            return b'\x69'
    elif valor == 106:
            return b'\x6A'
    elif valor == 107:
            return b'\x6B'
    elif valor == 108:
            return b'\x6C'
    elif valor == 109:
            return b'\x6D'
    elif valor == 110:
            return b'\x6E'
    elif valor == 111:
            return b'\x6F'
    elif valor == 112:
            return b'\x70'
    elif valor == 113:
            return b'\x71'
    elif valor == 114:
            return b'\x72'
    elif valor == 115:
            return b'\x73'
    elif valor == 116:
            return b'\x74'
    elif valor == 117:
            return b'\x75'
    elif valor == 118:
            return b'\x76'
    elif valor == 119:
            return b'\x77'
    elif valor == 120:
            return b'\x78'
    elif valor == 121:
            return b'\x79'
    elif valor == 122:
            return b'\x7A'
    elif valor == 123:
            return b'\x7B'
    elif valor == 124:
            return b'\x7C'
    elif valor == 125:
            return b'\x7D'
    elif valor == 126:
            return b'\x7E'
    elif valor == 127:
            return b'\x7F'
    elif valor == 128:
            return b'\x80'
    elif valor == 129:
            return b'\x81'
    elif valor == 130:
            return b'\x82'
    elif valor == 131:
            return b'\x83'
    elif valor == 132:
            return b'\x84'
    elif valor == 133:
            return b'\x85'
    elif valor == 134:
            return b'\x86'
    elif valor == 135:
            return b'\x87'
    elif valor == 136:
            return b'\x88'
    elif valor == 137:
            return b'\x89'
    elif valor == 138:
            return b'\x8A'
    elif valor == 139:
            return b'\x8B'
    elif valor == 140:
            return b'\x8C'
    elif valor == 141:
            return b'\x8D'
    elif valor == 142:
            return b'\x8E'
    elif valor == 143:
            return b'\x8F'
    elif valor == 144:
            return b'\x90'
    elif valor == 145:
            return b'\x91'
    elif valor == 146:
            return b'\x92'
    elif valor == 147:
            return b'\x93'
    elif valor == 148:
            return b'\x94'
    elif valor == 149:
            return b'\x95'
    elif valor == 150:
            return b'\x96'
    elif valor == 151:
            return b'\x97'
    elif valor == 152:
            return b'\x98'
    elif valor == 153:
            return b'\x99'
    elif valor == 154:
            return b'\x9A'
    elif valor == 155:
            return b'\x9B'
    elif valor == 156:
            return b'\x9C'
    elif valor == 157:
            return b'\x9D'
    elif valor == 158:
            return b'\x9E'
    elif valor == 159:
            return b'\x9F'
    elif valor == 160:
            return b'\xA0'
    elif valor == 161:
            return b'\xA1'
    elif valor == 162:
            return b'\xA2'
    elif valor == 163:
            return b'\xA3'
    elif valor == 164:
            return b'\xA4'
    elif valor == 165:
            return b'\xA5'
    elif valor == 166:
            return b'\xA6'
    elif valor == 167:
            return b'\xA7'
    elif valor == 168:
            return b'\xA8'
    elif valor == 169:
            return b'\xA9'
    elif valor == 170:
            return b'\xAA'
    elif valor == 171:
            return b'\xAB'
    elif valor == 172:
            return b'\xAC'
    elif valor == 173:
            return b'\xAD'
    elif valor == 174:
            return b'\xAE'
    elif valor == 175:
            return b'\xAF'
    elif valor == 176:
            return b'\xB0'
    elif valor == 177:
            return b'\xB1'
    elif valor == 178:
            return b'\xB2'
    elif valor == 179:
            return b'\xB3'
    elif valor == 180:
            return b'\xB4'
    elif valor == 181:
            return b'\xB5'
    elif valor == 182:
            return b'\xB6'
    elif valor == 183:
            return b'\xB7'
    elif valor == 184:
            return b'\xB8'
    elif valor == 185:
            return b'\xB9'
    elif valor == 186:
            return b'\xBA'
    elif valor == 187:
            return b'\xBB'
    elif valor == 188:
            return b'\xBC'
    elif valor == 189:
            return b'\xBD'
    elif valor == 190:
            return b'\xBE'
    elif valor == 191:
            return b'\xBF'
    elif valor == 192:
            return b'\xC0'
    elif valor == 193:
            return b'\xC1'
    elif valor == 194:
            return b'\xC2'
    elif valor == 195:
            return b'\xC3'
    elif valor == 196:
            return b'\xC4'
    elif valor == 197:
            return b'\xC5'
    elif valor == 198:
            return b'\xC6'
    elif valor == 199:
            return b'\xC7'
    elif valor == 200:
            return b'\xC8'
    elif valor == 201:
            return b'\xC9'
    elif valor == 202:
            return b'\xCA'
    elif valor == 203:
            return b'\xCB'
    elif valor == 204:
            return b'\xCC'
    elif valor == 205:
            return b'\xCD'
    elif valor == 206:
            return b'\xCE'
    elif valor == 207:
            return b'\xCF'
    elif valor == 208:
            return b'\xD0'
    elif valor == 209:
            return b'\xD1'
    elif valor == 210:
            return b'\xD2'
    elif valor == 211:
            return b'\xD3'
    elif valor == 212:
            return b'\xD4'
    elif valor == 213:
            return b'\xD5'
    elif valor == 214:
            return b'\xD6'
    elif valor == 215:
            return b'\xD7'
    elif valor == 216:
            return b'\xD8'
    elif valor == 217:
            return b'\xD9'
    elif valor == 218:
            return b'\xDA'
    elif valor == 219:
            return b'\xDB'
    elif valor == 220:
            return b'\xDC'
    elif valor == 221:
            return b'\xDD'
    elif valor == 222:
            return b'\xDE'
    elif valor == 223:
            return b'\xDF'
    elif valor == 224:
            return b'\xE0'
    elif valor == 225:
            return b'\xE1'
    elif valor == 226:
            return b'\xE2'
    elif valor == 227:
            return b'\xE3'
    elif valor == 228:
            return b'\xE4'
    elif valor == 229:
            return b'\xE5'
    elif valor == 230:
            return b'\xE6'
    elif valor == 231:
            return b'\xE7'
    elif valor == 232:
            return b'\xE8'
    elif valor == 233:
            return b'\xE9'
    elif valor == 234:
            return b'\xEA'
    elif valor == 235:
            return b'\xEB'
    elif valor == 236:
            return b'\xEC'
    elif valor == 237:
            return b'\xED'
    elif valor == 238:
            return b'\xEE'
    elif valor == 239:
            return b'\xEF'
    elif valor == 240:
            return b'\xF0'
    elif valor == 241:
            return b'\xF1'
    elif valor == 242:
            return b'\xF2'
    elif valor == 243:
            return b'\xF3'
    elif valor == 244:
            return b'\xF4'
    elif valor == 245:
            return b'\xF5'
    elif valor == 246:
            return b'\xF6'
    elif valor == 247:
            return b'\xF7'
    elif valor == 248:
            return b'\xF8'
    elif valor == 249:
            return b'\xF9'
    elif valor == 250:
            return b'\xFA'
    elif valor == 251:
            return b'\xFB'
    elif valor == 252:
            return b'\xFC'
    elif valor == 253:
            return b'\xFD'
    elif valor == 254:
            return b'\xFE'
    elif valor == 255:
            return b'\xFF'
    else:
            print("El numero es incorrecto")

#--------------------------------------------------------------
#---- Inicia --- Comunicacion ---------------------------------
class ComunicacionGeneradorTurnos():
    """docstring for Comunicacion
    Este Objeto crea el un puerto de comunicacion en
    el que podemos estar acceder no solo a envio y
    recepcion de turnos si no tambien a que turnos a
    manejado para poderce devolver.
    """
    def __init__(self, NombrePuerto):
        try:
            self.NombrePuerto = NombrePuerto
            self.COM = serial.Serial(
                port=NombrePuerto,
                baudrate=9600,
                timeout=1,
                parity=serial.PARITY_EVEN,
                stopbits=serial.STOPBITS_TWO,
                bytesize=serial.EIGHTBITS
                )
        except:
            print("ERROR - El puerto " + NombrePuerto + " no esta disponible")

    def siguiente(self,TurnosDisponibles):
        try:
            TurnosDisponibles.LimiteTurnos += 1
            print("Se añado un Nuevo turno, Turno #"+str(TurnosDisponibles.LimiteTurnos))
            #TurnosDisponibles.PrintEstado()
            byte = IntToHexa(ValueTo100(TurnosDisponibles.LimiteTurnos))
            self.COM.write(byte)
        except:
            print("ERROR (%s) - Al añadir un Turno al Turnero" % self.NombrePuerto)

    def EntroDato(self,Dato,TurnosDisponibles):
        if Dato == b'\x01':
            self.siguiente(TurnosDisponibles)
        else:
            print("ERROR - El dato "+str(Dato)+" enviado por "+self.NombrePuerto+" es incorrecto (ComunicacionGeneradorTurnos)")

#---- Termina --- ListaDeCorrimiento --------------------------
#--------------------------------------------------------------

#--------------------------------------------------------------
#---- Inicia --- Comunicacion ---------------------------------
class Comunicacion():
    """docstring for Comunicacion
    Este Objeto crea el un puerto de comunicacion en
    el que podemos estar acceder no solo a envio y
    recepcion de turnos si no tambien a que turnos a
    manejado para poderce devolver.
    """
    def __init__(self, NombrePuerto, NumeroMesa):
        try:
            self.ListaTurnosAlmacenados = []
            self.NombrePuerto = NombrePuerto
            self.NumeroMesa = str(NumeroMesa)
            self.COM = serial.Serial(
                port=NombrePuerto,
                baudrate=9600,
                timeout=1,
                parity=serial.PARITY_EVEN,
                stopbits=serial.STOPBITS_TWO,
                bytesize=serial.EIGHTBITS
                )
        except:
            print("ERROR - El puerto " + NombrePuerto + " no esta disponible")

    def siguiente(self, TurnosDisponibles, PantallaPrincipal):
        try:
            turno = TurnosDisponibles.UtilizarTurno()
            if turno != 0:
                PantallaPrincipal.anadir(ValueTo100(turno),self.NumeroMesa)
                if len(self.ListaTurnosAlmacenados) != 0:
                    if self.ListaTurnosAlmacenados[-1] != 0:
                        self.ListaTurnosAlmacenados.append(turno)
                        byte = IntToHexa(ValueTo100(turno))
                        self.COM.write(byte)
                    else:
                        self.ListaTurnosAlmacenados.pop(-1)
                        self.ListaTurnosAlmacenados.append(turno)
                        byte = IntToHexa(ValueTo100(turno))
                        self.COM.write(byte)
                else:
                    self.ListaTurnosAlmacenados.append(turno)
                    byte = IntToHexa(ValueTo100(turno))
                    self.COM.write(byte)
            else:
                print("No hay mas turnos existentes")
        except:
            print("ERROR en siguiente (%s) - el turno asignado es invalido" % self.NombrePuerto)

    def anterior(self, TurnosDisponibles, PantallaPrincipal):
        try:
            turno = self.getTurno()
            if turno != 0:
                PantallaPrincipal.remover(turno)
                TurnosDisponibles.DevolverTurno(self.getTurno())
                #TurnosDisponibles.PrintEstado()
                self.ListaTurnosAlmacenados.pop(-1)
                turno = self.getTurno()
                byte = IntToHexa(ValueTo100(turno))
                self.COM.write(byte)
                #print("(%s) ListaTurnosAlmacenados = %s" % (self.NombrePuerto,str(self.ListaTurnosAlmacenados)))
        except:
            print("ERROR en anterior (%s) - al retroceder de numero" % self.NombrePuerto)

    def getTurno(self):
        """docstring for getTurno
        Obtenemos el turno que se esta atendiendo actualmente
        """
        try:
            return(self.ListaTurnosAlmacenados[-1])
        except:
            return 0

    def EntroDato(self, Dato, TurnosDisponibles, PantallaPrincipal):
        if Dato == b'\x01':
            self.siguiente(TurnosDisponibles, PantallaPrincipal)
        elif Dato == b'\x02':
            self.anterior(TurnosDisponibles, PantallaPrincipal)
        else:
            print("ERROR - El dato "+str(Dato)+" enviado por "+self.NombrePuerto+" es incorrecto (Comunicacion)")

#---- Termina --- ListaDeCorrimiento --------------------------
#--------------------------------------------------------------
