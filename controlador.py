from datetime import date, datetime
import subprocess
from tkinter import filedialog
import csv
import registro_lecturas

# Este método se encarga de la lectura del fichero csv y de la conversión de esta recopilación de registros a una lista de instancias del objeto registro.py, la cual es devuelta para su
# posterior uso. Este método también devuelve un valor booleano el cual es verdadero en caso de que haya sido necesario omitir parte del contenido del fichero para la correcta interpretación
# de los registros, seguramente si esto pasa se debe al uso de saltos de línea en los comentarios de los técnicos a la hora de hacer la revisión.
def leer_archivo_lecturas():
    ruta = None
    ruta = filedialog.askopenfilename()
    if(not ruta):
        salir()
    else:
        with open(ruta, 'r', encoding='utf-8') as fichero:
            lista_l=[]
            lineas = csv.reader(fichero)
            cabecera = True
            skipped=False
            for linea in lineas:
                if not cabecera:
                    try:
                        reg=registro_lecturas.RegistroLecturas(linea[0], int(linea[1]), int(linea[2]), linea[3], int(linea[5]), int(linea[6]), int(linea[7]), linea[12], int(linea[24]), linea[26])
                        lista_l.append(reg)
                    except(IndexError,ValueError):
                        skipped=True
                else:
                    cabecera=False
        return lista_l, skipped

def leer_archivo_contadores():
    ruta = None
    ruta = filedialog.askopenfilename()
    if(not ruta):
        salir()
    else:
        with open(ruta, 'r', encoding='utf-8') as fichero:
            lista_c=[]
            lineas = csv.reader(fichero)
            cabecera = True
            skipped=False
            for linea in lineas:
                if not cabecera:
                    try:
                        reg=""
                        #reg=registro_contadores.RegistroContadoress(linea[n], linea[n1], int(linea[n2]))
                        lista_c.append(reg)
                    except(IndexError,ValueError):
                        skipped=True
                else:
                    cabecera=False
        return lista_c, skipped

# Este método se encarga de filtrar la lista de instancias de registro.py que se le pasa como parámetro usando los demás parámetros incluidos en este para devolver solo aquellos que concuerden
# o estén contenidos dentro de los diferentes valores y rangos establecidos en estos. Además de la lista filtrada, este método devuelve la cantidad de registros que cumplen cada condición individual elegida.
def consulta_parametrizada(peri, anno_com, anno_fin, cons_min, cons_max, lista_l):
    cont1=0
    cont2=0
    cont3=0
    lista_val = []
    for reg in lista_l: 
        cont1+=1
        if((reg.anno_lectura>=anno_com) and (reg.anno_lectura<=anno_fin)):
            cont2+=1
            if(peri.__contains__((str(reg.cod_periodo)))):
                cont3+=1
                if((reg.val_consumo>=cons_min) and (reg.val_consumo<=cons_max)):
                    lista_val.append(reg)
    return lista_val, cont1, cont2, cont3

# Este método se encarga de filtrar la lista de instancias de registro.py que se le pasa como parámetro usando los demás parámetros incluidos en este para devolver que contadores han consumido 
# una cantidad total dentro del rango de consumo durante todo el rango de años. Además de la lista filtrada, este método devuelve el contador de incidencias junto a la lista de los códigos 
# de abonado a los que están vinculadas y el número de contadores correctamente identificados que existieron durante la extensión completa del rango de años.
def consulta_consumo(anno_com, anno_fin, cons_min, cons_max, lista_l):
    lista_ini = []
    lista_fin = []
    lista_res = []
    lista_inc = []
    cont = 0
    cont_inc = 0
    for reg in lista_l: 
        if((int(reg.anno_lectura)==anno_com-1) and (int(reg.cod_periodo)==4)):
            lista_ini.append(reg)
        if((int(reg.anno_lectura)==anno_fin) and (int(reg.cod_periodo)==4)):
            lista_fin.append(reg)
    for reg_fin in lista_fin:
        if (reg_fin.cod_contador!="0"):
            for reg_ini in lista_ini:
                if (reg_fin.cod_contador == reg_ini.cod_contador):
                    cons=reg_fin.val_lectura-reg_ini.val_lectura
                    cont += 1
                    if ((cons >= cons_min) and (cons <= cons_max)):
                        lista_res.append(reg_fin.cod_contador)
        else:
            cont_inc += 1
            if not lista_inc.__contains__(reg_fin.cod_abonado):
                lista_inc.append(reg_fin.cod_abonado)
    return lista_res, cont, lista_inc, cont_inc

#
def consulta_contador(anno_com, anno_fin, cod, lista_l):
    list_res = []
    cons_total = 0
    for reg in lista_l:
        if((reg.cod_contador == cod) and (int(reg.anno_lectura)>=anno_com) and (int(reg.anno_lectura)<=anno_fin)):
            list_res.append(reg)
            cons_total += int(reg.val_consumo)
    list_res = sorted(list_res, key=lambda registro_lecturas:registro_lecturas.cod_periodo)
    list_res = sorted(list_res, key=lambda registro_lecturas:registro_lecturas.anno_lectura)
    if(len(list_res)>0):
        return list_res, cons_total
    
#
def buscar_tipo_diam(lista_l, cod):
    tipo = ""
    diam = 0
    for reg in lista_l:
        if((reg.cod_contador == cod)):
            tipo = reg.tipo_contador
            diam = reg.diam_contador
    return tipo, diam


def salir():
    exit()
    subprocess.call("cmd.exe /C exit", shell=True)