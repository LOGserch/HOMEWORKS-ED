import xlrd
class Array3D:
    def  __init__(self,depth, rows , cols):
        self.__data=[]
        self.__rows=rows
        self.__cols=cols
        self.__depth=depth
        for i in range(depth):
            tmp=[]
            for j in range(rows):
                tmp2=[]
                for k in range(cols):
                    tmp2.append(k)
                    tmp.append(tmp2)
                    self.__data.append(tmp)
    
    def get_num_rows(self):
            return self.__rows

    def get_num_cols(self):
           return self.__cols

    def get_num_depth(self):
           return self.__depth

    def set_item(self,r,c,d,value):
        self.__data[d][r][c]=value

    def get_item(r,c,a):
        return self.__data[a][r][c]

    def clearing(self,value):#pone todo en limpio, y asignara el valor que le asignemos
        for i in range(self.__depth):
            for j in range(self.__rows):
                for k in range(self.__cols):
                    self.__data[i][j][k]=value
                                                                        

    def to_string(self):
           print(self.__data)

    def lectura(self,depth,row,col):
        data=[]
        for anio in range(1985,2019):
            anio_lista=[]#lista para el anio
            archivo=xlrd.open_workbook(filename="./Precipitacion/"+str(anio)+'Precip.xls')
            hoja=archivo.sheet_by_index(0) 
            for estado in range(2,3,4):
                mes_lista=[]#lista para el mes
                for mes in range(1,13):
                    mes_lista.append("%.2f" % hoja.cell_value(estado,mes))
                anio_lista.append(mes_lista)
            data.append(anio_lista)
    #print(f"el promedio mensual es:{data[anio-1985][estado-1][mes-1]}")

        print(data)

        
"""
def main():
        Arreglo=Array3D(1,2,2)
        print("------primero--------")
        print("")
        Arreglo.to_string()
        Arreglo.clearing(1)
        print("------segundo--------")
        print("")
        Arreglo.to_string()
        Arreglo.set_item(1,2,2,3)
     
main()
"""
