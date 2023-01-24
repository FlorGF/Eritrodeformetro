#programa para controlar el eritrodeformetro
#voy a usar la libreria TkInter para crear la GUI
import tkinter as tk
from tkinter import ttk
root=tk.Tk()

root.title("Eritrodeformetro")
root.config(width=400,height=300)
#defino los botones

#botones de ensayo
label_ensayo=ttk.LabelFrame(root,text="Ensayos:")
label_ensayo.grid(column=0,row=0)
bot_carga=ttk.Button(label_ensayo,text="Carga")
bot_carga.grid(column=0,row=1)
bot_descarga=ttk.Button(label_ensayo,text="Descarga")
bot_descarga.grid(column=0,row=2)
bot_dinamico=ttk.Button(label_ensayo,text="Dinamico")
bot_dinamico.grid(column=0,row=3)

#botones de motor
bot_encender=ttk.Button(root,text="Encender motor")
bot_encender.grid(column=1,row=0)
bot_apagar=ttk.Button(root,text="Apagar motor")
bot_apagar.grid(column=1,row=1)

#botones del puerto
label_puerto=ttk.LabelFrame(root,text="Puerto:")
label_puerto.grid(column=1,row=2)
abrir_puerto=ttk.Radiobutton(label_puerto,text="Abrir")
abrir_puerto.grid(column=1,row=3)
cerrar_puerto=ttk.Radiobutton(label_puerto,text="Cerrar")
cerrar_puerto.grid(column=1,row=4)

#botones de frecuencia
label_frecuencia=ttk.LabelFrame(root,text="Frecuencia:")
label_frecuencia.grid(column=0,row=5)
cinco=ttk.Radiobutton(label_frecuencia,text="0,5Hz")
cinco.grid(column=0,row=6)
diez=ttk.Radiobutton(label_frecuencia,text="1Hz")
diez.grid(column=0,row=7)
quince=ttk.Radiobutton(label_frecuencia,text="1,5Hz")
quince.grid(column=0,row=8)


#botones de velocidad
label_velocidad=ttk.LabelFrame(root,text="Velocidad:")
label_velocidad.grid(column=1,row=5)
menor=ttk.Radiobutton(label_velocidad,text="17rpm")
menor.grid(column=1,row=6)
intermedia=ttk.Radiobutton(label_velocidad,text="35rpm")
intermedia.grid(column=1,row=7)
mayor=ttk.Radiobutton(label_velocidad,text="70rpm")
mayor.grid(column=1,row=8)
root.mainloop()