# ENTRADAS=VARIABLES=REFERENCIAS EN MEMORIA
nivelAgua=input("Digite el nivel de agua: ")

#PROCESO
if(nivelAgua>=0 and nivelAgua<20):
    #SALIDA
    print(f'el nivel de agua es {nivelAgua} y este es bajo')
elif(nivelAgua>=20 and nivelAgua<400):
    #SALIDA
    print(f'el nivel de agua es {nivelAgua} Operando normalmente')
elif(nivelAgua>=400):
    #SALIDA
    print(f'el nivel de agua es {nivelAgua} llamen a FICO y a LUPE')
else:
    #SALIDA
    print("El nivel de agua no es valido")


