#DEPARTAMENTO DE INFORMÁTICA DEL AYUNTAMIENTO DE ARANDA DE DUERO
#Código desarrollado por: Javier Montes de Blas

#Librerías
from matplotlib import pyplot as plt
import controlador

#Este método es el primero en ser ejecutado en caso de haver elegido la opción cin interfaz y contiene el flujo de ejecución principal de todo programa
def con_interfaz():
    print("Por favor seleccione el archivo csv que contiene las lecturas: ")
    lista, alerta=controlador.leer_archivo()
    if len(lista)>0:
        if alerta:
            print("Algunos registros erróneos han sido ignorados, los datos útiles no deberían haber sido afectados.")
        else:
            print("Carga de datos completada con éxito.")
        menu(lista)
    else:
        print("No se ha podido interpretar ningún registro")
        print("Para terminar la ejecución del programa pulse la tecla 'Enter'",end = "")
        controlador.salir()
    
# Este método contiene el bucle que permite la interacción con el menú y cada una de sus funciones asociadas, ejecutándos en bucle hasta que el usuario decida terminar usando la sentencia 0
def menu(lista):
    while True:
        menu_interface()
        opcion = input().upper()
        print()
        match opcion:
            case "1":
                consulta_parametrizada(lista)
            case "2":
                consulta_consumo_total_rango_años(lista)
            case "H":
                help()
            case "0":
                print("Fin de la ejecución")
                controlador.salir()
            case _:
                print("Opción deseada no recogida dentro de las implementadas, cuando el menú vuelva a mostrarse pulse 'H' seguido de la tecla 'Enter' para acceder al texto de ayuda")
        print()

# Este método está encargado de mostrar el apartado visual del menú
def menu_interface():
    print("*************************************************************************************************************")
    print("------Analizador de registros de Aguas (Contadores)------")
    print(" 1 - Consulta y estadísticas parametrizadas")
    print(" 2 - Consultar por consumo total en rango de años")
    print(" H - Ayuda")
    print(" 0 - Salir")
    print("Opción elegida:", end=" ")

#Este método muestra en forma de gráfica los parámetros dados
def graf(lista_val, cont1, cont2, cont3):
    fig, ax = plt.subplots()
    ax.grid()
    ax.grid(which="minor", color="0.5")
    ax.bar(['Registros totales', 'Registros' + '\n' + 'en el rango de' + '\n' + 'años', 'Registros en' + '\n' + 'el rango de años' + '\n' + 'y trimestres', 'Registros resultado'], [cont1, cont2, cont3, len(lista_val)], width=0.5, color=['tab:brown', 'tab:red', 'tab:orange', 'tab:olive'])
    ax.set_title("Representación gráfica de la consulta")
    ax.set_ylabel('Cantidad')
    print("Cierre la gráfica para continuar")
    plt.show()

# Este método se encarga de la inserción de datos necesaria para que se ejecute el método consulta_parametrizada de la clase controlador.py de forma adecuada.
def consulta_parametrizada(lista):
        try:
            print("Elige de que trimestre/es quieres los datos (Valores leídos: 1, 2, 3, 4):", end=" ")
            peri = str(input()).upper()
            print("Elige los límites del rango de años de los registros que se van a mostrar (En el rango se incluyen tanto el año comienzo como el año final) (El año comienzo debe ser menor o igual al año final)")
            print("-Comienzo del rango (ejem: 2016):", end=" ")
            anno_com = int(input())
            print("-Final del rango (ejem: 2018):", end=" ")
            anno_fin = int(input())
            if(anno_fin<anno_com):
                raise ValueError
            print("Elige los límites del rango de consumo de los registros que se van a mostrar (En el rango se incluyen tanto el valor comienzo como el valor final) (El valor comienzo debe ser menor o igual al valor final)")
            print("-Comienzo del rango (ejem: 0):", end=" ")
            cons_min = int(input())
            print("-Final del rango (ejem: 100):", end=" ")
            cons_max = int(input())
            if(cons_max<cons_min):
                raise ValueError
            lista_val,cont1,cont2,cont3=controlador.consulta_parametrizada(peri, anno_com, anno_fin, cons_min, cons_max, lista)
            if(len(lista_val)==0):
                print()
                print(f"No hay ningún registro existente bajo los parámetros escogidos.")
            else:
                print()
                for reg in lista_val:
                    print(reg.to_string())
                mostrar_res_cp(lista_val, cont1, cont2, cont3)
                print("Para continuar pulse la tecla 'Enter', para ver la gráfica escriba 'G' y pulse 'Enter':",end = " ")
                graf=input()
                if(graf.upper()=='G'):
                    graf(lista_val, cont1, cont2, cont3)
        except(ValueError):
            print()
            print("El valor insertado no cumple con los requisitos solicitados, vuelva a intentarlo")

# Muestra al usuario los resultados de la ejecución del método consulta_parametrizada().

def mostrar_res_cp(lista_val, cont1, cont2, cont3):
    print()
    print(f"El porcentaje de registros que cumplen estos requisitos es el {(len(lista_val)/cont1)*100}% de {cont1} registros totales. ({int((len(lista_val)/cont1)*cont1)} registros)")
    print(f"El porcentaje de registros en el rango de años especificado (Los cuales son el {(cont2/cont1)*100}% del total) que cumplen los requisitos es el {(len(lista_val)/cont2)*100}% de {cont2}.")
    print(f"El porcentaje de registros en el rango de años y trimestres especificados (Los cuales son el {(cont3/cont1)*100}% del total) que cumplen los requisitos de consumo es el {(len(lista_val)/cont3)*100}% de {cont3}.")
    print()

# Este método está encargado de mostrar información de ayuda destinada a resolver las dudas que pueda tener el usuario respecto a la ejecucuión del programa
def help():
    print("----Documentación de Ayuda----")
    print(" --Ayuda de Menú--")
    print("Para usar el menú, primero fíjese en los números que se encuentran delante de cada una de las opciones. Se puede acceder a cada una de ellas escribiendo el numero correspondiente en la zona indicada del menú. Si se escribe cualquier sentencia que no esté recogida entre las permitidas, saltará un mensaje informando de esto y ofreciendo ayuda sobre como llegar a esta información.")
    print(" --Ayuda de Consulta Parametrizada--")
    print("Esta opción permite la visualización de información relacionada con los registros que coincidan con una serie de parámetros establecidos por el usuario. Explicaremos estos parámetros uno a uno a continuación:")
    print("- Trimestre: Permite al usuario elegir entre el primer, segundo, tercer y cuarto trimestre o periodo. Si un registro tiene su fecha de lectura dentro del trimestre seleccionado por el usuario, este se incluirá en la consulta. Se pueden elegir varios trimestres concatenándolos de cualquier forma, por ejemplo '1,2,3,4', '1-2-3-4', '1 2 3 4' y '1234' serían ejemplos completamente válidos para elegir todo el año.")
    print("- Años: Indican los límites del rango de años que se van a tener en cuenta en la consulta. Si un registro tiene su fecha de lectura dentro del rango de años elegido, este registro formará parte de la consulta. Cualquiera de los años solo tiene como única restricción ser un número, y, en caso del año final, ser mayor o igual al de comienzo.")
    print("- Consumo: Indican los límites del rango de gasto contado que se va a tener en cuenta en la consulta. Si un registro tiene su consumo dentro del rango de consumo elegido, este registro formará parte de la consulta. Cualquiera de los valores de consumo tienen como única restricción ser un número, y, en caso del valor de consumo final, ser mayor o igual que el de comienzo.")
    print("Al ejecutar este proceso con éxito se nos devolverán y mostrarán todos los registros que cumplan con los requisitos de nuestra consulta encabezados por el 'número' o 'código' de abonado. Además de esto se nos mostrarán una serie de estadísticas informativas y porcentajes basados en la consulta realizada. Si deseamos ver una gráafica basada en la consulta simplemente debemos de escibir 'G' antes de darle a 'Enter'.")
    print(" --Ayuda de Consulta por Consumo Total--")
    print("Esta opción permite ver que contadores han tenido su consumo total dentro del rango de consumo especificado al terminar el rango de años especificado. Los parametros a introducir son estos:")
    print("- Años: Indican los límites del rango de años que se van a tener en cuenta en la consulta. Si un contador tiene una lectura al comienzo y al final del rango de años elegido, estas se usaran para sacar la diferencia de los valores de lectura. Cualquiera de los años solo tiene como única restricción ser un número, y, en caso del año final, ser mayor o igual al de comienzo.")
    print("- Consumo: Indican los límites del rango de gasto contado que se va a tener en cuenta en la consulta. Si un contador tiene su consumo total del rango de años dentro del rango de consumo elegido, este registro formará parte de la consulta. Cualquiera de los valores de consumo tienen como única restricción ser un número, y, en caso del valor de consumo final, ser mayor o igual que el de comienzo.")
    print("Al ejecutar este proceso con éxito se nos devolverán y mostrarán todos los códigos de los contadores que cumplan con los requisitos de nuestra consulta. Además de esto se nos mostrará el porcentaje de contadores correctamente registrados que cumplen la consulta realizada y tanto el número de contadores mal registrados en el rango como a que números de abonado están vinculados.")
    print()
    print("Para salir del menu de ayuda pulse la tecla 'Enter'",end = "")
    input()

# Este método se encarga de la inserción de datos necesaria para que se ejecute el método consulta_consumo de la clase controlador.py de forma adecuada.
def consulta_consumo_total_rango_años (lista):
    print("Elige los límites del rango de años de los registros que se van a mostrar (En el rango se incluyen tanto el año comienzo como el año final) (El año comienzo debe ser menor o igual al año final)")
    print("-Comienzo del rango (ejem: 2016):", end=" ")
    anno_com = int(input())
    print("-Final del rango (ejem: 2018):", end=" ")
    anno_fin = int(input())  
    if(anno_fin<anno_com):
        raise ValueError
    print("Elige los límites del rango de consumo total en el rango de años de los registros que se van a mostrar (En el rango se incluyen tanto el valor comienzo como el valor final) (El valor comienzo debe ser menor o igual al valor final)")
    print("-Comienzo del rango (ejem: 0):", end=" ")
    cons_min = int(input())
    print("-Final del rango (ejem: 100):", end=" ")
    cons_max = int(input())
    if(cons_max<cons_min):
        raise ValueError
    lista_res, cont, lista_inc, cont_inc = controlador.consulta_consumo(anno_com, anno_fin, cons_min, cons_max, lista)
    mostrar_res_cct(lista_res, cont, lista_inc, cont_inc)
    print("Para continuar pulse la tecla 'Enter'",end = "")
    input()

# Muestra al usuario los resultados de la ejecución del método consulta_consumo_total_rango_años().
def mostrar_res_cct(lista_res, cont, lista_inc, cont_inc):
    print()
    try:
        print("Contadores que cumplen los requisitos:")
        for cnt in lista_res:
            print(f"{cnt},", end=" ")
        print()
        print()
        print(f"El porcentaje de los contadores que cumplen los requisitos de consumo en ese rango de años es el {(len(lista_res)/cont)*100}% (Solo se han tenido en cuenta los contadores correctamente identificados que han existido y sido registrados tanto al comienzo como al final del rango de años)")
        if len(lista_inc)>0:
            print()
            print(f"Se han hallado admás {cont_inc} incidencias (Contadores sin identificador) en este rango de años relacionadas con los siguientes códigos de abonado: ")
            for inc in lista_inc:
                print(f"{inc},", end=" ")
            print()
    except(ZeroDivisionError):
        print("ERROR: No hay contadores en el fichero que hayan existido durante la totalidad del rango de años")
        print()
    print()