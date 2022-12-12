from tkinter import *
import sqlite3
import aplicacion.bd

ventana = Tk()
ventana.resizable(0,0)
ventana.title ("Tich Login")
ventana.geometry ("350x200+500+250")
Label(ventana, text = "Nombre:").pack()
caja1 = Entry(ventana)
caja1.pack()

Label(ventana, text = "Apellido:").pack()
caja2 = Entry(ventana,)
caja2.pack()

Label(ventana, text = "Télefono:").pack()
caja2 = Entry(ventana,)
caja2.pack()

Label(ventana, text = "Documento:").pack()
caja2 = Entry(ventana,)
caja2.pack()

def login():
 # Connect to database
 db = sqlite3.connect('/home/diego123/Escritorio/login.db')
 c = db.cursor()
 
 usuario = caja1.get()
 contr = caja2.get()
 
 c.execute('SELECT * FROM usuarios WHERE usuario = ? AND pass = ?', (usuario, contr))
 
 if c.fetchall():
  showinfo(title = "Login correcto", message = "Usuario y contraseña correctos")
  print("Conexion Exitosa")
 else:
  showerror(title = "Login incorrecto", message = "Usuario o contraseña incorrecta")
  
 c.close()

Button (text = "Login", command = login).pack()


ventana.mainloop()
