#!/usr/bin/python
import Envio
import ConfigParser
from gi.repository import Gtk

class CTransferencia:
	def __init__(self,archivo):
		self.config=archivo
	
	def enviar(self,documento,label):
		configf = ConfigParser.ConfigParser()
		configf.read(self.config)
		self.direccion=configf.get('Servidor','direccion')
		#print self.direccion
		self.puerto=configf.getint('Servidor','puerto')
		#print self.puerto
		self.de=configf.get('Servidor','de')
		#print self.de
		self.para=configf.get('Servidor','para')
		#print self.para
		self.password=configf.get('Servidor','password')
		#print self.password
		trans=Envio.CEnvio(self.direccion,self.puerto)
		trans.configurar_correo(self.de,self.para)
		trans.clave(self.password)
		label.set_text("Iniciado")
		res=trans.enviar(documento)
		label.set_text("Finalizado")
		return res
			
	
