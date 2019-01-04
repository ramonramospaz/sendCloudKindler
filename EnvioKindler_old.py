#!/usr/bin/python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

servidor='smtp.gmail.com'
puerto=587
De='ramonramospaz@gmail.com'
#Para='ramonramospaz@gmail.com'
Para='ramonramospaz@kindle.com'
Titulo='Envio documento para kindler'
Texto='Envio documento para Kindler'

#hacia donde el correo
mensaje = MIMEMultipart()
mensaje['Subject']=Titulo
mensaje['From']=De 
mensaje['To']=Para

#Agrega texto
cuerpo=MIMEText(Texto)
mensaje.attach(cuerpo)

#Agrega PDF
archivo='DeepC_Scandev_Mar2013.pdf'
fp=open(archivo,'rb')
att=MIMEApplication(fp.read(),_subtype="pdf")
fp.close()
att.add_header('Content-Disposition','attachment; filename=%s'%archivo)
mensaje.attach(att)

try:
	smtpObj = smtplib.SMTP(servidor,puerto)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.ehlo
	smtpObj.login(De,'x15281565')
	smtpObj.sendmail(De,Para,mensaje.as_string())
	print "El mensaje se envio de forma exitosa"
except SMTPException:
	print "Existe un problema para enviar el mensaje"