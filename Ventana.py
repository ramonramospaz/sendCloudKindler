#!/usr/bin/python
from gi.repository import Gtk, Gdk, GLib
import Transferencia
from threading import Thread

#GObject.threads_init()
class CVentana(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self,title="Envio a Kindler")
		
		self.resize(200,100)
		self.trans=Transferencia.CTransferencia('config.ini')
		box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
		box.set_homogeneous(False)		
		self.add(box)
		self.button=Gtk.Button("Subir Archivo")
		self.button.connect("clicked", self.on_button_clicked)
		box.pack_start(self.button,True,True,0)
		self.label=Gtk.Label("")
		box.pack_start(self.label,False,False,0)
		self.connect("delete-event",Gtk.main_quit)
	
	def enviar_archivo(self,archivo,etiqueta):
		res=self.trans.enviar(archivo,etiqueta)
		if(res==1):
			dialogo=Gtk.MessageDialog(self,0,Gtk.MessageType.ERROR,Gtk.ButtonsType.CANCEL,"Error en archivo")
			dialogo.format_secondary_text("El nombre del archivo tiene un caracter invalid")
			dialogo.run()
			dialogo.destroy()
					
		

	def on_button_clicked(self, widget):
		self.label.set_text("")
		self.file=""
		dialog = Gtk.FileChooserDialog("Escoje el archivo", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
		self.add_filters(dialog)
		response = dialog.run()
		if response == Gtk.ResponseType.OK:
			self.file=dialog.get_filename()
		dialog.destroy()
		if self.file:
			#Thread(target=self.enviar_archivo(self.file,self.label)).start()
			#self.trans.enviar(self.file,self.label)
			self.enviar_archivo(self.file,self.label)
			self.label.set_text("Finalizado")
	
	def add_filters(self, dialog):
		filter_text = Gtk.FileFilter()
		filter_text.set_name("Pdf files")
		filter_text.add_mime_type("application/pdf")
		dialog.add_filter(filter_text)
		
		filter_text = Gtk.FileFilter()
		filter_text.set_name("Text files")
		filter_text.add_mime_type("text/plain")
		dialog.add_filter(filter_text)
	
	
	def mostrar(self):
		self.show_all()
		GLib.threads_init()
		Gdk.threads_init()
		Gdk.threads_enter()
		Gtk.main()
		Gdk.threads_leave()
