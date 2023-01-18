#programa para controlar el eritrodeformetro
#voy a usar la libreria TkInter para crear la GUI
import tkinter as tk
from tkinter import ttk
root=tk.Tk()

root.title("Eritrodeformetro")
root.config(width=400,height=300)
#defino los botones
label_ensayo=ttk.Label(root,text="Ensayos:",underline=0)
label_ensayo.place(x=10,y=10)
bot_carga=ttk.Button(root,text="Carga")
bot_carga.place(x=10,y=50)
bot_descarga=ttk.Button(root,text="Descarga")
bot_descarga.place(x=10,y=80)
bot_dinamico=ttk.Button(root,text="Dinamico")
bot_dinamico.place(x=10,y=110)
bot_encender=ttk.Button(root,text="Encender motor")
bot_encender.place(x=100,y=10)
bot_apagar=ttk.Button(root,text="Apagar motor")
bot_apagar.place(x=100,y=50)
label_puerto=ttk.Label(root,text="Puerto:")
label_puerto.place(x=100,y=80)
abrir_puerto=ttk.Radiobutton(root,text="Abrir puerto")
abrir_puerto.place(x=100,y=100)
cerrar_puerto=ttk.Radiobutton(root,text="Cerrar puerto")
cerrar_puerto.place(x=100,y=130)




root.mainloop()