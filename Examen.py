import funcionesExamen as fn
import numpy as np
ubi=0
opc=0
arreglo=np.zeros((10,10),object)
total=[]
asiento=[]
runes=[]
categoria=[]
ganancia=0
entradas=0
for f in range(10):
 for c in range(10):
  ubi=ubi+1
  arreglo[f,c]=ubi
while opc!=5:
 print("**Concierto Michael Jam por Creativos.cl**")
 print("1)Comprar Entrada \n2)Mostrar Ubicaciones Disponibles \n3)Ver Listado de asistentes \n4)Mostrar Ganancias totales \n5)Salir")
 opc=fn.validaOpc(int,"Ingrese Opcion deseada: ",1,5)
 if opc==1:
    print("**Valores--->Platinun(1-20:$120000),Gold(21-50:$80000),Silver(51-100:$50000)**")
    num=fn.validaOpc(int,"Ingrese ubicacion que desea comprar:",1,100)
    run=fn.validaOpc(int,"Ingresa Rut(sin DV):",1000000,99999999)
    fn.comprarAsiento(arreglo,num,run,asiento,total,runes,categoria)
 elif opc==2:
    fn.imprimirArreglo(arreglo)
 elif opc==3:
   print('*'*45)
   print("Lista Asistentes:")
   fn.imprimirAsistentes(runes)
   print('*'*45)
 elif opc==4:
   print("***Entradas Vendidas***")
   fn.imprimirGanancias(categoria,asiento,total)
   ganancia=sum(total)
   print(f"La ganancia es:${ganancia} con {len(asiento)} entradas vendidas")
   print('*'*50)
 else:
   fn.despedida()       