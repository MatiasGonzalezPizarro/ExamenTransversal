import numpy as np
import datetime as dt
def menu():
    while True:
     print("Concierto Michael Jam")
     print("1)Comprar Entrada \n2)Mostrar Ubicaciones Disponibles \n3)Ver Listado de asistentes \n4)Mostrar Ganancias totales \n5)Salir")
def imprimirArreglo(arreglo):
   print(arreglo)
def validaOpc(tipo,texto,min,max):
    while True:
        try:
            nro=tipo(input(texto))
            if min!=None and max!=None:
               if min<=nro<=max: 
                 break
               else:
                print("Fuera de rango")
            elif min!=None:
               if min<=nro:
                  break
               else:
                  print("Opcion Invalida")
            elif max!=None:
               if nro<=max:
                  break
               else:
                  print("Opcion Invalida")
            else:
               break
        except:
           print("Tiene que ser un numero")
    return nro                                                  
def comprarAsiento(arreglo,num,run,lista1,lista2,lista3,lista4):
   asiento=False
   entradas=0
   for f in range(10):
      for c in range(10):
          if arreglo[f,c]==num:
            arreglo[f,c]='X'
            lista1.append(num)
            if num>=1 and num<=20:
               lista2.append(120000)
               asiento=True
               lista3.append(run)
               lista4.append("Platinum")
               entradas=entradas+1
               break
            elif num>=21 and num<=50:
               lista2.append(80000)
               asiento=True
               lista3.append(run)
               lista4.append("Gold")
               entradas=entradas+1
               break
            elif num>=51 and num<=100:
               lista2.append(50000)
               asiento=True
               lista3.append(run)
               lista4.append("Silver")
               entradas=entradas+1
               break      
          if asiento:
            break
   if not asiento:
    print("--->Asiento No disponible<---")    
   return (arreglo,lista1,lista2,entradas)
def imprimirGanancias(lista1,lista2,lista3):
   for i in range(len(lista1)):
      if len(lista1)>=1:
         print(f"Categoria:{lista1[i]}|Ubicacion:{lista2[i]}|Pagado:{lista3[i]}")
      if len(lista1)==0:
         print("No hay asistentes")
def imprimirAsistentes(lista1):
   lista1.sort()
   for i in range(len(lista1)):
    print(f"Rut:{lista1[i]}")         
def despedida():
   print(f"Adios \nMatias Gonzalez Pizarro ")       