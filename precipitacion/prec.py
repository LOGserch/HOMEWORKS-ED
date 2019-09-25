#pip (o pip 3) ->pip install xird
#python instalation program
#import xlrd
for anio in range(1985,2020,1):
    #print(anio)
    path = "./Precipitacion/"+str(anio)+"Precip.xls"#str(),para convertirlo a string
    print(path)
    archivo = xlrd.open_workbook(filename = path)
    hoja = archivo.sheet_by_index(0)
    #aguascalientes, enero de todos los años
    print(hola.cell_value(2,1))
