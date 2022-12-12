import tkinter
from tkinter import *
import sqlite3
      
ventana = Tk()
ventana.resizable(0,0)
ventana.title ("Tizi Login")
ventana.geometry ("350x200+500+250")
Label(ventana, text = "Nombre:").pack()
caja1 = Entry(ventana)
caja1.pack()
Label(ventana, text = "Apellido:").pack()
caja2 = Entry(ventana)
caja2.pack()
Label(ventana, text = "Télefono").pack()
caja1 = Entry(ventana)
caja1.pack()
Label(ventana, text = "Documento:").pack()
caja1 = Entry(ventana)
caja1.pack()
guar = tkinter.Button (ventana, text= "Guardar", command = ventana)
guar.pack()
guar.place(x=137, y=165)

#Acceder a base de datos

bd = sqlite3.connect("juego_tizi.bd")
cursor = bd.cursor()
cursor.execute("SELECT * FROM login")
print(cursor)
datos = cursor.fetchone()
print(datos)
    
    
valores = [('tomas', 'silva', '1123456789', '23453234'),
  ('lucas', 'ugarte', '1109785693', '97458452'),
  ('demian', 'gallardo', '1189743792', '63549232')]

cursor.executemany("INSERT INTO login VALUES (?,?,?,?)", valores)

bd.commit()

bd.close()
ventana.mainloop()