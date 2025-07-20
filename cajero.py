"""CAJERO"""
"""hacer un cajero con un saldo inicial de $1000 y tedndria un ménu de opciones
1 Ingresar dinero en la cuenta
2  Retirar dinero de la cuenta
3  Mostrar dinero disponible
4. Hisotiral de transacciones
5 Salir"""


print("Bienvenido a su banco de confianza")
saldo=500.00
transaccion=[]

while True:
    print("\nMENU DE OPCIONES")
    print("1. Ingreso de dinero")
    print("2. Retiro de dinero")
    print("3. Mostrar saldo")
    print("4. Historial de Transacciones")
    print("5. Salir")
    accion=int(input("Ingrese el número de la opcion que quiera elegir:\n"))

    if accion==1:
        ingreso=float(input("Ingrese el monto que desea depositar:\n"))
        saldo+=ingreso
        transaccion.append(f"Ingreso->{ingreso}")
        print(f"El deposito fue exitoso, su cuenta mantiene un saldo actual de ${saldo:.2f}")
    elif accion==2:
        retiro=float(input("Ingrese el monto a retirar:"))
        if saldo>=retiro:
            saldo-=retiro
            transaccion.append(f"Retiro->{retiro}")
            print(f"El retiro fue exitoso, su cuenta mantiene un total de ${saldo}")
        else:
            print(f"Su cuenta no posee el dinero solicitado, intente con un monto menor o igual a ${saldo}")
    elif accion==3:
        print(f"Su saldo actual es de ${saldo}")
    elif accion==4:
        print("Sus transacciones realizadas el día de hoy fueron:\n")
        for t in transaccion:
            print(t)
    elif accion==5:
            print("Gracias por utilizar nuestros servicios. Vuelva pronto!")
            exit()
    
    else:
        print("Elija una opción correcta del menú")


        

