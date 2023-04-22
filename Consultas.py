import random
import sqlite3 as lite
import tkinter
from tkinter import *
from PIL import Image, ImageTk

import matplotlib
import pandas as pd
from matplotlib.backends._backend_tk import NavigationToolbar2Tk

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import matplotlib.pyplot as plt

'''
Programa para conultar el registro registro de seguimiento de un sistema de aspiración para una factoria

Los datos se toman de la base de datos y estos se alimentan a traves de un excel - ver archivo Main.py - 
'''


def leeVibraciones():
    print("La vibración máxima registrada ha sido de: ")
    conexion = lite.connect("registroAspiracion.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM registro where vibraciones = (SELECT MAX (vibraciones) FROM registro);")
    tomarDatos = ""
    datos = cursor.fetchall()
    for i in datos:
        print(" Maquina:" + i[1] + "\t Vibraciones: " + str(i[2]) + "\t Temperatura:" + str(
            i[3]) + "\t Dif_Presión:" + str(i[4]) + "\t Intensidad:" + str(i[5]))
        tomarDatos += str(" Maquina:" + i[1] + "\t Vibraciones: " + str(i[2]) + "\t Temperatura:" + str(
            i[3]) + "\t Dif_Presión:" + str(i[4]) + "\t Intensidad:" + str(i[5]) + "\n")

    reporteDatos.insert(INSERT, tomarDatos)
    conexion.commit()


def leeTemperaturas():
    print("La temperatura máxima registrada ha sido de: ")
    conexion = lite.connect("registroAspiracion.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM registro where temperatura = (SELECT MAX (temperatura) FROM registro);")
    tomarDatos = ""
    datos = cursor.fetchall()
    for i in datos:
        print(" Maquina:" + i[1] + "\t Vibraciones: " + str(i[2]) + "\t Temperatura:" + str(
            i[3]) + "\t Dif_Presión:" + str(i[4]) + "\t Intensidad:" + str(i[5]))
        tomarDatos += str(" Maquina:" + i[1] + "\t Vibraciones: " + str(i[2]) + "\t Temperatura:" + str(
            i[3]) + "\t Dif_Presión:" + str(i[4]) + "\t Intensidad:" + str(i[5]) + "\n")

    reporteDatos.insert(INSERT, tomarDatos)
    conexion.commit()


def leeDifPresión():
    print("La caida de presión máxima registrada ha sido de: ")
    conexion = lite.connect("registroAspiracion.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM registro where dif_tension = (SELECT MAX (dif_tension) FROM registro);")
    tomarDatos = ""
    datos = cursor.fetchall()
    for i in datos:
        print(" Maquina:" + i[1] + "\t Vibraciones: " + str(i[2]) + "\t Temperatura:" + str(
            i[3]) + "\t Dif_Presión:" + str(i[4]) + "\t Intensidad:" + str(i[5]))
        tomarDatos += str(" Maquina:" + i[1] + "\t Vibraciones: " + str(i[2]) + "\t Temperatura:" + str(
            i[3]) + "\t Dif_Presión:" + str(i[4]) + "\t Intensidad:" + str(i[5]) + "\n")

    reporteDatos.insert(INSERT, tomarDatos)
    conexion.commit()


def leeIntensidad():
    print("La intensidad máxima registrada ha sido de: ")
    conexion = lite.connect("registroAspiracion.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM registro where intensidad = (SELECT MAX (intensidad) FROM registro);")
    tomarDatos = ""
    datos = cursor.fetchall()
    for i in datos:
        print(" Maquina:" + i[1] + "\t Vibraciones: " + str(i[2]) + "\t Temperatura:" + str(
            i[3]) + "\t Dif_Presión:" + str(i[4]) + "\t Intensidad:" + str(i[5]))
        tomarDatos += str(" Maquina:" + i[1] + "\t Vibraciones: " + str(i[2]) + "\t Temperatura:" + str(
            i[3]) + "\t Dif_Presión:" + str(i[4]) + "\t Intensidad:" + str(i[5]) + "\n")

    reporteDatos.insert(INSERT, tomarDatos)
    conexion.commit()


def graficoVibraciones():
    conexion = lite.connect("registroAspiracion.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT vibraciones FROM registro where maquina == 'F1' ;")
    listaDatos1 = cursor.fetchall()
    cursor.execute("SELECT vibraciones FROM registro where maquina == 'F2' ;")
    listaDatos2 = cursor.fetchall()
    cursor.execute("SELECT vibraciones FROM registro where maquina == 'F3' ;")
    listaDatos3 = cursor.fetchall()
    cursor.execute("SELECT vibraciones FROM registro where maquina == 'F4' ;")
    listaDatos4 = cursor.fetchall()

    #Genero dataframes con los datos de las consultas
    df1 = pd.DataFrame(listaDatos1,columns=['Filtro 1'])
    df2 = pd.DataFrame(listaDatos2,columns=['Filtro 2'])
    df3 = pd.DataFrame(listaDatos3,columns=['Filtro 3'])
    df4 = pd.DataFrame(listaDatos4,columns=['Filtro 4'])

    #Genero gráficos
    primero = df1.plot(color='blue')
    segundo = df2.plot(color='yellow', ax=primero)
    tercero = df3.plot(color='green', ax=segundo)
    df4.plot(color='red', ax=tercero)
    plt.ylabel('Nivel de vibraciones')
    plt.show()

    #Mostrar gráfico en ventana
    root = tkinter.Tk()
    fig = Figure(figsize=(6, 4))
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    #Barra de herremientas
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)



def limpia():
    reporteDatos.delete('1.0', END)


def tomarVibracionMax():
    conexion = lite.connect("registroAspiracion.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT vibraciones FROM registro where vibraciones = (SELECT MAX (vibraciones) FROM registro) ;")
    datosVibMax = cursor.fetchall()
    datosVibMax = str(datosVibMax[0])
    return datosVibMax

def tomarTempMax():
    conexion = lite.connect("registroAspiracion.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT temperatura FROM registro where temperatura = (SELECT MAX (temperatura) FROM registro) ;")
    datosTempMax = cursor.fetchall()
    datosTempMax = str(datosTempMax[0])
    return datosTempMax

def tomarDifPresMax():
    conexion = lite.connect("registroAspiracion.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT dif_tension FROM registro where dif_tension = (SELECT MAX (dif_tension) FROM registro) ;")
    datosDifPresMax = cursor.fetchall()
    datosDifPresMax = str(datosDifPresMax[0])
    return datosDifPresMax

def tomarIntPresMax():
    conexion = lite.connect("registroAspiracion.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT intensidad FROM registro where intensidad = (SELECT MAX (intensidad) FROM registro) ;")
    datosIntMax = cursor.fetchall()
    datosIntMax = str(datosIntMax[0])
    return datosIntMax

marco = Frame(width=600, height=600)
marco.grid(pady=5,padx=5)

titulo = Label(marco, text="Sistema control aspiración", fg="black", font=("Arial,Verdana,sans-serif", 30))
titulo.grid(pady=5,padx=5, row=1, column=0)
mensaje = Label(marco, text="Area de consulta para personal de mantenimiento", fg="grey",
                font=("Arial,Verdana,sans-serif", 16))
mensaje.grid(pady=5,padx=5, row=2, column=0)

# Imagen aleatoria
images = ["imagenes/imagenFiltro.png", "imagenes/imagenFiltro2.png", "imagenes/imagenFiltro3.png",
          "imagenes/imagenFiltro4.png"]
i = random.randrange(4)
foto = ImageTk.PhotoImage(file=images[i], width=600, height=400)
textofoto = Label(marco, image=foto)
textofoto.grid(pady=5,padx=5, row=3, column=0)

# Buscar y leer registros de la base de datos acerca vibraciones
botondame = Button(marco, text="Consulta de vibraciones máximas", command=lambda: leeVibraciones())
botondame.config(width=30, height=1)
botondame.grid(pady=5,padx=5, row=4, column=0)

# Buscar y leer registros de la base de datos acerca temperaturas
botondame = Button(marco, text="Consulta de temperaturas máximas", command=lambda: leeTemperaturas())
botondame.config(width=30, height=1)
botondame.grid(pady=5,padx=5, row=5, column=0)

# Buscar y leer registros de la base de datos acerca temperaturas
botondame = Button(marco, text="Consulta de caidas de pressión máxima", command=lambda: leeDifPresión())
botondame.config(width=30, height=1)
botondame.grid(pady=5,padx=5, row=6, column=0)

# Buscar y leer registros de la base de datos acerca temperaturas
botondame = Button(marco, text="Consulta de intensidad máxima", command=lambda: leeIntensidad())
botondame.config(width=30, height=1)
botondame.grid(pady=5,padx=5, row=7, column=0)

# Reporte en el textBox
reporteDatos = Text(marco, height=25, width=82)
reporteDatos.get("1.0", "end")
reporteDatos.grid(pady=5,padx=5, row=3, column=1)

# Boton limpiar textBox
botondame = Button(marco, text="Limpiar", command=lambda: limpia())
botondame.config(width=30, height=1)
botondame.grid(pady=5,padx=5, row=4, column=1)

# Grafico de vibraciones
botondame = Button(marco, text="Grafico de vibraciones", command=lambda: graficoVibraciones())
botondame.config(width=30, height=1)
botondame.grid(pady=5,padx=5, row=5, column=1)

# Etiqueta para vibracions máximas
datos = "\t"+tomarVibracionMax()+tomarTempMax()+tomarDifPresMax()+tomarIntPresMax()
datos = datos.replace('(','').replace(')','').replace(',','\t')
etiquetaVibraciones = Label(marco, text="Niveles máximos obtenidos (Vib / Temp / Pres / Int): "+datos, fg="black",font=("Arial,Verdana,sans-serif",10))
etiquetaVibraciones.grid(pady=5,padx=5, row=6, column=1)

mainloop()
