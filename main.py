import funciones
trabajadores = ["Juan Pérez","Maria García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
generado = False
while True:
        funciones.menu()
        try:
            opc = int(input("Ingresa opción: "))
            if opc == 1:
                generado = True
                sueldos = funciones.asignar()
            elif opc == 5:
                funciones.salir()
                break
            elif not generado:
                print("Error, no se han generado los sueldos aún")
            elif opc == 2:
                funciones.clasificar(sueldos,trabajadores)
            elif opc == 3:
                funciones.estadisticas(sueldos)
            elif opc == 4:
                funciones.reporte(sueldos,trabajadores)
            else: 
                raise ValueError
        except:
            print("Error")