from tkinter import filedialog
import csv
import registro

# Este método se encarga de la lectura del fichero csv y de la conversión de esta recopilación de registros a una lista de instancias del objeto registro.py, la cual es devuelta para su
# posterior uso. Este método también devuelve un valor booleano el cual es verdadero en caso de que haya sido necesario omitir parte del contenido del fichero para la correcta interpretación
# de los registros, seguramente si esto pasa se debe al uso de saltos de línea en los comentarios de los técnicos a la hora de hacer la revisión.
def leer_archivo():
    ruta = None

    while(not ruta):
        ruta = filedialog.askopenfilename()

    with open(ruta, 'r', encoding='utf-8') as fichero:
        lista=[]
        lineas = csv.reader(fichero)
        cabecera = True
        skipped=False
        for linea in lineas:
            if not cabecera:
                try:
                    reg=registro.Registro(linea[0], int(linea[1]), int(linea[2]), linea[3], int(linea[5]), int(linea[6]), int(linea[7]), linea[12])
                    lista.append(reg)
                except(IndexError,ValueError):
                    skipped=True
            else:
                cabecera=False
    return lista, skipped

# Este método se encarga de filtrar la lista de instancias de registro.py que se le pasa como parámetro usando los demás parámetros incluidos en este. Además de la lista filtrada, este
# método devuelve la cantidad de registros que cumplen cada condición individual elegida.
def consulta_parametrizada(peri, anno_com, anno_fin, cons_min, cons_max, lista):
    cont1=0
    cont2=0
    cont3=0
    lista_val = []
    for reg in lista: 
        cont1+=1
        if((reg.anno_lectura>=anno_com) and (reg.anno_lectura<=anno_fin)):
            cont2+=1
            if(peri.__contains__((str(reg.cod_periodo)))):
                cont3+=1
                if((reg.val_consumo>=cons_min) and (reg.val_consumo<=cons_max)):
                    lista_val.append(reg)
    return lista_val, cont1, cont2, cont3

def consulta_consumo(anno_com, anno_fin, cons_min, cons_max, lista):
    lista_ini = []
    lista_fin = []
    lista_res = []
    lista_inc = []
    cont = 0
    cont_inc = 0
    for reg in lista: 
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