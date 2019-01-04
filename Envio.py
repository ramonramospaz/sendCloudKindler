#!/usr/bin/python

import smtplib
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication



class CEnvio:
	__servidor=""
	__puerto=0
	__de=""
	__para=""
	__clave=""
	
	def __init__(self,servidor,puerto):
		self.__servidor=servidor
		self.__puerto=puerto
	
	def configurar_correo(self,de,para):
		self.__de=de
		self.__para=para
	
	def clave(self,clave):
		self.__clave=clave
	
	def enviar(self,archivo):

		#hacia donde el libro
		mensaje = MIMEMultipart()
		mensaje['Subject']='Envio documento para kindler'
		mensaje['From']=self.__de
		mensaje['To']=self.__para
		
		#Agrega texto
		cuerpo=MIMEText('Envio documento para kindler')
		mensaje.attach(cuerpo)

		#agragar archivo (acuerdate de validar el archivo)		
		fp=open(archivo,'rb')
		#validar la extension del archivo para subirlo
		att=MIMEApplication(fp.read(),_subtype="pdf")
		fp.close()
		nombre_archivo=archivo[archivo.rfind("/")+1:].replace(' ','_')
		print nombre_archivo
		resultado=0
		if(not self.check(nombre_archivo)):
			att.add_header('Content-Disposition','attachment; filename=%s'%nombre_archivo)
			mensaje.attach(att)
			#intento enviarlo
			try:
				smtpObj = smtplib.SMTP(self.__servidor,self.__puerto)
				smtpObj.ehlo()
				smtpObj.starttls()
				smtpObj.ehlo
				smtpObj.login(self.__de,self.__clave)
				smtpObj.sendmail(self.__de,self.__para,mensaje.as_string())
				print "El mensaje se envio de forma exitosa"
			except: 
				print "Existe un problema para enviar el mensaje, verifique los datos de configuracion"
		else:
			resultado=1
			print "Existe un problema en el archivo a enviar"
		return resultado
	
	def check(self,texto):
		patron = r'[^\.\_\-qa-zA-Z0-9]'
		print re.search(patron,texto)
		return re.search(patron,texto)
			
		
	
