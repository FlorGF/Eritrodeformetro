#programa para controlar el eritrodeformetro
#voy a usar la libreria TkInter para crear la GUI
import tkinter as tk
from tkinter import ttk
root=tk.Tk()

root.title("Eritrodeformetro")
root.config(width=400,height=300)
#defino los botones
label_ensayo=ttk.LabelFrame(root,text="Ensayos:")
label_ensayo.grid(column=0,row=0)
bot_carga=ttk.Button(label_ensayo,text="Carga")
bot_carga.grid(column=0,row=1)
bot_descarga=ttk.Button(label_ensayo,text="Descarga")
bot_descarga.grid(column=0,row=2)
bot_dinamico=ttk.Button(label_ensayo,text="Dinamico")
bot_dinamico.grid(column=0,row=3)
bot_encender=ttk.Button(root,text="Encender motor")
bot_encender.grid(column=1,row=0)
bot_apagar=ttk.Button(root,text="Apagar motor")
bot_apagar.grid(column=1,row=1)
label_puerto=ttk.LabelFrame(root,text="Puerto:")
label_puerto.grid(column=1,row=2)
abrir_puerto=ttk.Radiobutton(label_puerto,text="Abrir")
abrir_puerto.grid(column=1,row=3)
cerrar_puerto=ttk.Radiobutton(label_puerto,text="Cerrar")
cerrar_puerto.grid(column=1,row=4)




root.mainloop()