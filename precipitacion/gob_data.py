#Lista principal
import xlrd
from Array3D import Array3D
estados=[]
meses=range(1,13)
años=range(1985,2020)
#registros:
estado={"id":0,
        "nombre":"", 
        "años_precip":[]
        }
registro_año={
    "año":0,
    "meses":[]
}
registro_mes={
    "mes":0,
    "valor":0.0
}
class data:
    def __init__(self,anio,mes,estado):
        self._cuadro=Array3D(anio,mes,estado)
        self.__registro_año=anio
        self.__registro_mes=mes
        self.__estado=estado
        
        

def init_data():
    #self.__cuadro.to_string()
    print(estado)
    print(años)

def buscar():#pone todo en limpio, y asignara el valor que le asignemos
        for anio in range(1985,2019,1):
            archivo=xlrd.open_workbook(filename="./Precipitacion/"+str(anio)+'Precip.xls')
            hoja=archivo.sheet_by_index(0)
            for i in range(2,34):
                for j in range(1,13):
                    contenido_celda = anio.cell_value(i,j)
    print("anio: \"" + str(contenido_celda) + "\"")
            



