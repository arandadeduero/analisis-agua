# Análisis de aguas
<p align="center"><img src="./icon.ico" alt="ERR"></p>

## Introducción
Este programa tiene como objetivo principal el servir como herramienta de ayuda a la hora de analizar volcados de la base de datos de revisiones de contadores en ficheros formato CSV. Este programa está desarrollado por Javier Montes como empleado en prácticas del [Ayuntamiento de Aranda de Duero](https://www.arandadeduero.es/).
Este programa está adaptado para nuestros registros y campos propios, pero este aspecto debería ser facilmente modificable ajustando el método 'leer_archivo()' de la clase 'controlador.py' para que se ciña a las necesidades y sistema deseados.
## Funcionamiento
Lo primero que te pedirá el programa a la hora de ejecutarlo es que selecciones el archivo CSV que contiene las lecturas que se deseen analizar, no se podrá avanzar en la ejecución del programa sin cumplir este paso. Si se cierra el diálogo de selección el programa terminará su ejecución de inmediato. En caso de seleccionar un CSV parcialmente erróneo el programa nos avisará de la posible pérdida de datos al no haber podido interpretar algunos registros. Si la interpretación de las lecturas es correcta o solo parcialmente errónea el programá procederá a mostrarnos este menú:

<p align="left">
    <b>------Analizador de registros de Aguas (Contadores)------</b> <br/>
     1 - Consulta y estadísticas parametrizadas <br/>
     2 - Consultar por consumo total en rango de años <br/>
     3 - No implementado <br/>
     H - Ayuda <br/>
     0 - Salir <br/>
    Opción elegida:
</p>

Una vez se nos ha mostrado el menú, para elegir la opción deseada solo debemos escribir a la derecha de donde se halla el texto 'Opción elegida: ' el número o caracter que corresponda a la acción que deseemos realizar y pulsar la tecla 'Enter' o 'Intro'. Para una primera ejecución recomendamos el seleccionar la opción de 'Ayuda' escribiendo el caracter 'H' y pulsando 'Enter', lo que nos llevará a una guía escrita de cada uno de los apartados del programa. También puede leerla a continuación:

<p align="left">
  <strong>----Documentación de Ayuda----</strong><br/>
   <b>--Ayuda de Menú--</b><br/>
  Para usar el menú, primero fíjese en los números que se encuentran delante de cada una de las opciones. Se puede acceder a cada una de ellas escribiendo el numero correspondiente en la zona indicada del menú. Si se escribe cualquier sentencia que no esté recogida entre las permitidas, saltará un mensaje informando de esto y ofreciendo ayuda sobre como llegar a esta información.<br/>
  <b>--Ayuda de Consulta Parametrizada--</b><br/>
  Esta opción permite la visualización de información relacionada con los registros que coincidan con una serie de parámetros establecidos por el usuario. Explicaremos estos parámetros uno a uno a continuación:<br/>
  - Trimestre: Permite al usuario elegir entre el primer, segundo, tercer y cuarto trimestre o periodo. Si un registro tiene su fecha de lectura dentro del trimestre seleccionado por el usuario, este se incluirá en la consulta. Se pueden elegir varios trimestres concatenándolos de cualquier forma, por ejemplo '1,2,3,4', '1-2-3-4', '1 2 3 4' y '1234' serían ejemplos completamente válidos para elegir todo el año.<br/>
  - Años: Indican los límites del rango de años que se van a tener en cuenta en la consulta. Si un registro tiene su fecha de lectura dentro del rango de años elegido, este registro formará parte de esta. Cualquiera de los años solo tiene como única restricción ser un número, y, en caso del año final, ser mayor o igual al de comienzo.<br/>
  - Consumo: Indican los límites del rango de gasto contado que se va a tener en cuenta en la consulta. Si un registro tiene su consumo dentro del rango de consumo elegido, este registro formará parte de esta. Cualquiera de los valores de consumo tienen como única restricción ser un número, y, en caso del valor de consumo final, ser mayor o igual que el de comienzo.<br/>
  Al ejecutar este proceso con éxito se nos devolverán y mostrarán todos los registros que cumplan con los requisitos de nuestra consulta encabezados por el 'número' o 'código' de abonado. Además de esto se nos mostrarán una serie de estadísticas informativas y porcentajes basados en la consulta realizada.
</p>
