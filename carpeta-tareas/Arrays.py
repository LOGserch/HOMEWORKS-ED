#Array es ADT(es un tipo de dato abstracto) que almacena elementos con indice:
#operaciones de Array:
#Array()--constructor
#get_length()--tamaño
#get_item(index)--elem
#set_item(index,v)
#clearing(varol)
class Array:
    
    def __init__(self,n):#self es referencia a la propia clase
        self.__data=[]
        for i in range(n):
            self.__data.append(None)

    def get_length(self):
       return len(self.__data)

    def set_item(self , index , value ):
      if index >=0 and index < len(self.__data):
        self.__data[index]=value
      else:
          print("fuera de rango")

    def get_item(self,index):
        if index >=0 and index < len(self.__data):
         return self.__data[index]
        else:
          print("fuera de rango")
        
    def clearing(self,valor):
        for index in range(len(self.__data)):
          self.__data[index]=valor
        
    def to_string(self):
        print(self.__data)
#main
def main():
  arreglo = Array(10)
  arreglo.to_string()
  print(f"el tamaño es de {arreglo.get_length()}")
  arreglo.set_item(1,10)
  arreglo.to_string()
  arreglo.set_item(12,10)
  print(f"el elemento 1 es{arreglo.get_item(1)}")
  arreglo.get_item(20)
  arreglo.clearing(5)
  arreglo.to_string()

  main()
  #get_nun_roses()regresa tamaño de filas
  #get_num_cols()regresa tamaño de columnas
  #get_item(v,c)va a regresar valores
  #sel_item(r,c,value)va a sobrescribir valores
