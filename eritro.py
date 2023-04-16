#programa para controlar el reometro
#voy a usar la libreria TkInter para crear la GUI
# para comunicarme con el puerto USB voy a usar la libreria pySerial
#para graficar voy a usar matplotlib
#para splitear el string que me mandan desde el USB voy a usar la libreria string
import tkinter as tk
from tkinter import ttk
import serial 
import matplotlib as plt 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv

root=tk.Tk()
ser=serial.Serial() #falta definir donde esta el puerto
root.title("Eritrodeformetro")
root.config(width=400,height=300)

#FUNCIONES
#esta funcion es generica para escribir por el puerto serie, manda los token
def comunicaUSB(cod_token):
    ser.write(cod_token)

#esta funcion se encarga de leer los datos que se mandan desde el puerto
def leerUSB():
    datos = ser.readline() #datos es un string 
    return datos

#funcion para graficar en la GUI
def graficar(x,r,t,cent):
    figure = Figure(figsize=(6, 4), dpi=100)
    ax1 = figure.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure, top)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    ax1.plot(x,r,"bo",label="Eje R")
    ax1.plot(x,t,"g",label="Eje T")
    ax1.plot(x,cent,"r",label="Central")
    ax1.set_title("Gráfica")
    ax1.set_ylabel("Intensidad")
    ax1.set_xlabel("Tiempo")

def ensayo(codigo,tiempo):
    tiempo = []
    eje_r = []
    eje_t = []
    cent = []
    comunicaUSB(codigo) 
    #aca debería poner que espere el OK que esta midiendo 
    #también deberia esperar una cantidad de tiempo dada por cada ensayo así no toma datos
    med = leerUSB()
    #tengo que pasarla a flotante aca 
    medicion = med.split(sep="\n")
    for m in medicion: 
        aux = m.split(sep=";")
        tiempo.append=aux[0]
        eje_r.append=aux[1]
        eje_t.append=aux[2]
        cent.append=aux[3]
    graficar(tiempo,eje_r,eje_t,cent)
    return medicion

#funcion para guardar la medición 
def guardar():
    med = leerUSB()
    medicion = med.split(sep="\n")
    with open('medicion.csv',mode='w') as file:
         data_writer = csv.writer(file)
         for m in med: 
              data_writer.writerow(m)
    

    
#funcionalidad del boton de parada
def parada(): 
    cod="M00000"
    print(cod)
    #ensayo(cod)


#funcionalidad del puerto
def f_puerto(): 
    flag_puerto=puerto.get()
    if flag_puerto == 1: 
        ser.open()
    if flag_puerto == 0:
        ser.close()


#funcionalidad del boton de carga
def e_carga():
    vel=velocidad.get()
    cod="EC"+vel+"00"
    tiempo=333.3 #tiempo que dura el ensayo
   #ensayo(cod,tiempo)
    print(cod)
  

#funcionalidad del boton de descarga
def e_descarga():
    tiempo=433.3 #tiempo que dura el ensayo
    vel=velocidad.get()
    cod="ED"+vel+"00"
    #ensayo(cod,tiempo)
    print(cod)
    


def e_dinamico():
    tiempo=433.3 #tiempo que dura el ensayo
    vel=velocidad.get()
    f=frec.get()
    if(f != 5):
        cod="EO"+vel+f
    else:
        cod="EO"+vel+"0"+f 
    
    print(cod)
    #ensayo(cod,tiempo)
    

##########################################################################################
#defino los botones

#botones de motor
bot_encender=ttk.Button(root,text="Encender motor",command=parada)
bot_encender.grid(column=1,row=0)
bot_apagar=ttk.Button(root,text="Apagar motor")
bot_apagar.grid(column=1,row=1)

#botones del puerto
puerto=tk.StringVar()
label_puerto=ttk.LabelFrame(root,text="Puerto:")
label_puerto.grid(column=1,row=2)
abrir_puerto=ttk.Radiobutton(label_puerto,text="Abrir",value=1,variable=puerto)
abrir_puerto.grid(column=1,row=3)
cerrar_puerto=ttk.Radiobutton(label_puerto,text="Cerrar",value=0,variable=puerto)
cerrar_puerto.grid(column=1,row=4)

#botones de frecuencia
frec=tk.StringVar()
label_frecuencia=ttk.LabelFrame(root,text="Frecuencia:")
label_frecuencia.grid(column=0,row=5)
cinco=ttk.Radiobutton(label_frecuencia,text="0,5Hz",value=5,variable=frec)
cinco.grid(column=0,row=6)
diez=ttk.Radiobutton(label_frecuencia,text="1Hz",value=10,variable=frec)
diez.grid(column=0,row=7)
quince=ttk.Radiobutton(label_frecuencia,text="1,5Hz",value=15,variable=frec)
quince.grid(column=0,row=8)


#botones de velocidad
velocidad=tk.StringVar()
label_velocidad=ttk.LabelFrame(root,text="Velocidad:")
label_velocidad.grid(column=1,row=5)
menor=ttk.Radiobutton(label_velocidad,text="17rpm",value=17,variable=velocidad)
menor.grid(column=1,row=6)
intermedia=ttk.Radiobutton(label_velocidad,text="35rpm",value=35,variable=velocidad)
intermedia.grid(column=1,row=7)
mayor=ttk.Radiobutton(label_velocidad,text="70rpm",value=70,variable=velocidad)
mayor.grid(column=1,row=8)

#botones de ensayo
label_ensayo=ttk.LabelFrame(root,text="Ensayos:")
label_ensayo.grid(column=0,row=0)
bot_carga=ttk.Button(label_ensayo,text="Carga",command=e_carga)
bot_carga.grid(column=0,row=1)
bot_descarga=ttk.Button(label_ensayo,text="Descarga",command=e_descarga)
bot_descarga.grid(column=0,row=2)
bot_dinamico=ttk.Button(label_ensayo,text="Dinamico",command=e_dinamico)
bot_dinamico.grid(column=0,row=3)





root.mainloop()