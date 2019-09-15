class Array2D:
    def __init__(self,rows,cols):#self solo es una variable instancial
        self.__data=[]#instanciamos una cadena
                               
        for row in range(rows):
            tmp=[]                                      
                          #declaramos una cadena vacia
            for cols in range(cols):
                #append(),para meter valores a una lista
                tmp.append(None)#asignamos un valor none a la cadena vacia
            self.__data.append(tmp)

    def to_string(self):
      print(self.__data)

    def get_num_rows(self):
        return self.__row

    def get_num_cols(self):        
         return self.__cols

    def clearing(self,value):
        for row in range(self.__row):
            for col in range((self.__cols):
                self.__data[row][cols]=value

    def set_item(self,r,c,1):
        if (r >=0 and r<self.__row) and (c >=0 and c<self.__col)
             self.__data[r][c]=valor               
                            
        

def main():
    Arreglo=Array2D(5,5)
    Arreglo.to_string()
    print(f"el valor de los renglones es: {Arreglo.get_num_row()}")
    print(f"el valor de las columnas es: {Arreglo.get_num_cols()}")

main()
"""
                                   en este primer for,obtenemos un valor inicial
                                    desde el comstructor, hasta el rango del valor
                                    de la primer variable
                                    """
"""
                                                    para el segundo for,se utiliza el segundo
                                                   argumento obtenido desde el constructor,
                                                  hasta el rango de el argumento mismo
                                                  """
"""
                                al finalizar el segundo for en evaluar,
                                el primer for utiliza append para asignar
                                la cadena obtenida tmp, a la cadena principal
                                   """

                
