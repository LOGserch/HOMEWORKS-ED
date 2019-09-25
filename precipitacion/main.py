import xlrd
from Array3D import Array3D
#main
def main():
    estado=int(input('Que estado(1-32)?:'))
    anio=int(input("año(1985-2019)?:"))
    mes=int(input("mes(1-12)?:"))
    lectura_excel=Array3D(anio,mes,estado)
    lectura_excel.lectura(anio,mes,estado)

main()
