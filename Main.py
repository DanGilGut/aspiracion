import sqlite3 as lite
import time
import matplotlib

import pandas as pd

'''
Programa para crear un registro de seguimiento de un sistema de aspiración para una factoria

Funcionamiento:
 - El PLC del sistema de aspiración reporta variables cada x milisegundos y los exorta a un xls
 - Cada x seundos se registra la punta máxima en una BD sqLite
'''

def leeBaseDatos():
    print("Contenido inicial de la base de datos: ")

    conexion = lite.connect("registroAspiracion.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM registro;")
    datos = cursor.fetchall()
    for i in datos:
        print(" Maquina:" + i[1] + "\t Vibraciones: " + str(i[2]) + "\t Temperatura:" + str(i[3]) + "\t Dif_Presión:" + str(i[4]) + "\t Intensidad:" + str(i[5]))
    conexion.commit()


def guardaDatos(maq, vibr, temp, difP, inte):
    conexion = lite.connect("registroAspiracion.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO registro VALUES(NULL, '"+maq+"', '"+str(vibr)+"', '"+str(temp)+"', '"+str(difP)+"', '"+str(inte)+"');")
    conexion.commit()


def actualizaBaseDatos():
    #Creo un dataframe con el contenido del excel
    df = pd.read_excel('PLC_aspiracion.xlsx', sheet_name='Hoja1', names=['Maquina','Vibraciones','Temperatura','Dif_Presion','Intensidad'], header=None)

    #Captura inputs para del Filto 1
    miDatoF1 = df[df['Maquina']=="F1"]
    vibracionF1 = miDatoF1['Vibraciones'].mean()
    temperaturaF1 = miDatoF1['Temperatura'].mean()
    dif_PresionF1 = miDatoF1['Dif_Presion'].mean()
    intensidadF1 = miDatoF1['Intensidad'].mean()
    guardaDatos("F1", vibracionF1, temperaturaF1, dif_PresionF1, intensidadF1)

    #Captura inputs para del Filto 2
    miDatoF2 = df[df['Maquina']=="F2"]
    vibracionF2 = miDatoF2['Vibraciones'].mean()
    temperaturaF2 = miDatoF2['Temperatura'].mean()
    dif_PresionF2 = miDatoF2['Dif_Presion'].mean()
    intensidadF2 = miDatoF2['Intensidad'].mean()
    guardaDatos("F2", vibracionF2, temperaturaF2, dif_PresionF2, intensidadF2)

    #Captura inputs para del Filto 3
    miDatoF3 = df[df['Maquina']=="F3"]
    vibracionF3 = miDatoF3['Vibraciones'].mean()
    temperaturaF3 = miDatoF3['Temperatura'].mean()
    dif_PresionF3 = miDatoF3['Dif_Presion'].mean()
    intensidadF3 = miDatoF3['Intensidad'].mean()
    guardaDatos("F3", vibracionF3, temperaturaF3, dif_PresionF3, intensidadF3)

    #Captura inputs para del Filto 4
    miDatoF4 = df[df['Maquina']=="F4"]
    vibracionF4 = miDatoF4['Vibraciones'].mean()
    temperaturaF4 = miDatoF4['Temperatura'].mean()
    dif_PresionF4 = miDatoF4['Dif_Presion'].mean()
    intensidadF4 = miDatoF4['Intensidad'].mean()
    guardaDatos("F4", vibracionF4, temperaturaF4, dif_PresionF4, intensidadF4)


leeBaseDatos()

# Actualizamos la BD cada 5 segundos y limpiamos el excel
while True:
    time.sleep(5)
    actualizaBaseDatos()

    '''
    # Limiar archivo / Ne entran datos - evitar error
    wb = load_workbook(filename='PLC_aspiracion.xlsx')
    for row in wb['Hoja1']:
        for cell in row:
            cell.value = None
    wb.save(filename='PLC_aspiracion.xlsx')
    wb.close()
    
    '''