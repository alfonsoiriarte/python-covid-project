"""
Fecha: Abril de 2020
Autor: Alfonso Iriarte
"""
# %%
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

def borrarPantalla():
    os.system("cls")
borrarPantalla()
appExit = 0

while appExit != 1:
    print("-------Graficador de Casos Covid-19-------")
    print("Espere...")
    ##############################################################################          Filtrado de datos       ##################################################

    #Leo el archivo y lo guardo en "datos" indexando la columna "date"
    fullExcel = pd.read_csv("full_data.csv", index_col ="location")

    #Creo una fila para poder comparar todos los datos
    fullExcel['enumero0'] = [x for x in range(len(fullExcel))]
    fullExcel.to_excel("verificoPais.xlsx")
    verificaciones = pd.read_excel("verificoPais.xlsx", index_col ="enumero0")
    ##############################################################################          Filtro Paises
    #Pido el ingreso de los paises deseados
    flagVer1 = 0
    flagVer2 = 0
    flagIngresoPais = 0
    while flagIngresoPais != 1:
        if flagVer1 == 0:
            pais1 = input(print("Ingrese el primer país:"))
        if flagVer2 == 0:
            pais2 = input(print("Ingrese el segundo país:"))

        for i in range(len(fullExcel)):
            if verificaciones.loc[i,'location'] == pais1:
                flagVer1 = 1
            if verificaciones.loc[i,'location'] == pais2:
                flagVer2 = 1
        if flagVer1 == 0: 
            print("[ERROR]El primer pais no se encuentra en la lista o su sintaxis es incorrecta. Ejemplo correcto: 'Brazil'.")
        if flagVer2 == 0: 
            print("[ERROR]El segundo pais no se encuentra en la lista o su sintaxis es incorrecta. Ejemplo correcto: 'Brazil'.")
        if flagVer1 == 1 and flagVer2 == 1:
            flagIngresoPais = 1
            

    #Filtro solo las filas del primer pais ingresado                                        FILTRO 1 PAIS 1
    filtroPais1 = fullExcel.loc[pais1]
    filtroPais1['enumero1'] = [x for x in range(len(filtroPais1))]
    filtroPais1.to_excel("verificoLim1.xlsx")
    verificaciones1 = pd.read_excel("verificoLim1.xlsx", index_col ="enumero1")

    #Filtro solo las filas del segundo pais ingresado                                       FILTRO 1 PAIS 2
    filtroPais2 = fullExcel.loc[pais2]
    filtroPais2['enumero1'] = [x for x in range(len(filtroPais2))]
    filtroPais2.to_excel("verificoLim2.xlsx")
    verificaciones2 = pd.read_excel("verificoLim2.xlsx", index_col ="enumero1")

    flag1Ver1 = 0
    flag1Ver2 = 0
    flag2Ver1 = 0
    flag2Ver2 = 0
    flagIngresoLim = 0
    borrarPantalla()
    while(flagIngresoLim != 1):
        #Pido el ingreso de los datos del intervalo
        
        año1 = input(print("--------Ingrese el año (en número) de la fecha inicial del intervalo de tiempo: "))
        mes1 = input(print("--------Ingrese el mes (en número) de la fecha inicial del intervalo de tiempo: "))
        dia1 = input(print("--------Ingrese el día (en número) de la fecha inicial del intervalo de tiempo: "))

        año2 = input(print("--------Ingrese el año (en número) de la fecha final del intervalo de tiempo: "))
        mes2 = input(print("--------Ingrese el mes (en número) de la fecha final del intervalo de tiempo: "))
        dia2 = input(print("--------Ingrese el día (en número) de la fecha final del intervalo de tiempo: "))

        #Guardo el los datos del intervalo
        lim1 = año1 + "-" + mes1 + "-" + dia1
        lim2 = año2 + "-" + mes2 + "-" + dia2

        #Verifico que las fechas sean correctas
        for i in range(len(filtroPais1)):
            if verificaciones1.loc[i,'date'] == lim1:
                flag1Ver1 = 1
        for i in range(len(filtroPais1)):        
            if verificaciones1.loc[i,'date'] == lim2:
                flag1Ver2 = 1
        for i in range(len(filtroPais2)):
            if verificaciones2.loc[i,'date'] == lim1:
                flag2Ver1 = 1
        for i in range(len(filtroPais2)):
            if verificaciones2.loc[i,'date'] == lim2:
                flag2Ver2 = 1
        #Verifico que no haya ningun error para seguir o volver a tomar los datos
        if flag1Ver1 == 1 and flag1Ver2 == 1:  
            flagIngresoLim = 1
        else:
            print("[ERROR]La fecha es incorrecta o no se encuentra para ninguno de los paises elegidos, pruebe un dia cercano  de la fecha final o inicial (tenga en cuenta que los limites son 2019-12-31 Y 2020-04-29)")
        if flag2Ver1 == 1 and flag2Ver2 == 1:
            flagIngresoLim = 1
        else:
            print("[ERROR]La fecha es incorrecta o no se encuentra para ninguno de los paises elegidos, pruebe un dia cercano  de la fecha final o inicial (tenga en cuenta que los limites son 2019-12-31 Y 2020-04-29)")

    ##########################################################################################################  PAIS 1
    #Exporto excel para poder filtrar por limites de fechas                             FILTRO 2 PAIS 1
    filtroPais1.to_excel("filtroPais1.xlsx")
    datosFiltrados1 = pd.read_excel("filtroPais1.xlsx", index_col ="date")
    filtroFechas1 = datosFiltrados1.loc[lim1:lim2]

    #Exporto excel para poder guardar los datos para el eje y                           FILTRO 3 PAIS 1
    filtroFechas1.to_excel("filtroCasos1.xlsx")
    filtroCasos1 = pd.read_excel("filtroCasos1.xlsx", index_col ="total_cases")
    ##########################################################################################################  PAIS 2
    #Exporto excel para poder filtrar por limites de fechas                             FILTRO 2 PAIS 2
    filtroPais2.to_excel("filtroPais2.xlsx")
    datosFiltrados2 = pd.read_excel("filtroPais2.xlsx", index_col ="date")
    filtroFechas2 = datosFiltrados2.loc[lim1:lim2]

    #Exporto excel para poder guardar los datos para el eje y                           FILTRO 3 PAIS 2
    filtroFechas2.to_excel("filtroCasos2.xlsx")
    filtroCasos2 = pd.read_excel("filtroCasos2.xlsx", index_col ="total_cases")

    ##############################################################################              GRAFICOS              ###########################################################

    #Configuro graficos
    plt.xlabel("Tiempo[AÑO-MES-DIA]")   # Inserta el título del eje X
    plt.ylabel("Casos/Fallecimientos totales")   # Inserta el título del eje Y

    #Establezco los ejes del primer grafico
    ejex1 = filtroCasos1.loc[:,'date']
    casos1 = filtroFechas1.loc[:,'total_cases']
    fallecimientos1 = filtroFechas1.loc[:,'total_deaths']

    #Establezco los ejes del segundo grafico
    ejex2 = filtroCasos2.loc[:,'date']
    casos2 = filtroFechas2.loc[:,'total_cases']
    fallecimientos2 = filtroFechas2.loc[:,'total_deaths']

    #Titulo
    plt.title("Casos y Fallecimientos para los paises ingresados")

    #Grafico del primer pais
    plt.plot(ejex1,casos1, linestyle='-', color='r', label = "Casos (País 1)")
    plt.plot(ejex1,fallecimientos1, linestyle='-', color='g', label = "Fallecimientos (País 1)")
    axes = plt.gca ()
    axes.xaxis.set_ticklabels(ejex1, rotation = -45, fontsize = 8, style = 'italic')


    #Grafico del segundo pais
    plt.plot(ejex2,casos2, linestyle='-', color='b', label = "Casos (País 2)")
    plt.plot(ejex2,fallecimientos2, linestyle='-', color='k', label = "Fallecimientos (País 2)")
    axes = plt.gca ()
    axes.xaxis.set_ticklabels(ejex2, rotation = -45, fontsize = 8, style = 'italic')

    ################################################################################################ Indexeo fila numerica creciente por la cantidad de fechas que hayan

    #Creo una fila para poder comparar todos los datos
    filtroFechas1['enumero1'] = [x for x in range(len(filtroFechas1.loc[:,'total_cases']))]
    filtroFechas1.to_excel("filtradoCruces1.xlsx")
    filtradoCruces1 = pd.read_excel("filtradoCruces1.xlsx", index_col ="enumero1")

    #Creo una fila para poder comparar todos los datos
    filtroFechas2['enumero2'] = [x for x in range(len(filtroFechas2.loc[:,'total_cases']))]
    filtroFechas2.to_excel("filtradoCruces2.xlsx")
    filtradoCruces2 = pd.read_excel("filtradoCruces2.xlsx", index_col ="enumero2")

    ################################################################################################ COMPARO PUNTOS DE CASOS TOTALES DE LAS FUNCIONES

    #Comparo los casos los dos paises en cada fecha y creo puntos en los graficos
    cruces = [x for x in range(len(filtradoCruces1.loc[:,'total_cases']))]
    flagCruce = 0
    for i in range(len(filtroFechas1.loc[:,'total_cases'])):
        if filtradoCruces1.loc[i,'total_cases'] == filtradoCruces2.loc[i,'total_cases']:
            cruces[i] = filtradoCruces1.loc[i,'total_cases']
            if flagCruce == 1:
                plt.plot(filtradoCruces1.loc[i,'date'],cruces[i], 'ro', color='k')
            else:
                plt.plot(filtradoCruces1.loc[i,'date'],cruces[i], 'ro', color='k', label = "Intersecciones de casos")
            flagCruce = 1
        else: 
            cruces[i] = 0
        i+1
    if flagCruce == 0:
        plt.plot(color='k', label = "Intersecciones de casos")
    ################################################################################################ COMPARO PUNTOS DE FALLECIMIENTOS TOTALES DE LAS FUNCIONES

    #Comparo los casos los dos paises en cada fecha y creo puntos en los graficos
    cruces = [x for x in range(len(filtradoCruces1.loc[:,'total_deaths']))]
    flagCruce = 0
    for i in range(len(filtroFechas1.loc[:,'total_deaths'])):
        
        if filtradoCruces1.loc[i,'total_deaths'] == filtradoCruces2.loc[i,'total_deaths']:
            cruces[i] = filtradoCruces1.loc[i,'total_deaths']
            if flagCruce == 1:
                plt.plot(filtradoCruces1.loc[i,'date'],cruces[i], 'ro', color='r')
            else:
                plt.plot(filtradoCruces1.loc[i,'date'],cruces[i], 'ro', color='r', label = "Intersecciones de fallecimientos")
            flagCruce = 1
        else: 
            cruces[i] = 0
        i+1
    if flagCruce == 0:
        plt.plot(color='r', label = "Intersecciones de fallecimientos")

    borrarPantalla()
    print("-----PAIS 1:", pais1,"-----")
    print("-----PAIS 2:", pais2,"-----")
    print("Sugerencia: Amplíe el grafico para una mejor resolución.")

    #Muestro los graficos
    plt.legend(loc="upper left")
    plt.yscale('log') 
    plt.show()





    borrarPantalla()
    salidaValida = 0
    while salidaValida != 1:
        print("--REINICIAR APLICACIÓN-- N")
        print("--FINALIZAR APLICACIÓN-- S")
        salida = input()
        if salida == "S" or salida == "s":
            appExit = 1
            salidaValida = 1
            borrarPantalla()
        elif salida == "N" or salida == "n":
            appExit = 0
            salidaValida = 1
            borrarPantalla()
        else:
            print("[ERROR]Letra invalida.")
        

borrarPantalla()
print("APLICACION FINALIZADA CON EXITO.")
print("Autor: Alfonso Iriarte.")