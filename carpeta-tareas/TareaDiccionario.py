materia_Estructura={
                       'caracter':'obligatoria',
                       'clave':'0190',
                       'teoria':'4.0',
                       'practica':'0.0',
                       'horas':'64.0',
                       'creditos':'08',
                       'tipo':'teorica'
         


           ,'asignaturas':{
            'precedentes':['comp, y programacion',
                           'prog orientada a objetos',
                           'algebra',
                           'diseño y analisis de algoritmos'],
            'subsecuentes':['diseño y analisis de algoritmos',
                            'ingenieria de software i y ii',
                            'bases de datos I Y II',
                            'visualizacion',
                            'Estructuras discretas',
                            'programacion de sistemas',
                            'graficacion por computadora',
                            'reconocimiento de patrones',
                            'ingenieria artificial']}
                       ,'UNIDAD I':[{'1.1':'generalidades'},
                                        {'1.1.1':'almacenamiento'},
                                        {'1.1.2':'memoria primaria'},
                                        {'1.1.3':'Rep.num.enteros'}],
                                        '1.2':'rep num estandar',
                                        '1.3':'rep.caracteres',
                                        '1.4':'rep,arreglos',
                                        '1.5':'cardin.conjuntos'
                                        ,
                            'UNIDAD II':['2.1 gen',
                                         {'2.2 ordenamientos internos',
                                         '2.2.1 met.seleccion',
                                         '2.2.2 met.intercambio',
                                         '2.2.3 met.insercion',
                                         '2.2.4 met.distribucion',
                                         '2.2.5 met.intercalacion'},
                                         {'2.3 met.ord.externos',
                                         '2.3.1 met.polifase',
                                         '2.3.2 met.met.cascada',
                                         '2.3.3 met.oscilante',
                                         '2.3.4 met.distribucion'}],
                       'UNIDAD III':['3.1 Generalidades',
                                    {'3.2 pila',
                                     '3.2.1 def y operaciones',
                                     '3.2.2 instrum.clase pila'},
                                    {'3.3 cola',
                                     '3.3.1 def y operaciones',
                                     '3.3.2 instr.clase cola',
                                     '3.3.3  clase queue en Standar template library'},
                                    {'3.4 listas doblemente ligadas',
                                     '3.4.1 def y operaciones',
                                     '3.4.2 instrum.clase lista',
                                     '3.4.3 clase lst en la standar template library'},
                                    {'3.5 colecciones',
                                     '3.5.1 vectores',
                                     '3.5.2 mapas'}
                           ],
                       'UNIDAD IV':['4.1 generalidades',
                                    {'4.2 arboles',
                                     '4.2.1 conceptos y def'},
                                    {'4.3 arboles binarios',
                                     '4.3.1 cncep y def',
                                     '4.3.2 instrum de clase arbol binario'},
                                    {'4.4 arbol B y Arbol B+',
                                     '4.4.1 Concept y def',
                                     '4.4.2 instrum de clase Arbol B+'},
                                    {'4.5. grados',
                                     '4.5.1 concept y def',
                                     '4.5.2 instrum de claso Grafos'
                                        }

                           ],
                       'UNIDAD V':['5.1 Generalidades',
                                   '5.2 Def de operacion busqueda',
                                   {'5.3 busqueda.comparacion de llaves',
                                    '5.3.1 lineal',
                                    '5.3.2 binaria'},
                                   {'5.4 busqueda por transformacion de llaves',
                                    '5.4.1 funciones de has',
                                    '5.4.2 colisiones'}
                           ]
                       
                }
print(materia_Estructura)
#si quiero imprimir la tercera unidad
print("------solo tercera unidad-------")
print(materia_Estructura['UNIDAD III'])
print("-----solo unidad I y seccion 1.1.2")
print(materia_Estructura['UNIDAD I'][2])

