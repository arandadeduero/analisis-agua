class RegistroLecturas:
    # Este método permite la creación de instancias de esta clase
    def __init__(self, cod_abonado, cod_periodo, anno_lectura, fecha_lectura, val_lectura, val_consumo, val_imputado, cod_contador, diam_contador, tipo_contador):
        self.cod_abonado = cod_abonado
        self.cod_periodo = cod_periodo
        self.anno_lectura = anno_lectura
        self.fecha_lectura = fecha_lectura
        self.val_lectura = val_lectura
        self.val_consumo = val_consumo
        self.val_imputado = val_imputado
        self.cod_contador = cod_contador
        self.diam_contador = diam_contador
        self.tipo_contador = tipo_contador

    # Este método devuelve una cadena de caracteres coherente que contiene toda la información relevante sobre la instancia de esta clase en la que se invoque
    def to_string(self):
        return (f" CA-{self.cod_abonado} -> Trimestre: {self.cod_periodo}, Año de Lectura: {self.anno_lectura}, Fecha de Lectura: {self.fecha_lectura}, " +
        f"Valor de Lectura: {self.val_lectura}, Consumo: {self.val_consumo}, Valor Imputado: {self.val_imputado}, Código de Contador: {self.cod_contador}, " + 
        f"Diámetro de Contador: {self.diam_contador}, Tipo de Tarifa: {self.tipo_contador};")