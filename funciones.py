import statistics
import random
import csv

def asignar():
    print(" ")
    sueldos = []
    for i in range(10):
        sueldos.append(random.randint(300000,2500000))
    return sueldos

def clasificar(sueldos,trabajadores):
    bajo = []
    medio = []
    alto = []
    for i in range(10):
        if sueldos[i] < 800000:
            bajo.append([sueldos[i],trabajadores[i]])
        elif sueldos[i] >= 800000 and sueldos[i] < 2000000:
            medio.append([sueldos[i],trabajadores[i]])
        elif sueldos[i] >= 2000000:
            alto.append([sueldos[i],trabajadores[i]])
    bajo.sort()
    medio.sort()
    alto.sort()
    print(" ")
    print("Sueldos menores a $800.000 TOTAL: "+str(len(bajo)))
    print(" ")
    if len(bajo) == 0:
        None
    else:
        print("Nombre empleado"+" "*15+"Sueldo")
        for i in range(len(bajo)):
            print(bajo[i][1]+" "*(30-len(bajo[i][1]))+"$"+str(bajo[i][0]))
        print(" ")
    print("Sueldos entre $800.000 y $2.000.000 TOTAL: "+str(len(medio)))
    print(" ")
    if len(medio) == 0:
        None
    else:
        print("Nombre empleado"+" "*15+"Sueldo")
        for i in range(len(medio)):
            print(medio[i][1]+" "*(30-len(medio[i][1]))+"$"+str(medio[i][0]))
    print(" ") 
    print("Sueldos superiores a $2.000.000 TOTAL: "+str(len(alto)))
    print(" ")
    if len(alto) == 0:
        None
    else:
        print("Nombre empleado"+" "*15+"Sueldo")
        for i in range(len(alto)):
            print(alto[i][1]+" "*(30-len(alto[i][1]))+"$"+str(alto[i][0]))
    return print(" ")

def estadisticas(sueldos):
    print(" ")
    mas_alto = 0
    for i in range(len(sueldos)):
        if sueldos[i] >= mas_alto:
            mas_alto = sueldos[i]
    print("Sueldo más alto: $"+str(mas_alto))
    mas_bajo = 2500000
    for i in range(len(sueldos)):
        if sueldos[i] < mas_bajo:
            mas_bajo = sueldos[i]
    print("Sueldo más bajo: $"+str(mas_bajo))
    print("Promedio de sueldos: $"+str(statistics.median(sueldos)))
    print("Media geométrica: $"+str(round(statistics.geometric_mean(sueldos))))
    return print(" ")

def reporte(sueldos,trabajadores):
    print(" ")
    descuentos_salud = []
    descuentos_afp = []
    sueldos_liquidos = []
    for i in range(10):
        descuentos_salud.append(round(sueldos[i]*0.07))
        descuentos_afp.append(round(sueldos[i]*0.12))
        sueldos_liquidos.append((sueldos[i]-descuentos_afp[i])-descuentos_salud[i])
    excel = [["Nombre empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Líquido"]]
    for i in range(10):
        excel.append([trabajadores[i],sueldos[i],descuentos_salud[i],descuentos_afp[i],sueldos_liquidos[i]])
    for i in range(len(excel)):
        if i == 0:
            print(str(excel[i][0])+" "*(25-len(str(excel[i][0])))+str(excel[i][1])+" "*(25-len(str(excel[i][1])))+str(excel[i][2])+" "*(25-len(str(excel[i][2])))+str(excel[i][3])+" "*(25-len(str(excel[i][3])))+str(excel[i][4])+" "*(25-len(str(excel[i][4]))))
        else:
            print(str(excel[i][0])+" "*(25-len(str(excel[i][0])))+"$"+str(excel[i][1])+" "*(24-len(str(excel[i][1])))+"$"+str(excel[i][2])+" "*(24-len(str(excel[i][2])))+"$"+str(excel[i][3])+" "*(24-len(str(excel[i][3])))+"$"+str(excel[i][4])+" "*(24-len(str(excel[i][4]))))
    with open("reporte.csv","w",newline="",encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerows(excel)
    return print(" ")



def salir():
    print(" ")
    print("Finalizando programa...")
    print("Desarrollado por Salomón Moreno")
    print("RUT 21.773.160-7")
    return

def menu():
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    return

trabajadores = ["Juan Pérez","Maria García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]