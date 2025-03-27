#DEPARTAMENTO DE INFORMÁTICA DEL AYUNTAMIENTO DE ARANDA DE DUERO
#Código desarrollado por: Javier Montes de Blas

#Librerías
import controlador
import interfaz
import argparse

#Este método es el primero en ser ejecutado y contiene el flujo de ejecución principal de todo programa
def main():
    parser = argparse.ArgumentParser(description="Permite el análisis de contadores de agua en base a un archivo csv")
    parser.add_argument('-i', '--interfaz', action="store_false", help="El programa se ejecutará sin interfaz gráfica, lo que hace que el resto de argumentos se vuelven relevantes.")
    parser.add_argument('-o', '--opcion', metavar="N", choices=['1','2','3'], help="Elegirá que tipo de consulta realizar si se ejecuta sin interfaz, consultar dudas en el README.txt.")
    parser.add_argument('-p', '--periodo', nargs='+', metavar="N", help="Los periodos N que se tendrán en cuenta en la consulta, se usan en la consulta 1.")
    parser.add_argument('-cod', '--codigo', metavar="N", help="El contador del que se realizará la consulta, se usa en la consulta 3")
    parser.add_argument('-a', '--años', metavar="N", nargs=2, type=int, help="El rango de años que se tendrá en cuenta en la consulta, se usa en la consulta 1, 2 y 3.")
    parser.add_argument('-con', '--consumo', metavar="N", nargs=2, type=int, help="El rango de consumo que se tendrá en cuenta en la consulta, se usa en la consulta 1 y 2.")
    parser.add_argument('-g', '--grafica', action="store_true", help="El programa mostrará una gráfica con los resultados, se usa en la consulta 1 y 3.")
    arguments = parser.parse_args()
    if(arguments.interfaz):
        interfaz.con_interfaz()
    else: 
        lista_l, b = controlador.leer_archivo_lecturas()
        if(arguments.opcion=='1'):
            if(not arguments.años or not arguments.consumo):
                print("El valor años (-a) y el valor consumo (-c) son obligatorios en la consulta 1 y 2.")
                print()
                controlador.salir()
            if(arguments.periodo):
                lista_val, cont1, cont2, cont3 = controlador.consulta_parametrizada(arguments.periodo, arguments.años[0], arguments.años[1], arguments.consumo[0], arguments.consumo[1], lista_l)
                interfaz.mostrar_res_c_par(lista_val, cont1, cont2, cont3)
                if(arguments.grafica):
                    interfaz.grafica_cons1(lista_val, cont1, cont2, cont3)
            else:
                print("El valor periodo es obligatorio en la consulta 1.")
                print()
        elif(arguments.opcion=='2'):
            if(not arguments.años or not arguments.consumo):
                print("El valor años (-a) y el valor consumo (-c) son obligatorios en la consulta 1 y 2.")
                print()
                controlador.salir()
            lista_res, cont, lista_inc, cont_inc = controlador.consulta_consumo(arguments.años[0], arguments.años[1], arguments.consumo[0], arguments.consumo[1], lista_l)
            interfaz.mostrar_res_c_cons(lista_res, cont, lista_inc, cont_inc)
        elif(arguments.opcion=='3'):
            if(not arguments.años):
                print("El valor años (-a) es obligatorio en la consulta 3.")
                print()
                controlador.salir()
            else:
                lista_res, cons_total = controlador.consulta_contador(arguments.años[0], arguments.años[1], arguments.codigo, lista_l)
                tipo, diam = controlador.buscar_tipo_diam(lista_l, arguments.codigo)
                interfaz.mostrar_res_c_cont(lista_res, cons_total, tipo, diam)
                if(arguments.grafica):
                    interfaz.grafica_cons2(lista_res)
        elif(not arguments.opcion):
            print("El valor opción (-o) es obligatorio en caso de no usar la interfaz.")
            print()
        print("Para terminar pulse la tecla 'Enter'",end = "")
        input()
    controlador.salir()

# Disparador que ejecuta el método main al iniciar el programa
if __name__=="__main__":
    main()