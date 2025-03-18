# Análisis de aguas
<br/>
<p align="center"><img src="./icon.ico" alt="ERR"></p>

## Introducción
Este programa tiene como objetivo principal el servir como herramienta de ayuda a la hora de analizar volcados de la base de datos de revisiones de contadores en ficheros formato CSV. Este programa está desarrollado por Javier Montes como alumno en prácticas del Departamento de Informática del [Ayuntamiento de Aranda de Duero](https://www.arandadeduero.es/).
Este programa está adaptado para nuestros registros y campos propios, pero este aspecto debería ser facilmente modificable ajustando el método 'leer_archivo()' de la clase 'controlador.py' para que se ciña a las necesidades y sistema deseados.
## Setup
Una vez instalado el repositorio, accede a la carpeta que contiene todos los archivos Python (.py) y en esta abre una pantalla de PowerShell pulsando 'Shift'+'Click Derecho' y buscando la opción 'Abrir ventana de PowerShell aquí'. En la ventana de PowerShell abierta ejecuta los siguientes comandos para convertir los diferentes archivos en un solo ejecutable compatible con el sistema operativo de aquel que lo convierta:

<p align="left">
    python -m venv myenv<br/>
    .\myenv\Scripts\activate<br/>
    pip install -r .\requirements.txt<br/>
    pyinstaller --onefile --icon=icon.ico main.py
</p>

Una vez completado estos pasos tendremos disponible el archivo ejecutable dentro de una carpeta llamada 'dist', la cual se halla dentro de la carpeta del repositorio. Eres completamente libre de moverlo y renombrarlo siempre y cuando no alteres la extensión del archivo.
## Ejecución
Para ejecutar el programa hay dos formas principales, con o sin interfaz. Para ejecutar el programa con interfaz se puede hacer tanto desde la consola de comandos usando su ruta absoluta o relativa, o simplemente seleccionando con doble 'Click Izquierdo' el archivo ejecutable. Para ejecutarlo sin interfaz  es necesario hacerlo desde la consola de comandos usando cualquiera de sus rutas, segida del argumento '-i'. Para una explicación más elavorada revise el apartado 'Sin interfaz', el cual se hallará en algún punto a continuación.
### Con interfaz
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
    <h4>Documentación de Ayuda</h4>
    <b>--Ayuda de Menú--</b><br/>
    Para usar el menú, primero fíjese en los números que se encuentran delante de cada una de las opciones. Se puede acceder a cada una de ellas escribiendo el numero correspondiente en la zona indicada del menú. Si se escribe cualquier sentencia que no esté recogida entre las permitidas, saltará un mensaje informando de esto y ofreciendo ayuda sobre como llegar a esta información.<br/><br/>
    <b>--Ayuda de Consulta Parametrizada--</b><br/>
  Esta opción permite la visualización de información relacionada con los registros que coincidan con una serie de parámetros establecidos por el usuario. Explicaremos estos parámetros uno a uno a continuación:<br/>
    &nbsp;&nbsp;- Trimestre: Permite al usuario elegir entre el primer, segundo, tercer y cuarto trimestre o periodo. Si un registro tiene su fecha de lectura dentro del trimestre seleccionado por el usuario, este se incluirá en la consulta. Se pueden elegir varios trimestres concatenándolos de cualquier forma, por ejemplo '1,2,3,4', '1-2-3-4', '1 2 3 4' y '1234' serían ejemplos completamente válidos para elegir todo el año.<br/>
    &nbsp;&nbsp;- Años: Indican los límites del rango de años que se van a tener en cuenta en la consulta. Si un registro tiene su fecha de lectura dentro del rango de años elegido, este registro formará parte de la consulta Cualquiera de los años solo tiene como única restricción ser un número, y, en caso del año final, ser mayor o igual al de comienzo.<br/>
    &nbsp;&nbsp;- Consumo: Indican los límites del rango de gasto contado que se va a tener en cuenta en la consulta. Si un registro tiene su consumo dentro del rango de consumo elegido, este registro formará parte de la consulta Cualquiera de los valores de consumo tienen como única restricción ser un número, y, en caso del valor de consumo final, ser mayor o igual que el de comienzo.<br/>
    Al ejecutar este proceso con éxito se nos devolverán y mostrarán todos los registros que cumplan con los requisitos de nuestra consulta encabezados por el 'número' o 'código' de abonado. Además de esto se nos mostrarán una serie de estadísticas informativas y porcentajes basados en la consulta realizada. Si deseamos ver una gráfica basada en la consulta simplemente debemos de escibir 'G' antes de darle a 'Enter'.<br/><br/>
    <b>--Ayuda de Consulta por Consumo Total--</b><br/>
    Esta opción permite ver que contadores han tenido su consumo total dentro del rango de consumo especificado al terminar el rango de años especificado. Los parametros a introducir son estos: <br/>
    &nbsp;&nbsp;- Años: Indican los límites del rango de años que se van a tener en cuenta en la consulta. Si un contador tiene una lectura al comienzo y al final del rango de años elegido, estas se usaran para sacar la diferencia de los valores de lectura. Cualquiera de los años solo tiene como única restricción ser un número, y, en caso del año final, ser mayor o igual al de comienzo.<br/>
    &nbsp;&nbsp;- Consumo: Indican los límites del rango de gasto contado que se va a tener en cuenta en la consulta. Si un contador tiene su consumo total del rango de años dentro del rango de consumo elegido, este registro formará parte de la consulta. Cualquiera de los valores de consumo tienen como única restricción ser un número, y, en caso del valor de consumo final, ser mayor o igual que el de comienzo. <br/>
    Al ejecutar este proceso con éxito se nos devolverán y mostrarán todos los códigos de los contadores que cumplan con los requisitos de nuestra consulta. Además de esto se nos mostrará el porcentaje de contadores correctamente registrados que cumplen la consulta realizada y tanto el número de contadores mal registrados en el rango como a que números de abonado están vinculados. <br/>
</p>

### Sin interfaz
Si deseas ver los argumentos a tu disposición despúes de la ruta del ejecutable escribe el argumento '-h':

<p align="left">
    .\main.exe -h
</p>

Este comando abrirá una descripción corta del programa y de cada argumento, además de un esquema de su uso. De todas formas a continuación habrá una lista de ejemplos de comandos para ejecutar el programa sin interfaz correctamente formados, seguida una explicación corta de cada argumento.

<p align="left">
    .\main.exe -i -o 1 -p 1 -a 2013 2015 -c 0 40<br/>
    .\main.exe -i -o 1 -p 2 3 -a 2005 2010 -c 0 0 -g<br/>
    .\main.exe -i -o 1 -p 1 2 3 4 -a 2000 2012 -c 5 15<br/>
    .\main.exe -i -o 2 -a 2005 2010 -c 0 0<br/>
    .\main.exe -i -o 2 -a 2015 2020 -c 10 20<br/><br/>
    -i -> Si está presente el programa se ejecutará en el modo 'Sin interfaz'. En caso de no estar presente no se leerán el resto de argumentos.<br/>
    -o -> Su uso en caso de una ejecución sin interfaz es obligatorio, y solo puede tener los valores contemplados a continuación:<br/>
    &nbsp;&nbsp;&nbsp;1 -> Ejecuta una consulta parametrizada, para ver su funcionamiento suba al apartado de 'Documentación de Ayuda' subapartado 'Ayuda de Consulta Parametrizada'.<br/>
    &nbsp;&nbsp;&nbsp;2 -> Ejecuta una consulta por consumo total, para ver su funcionamiento suba al apartado de 'Documentación de Ayuda' subapartado 'Ayuda de Consulta Parametrizada'.<br/>
    -p -> Los periodos N que se tendrán en cuenta en la consulta, se debe usar este argumento en la consulta 1. Se pueden colocar después del argumento '-p' los periodos deseados separados por espacios.<br/>
    -a -> El rango de años que se tendrá en cuenta en la consulta, se debe usar en la consulta 1 y 2. Se deben colocar el año en el que comienze el rango y el año en el que termine separados por un espacio después del argumento '-a'.<br/>
    -c -> El rango de consumo que se tendrá en cuenta en la consulta, se debe usar en la consulta 1 y 2. Se deben colocar el consumo en el que comienze el rango y el consumo en el que termine separados por un espacio después del argumento '-c'.<br/>
    -g -> Si está presente, al terminar la consulta parametrizada aparecerá una gráfica con información vinculada a esta. Se puede usar este argumento en la consulta 1.
</p>
