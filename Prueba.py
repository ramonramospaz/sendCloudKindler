#!/usr/bin/python
import Envio

#Test

a=Envio.CEnvio('smtp.gmail.com',587)
a.configurar_correo('ramonramospaz@gmail.com','ramonramospaz@gmail.com')
a.clave('15281565')
a.enviar('x.pdf')
