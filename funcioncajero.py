saldo=100.00
movimientos=[]

def consultar_saldo(saldo):
    return saldo
    

def depositar(cantidad):
    if cantidad>0:
        movimientos.append({"tipo": "deposito", "Cantidad": cantidad})
        print(F"Tu deposito fue de {cantidad}")
        return cantidad+saldo
    else:
        print(f"El monto debe ser mayor a 0 ")
        return saldo

def retirar(cantidad):
    if cantidad<=0:
       print("El retiro debe ser mayor que 0")
       return saldo
    elif cantidad>saldo:
        print(f"No puedes retirar más que {saldo}")
        return saldo
    else:
        movimientos.append({"tipo": "retiro", "Cantidad": cantidad})
        print(f"Tu retiro fue de {cantidad}")
        return saldo-cantidad

def mostrar_historial(movimientos):
    print("-----HISTORIAL DE MOVIMIENTOS-----")
    for movimiento in movimientos:
        print("-", movimiento["tipo"],"de", movimiento["Cantidad"])
        print("----------------")
    return

def mostrar_menu():
    print("-------CAJERO AUTOMATICO------")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Mostrar historial")
    print("5. Salir")
    return 

while True:
    mostrar_menu()
    opcion=input("Ingresa una opción:")
    print("Elegiste la opción:", opcion)

    if opcion=="1":
        print("Su saldo actual es de :", consultar_saldo(saldo))

    elif opcion=="2":
        try:
            cantidad=float(input("Ingresa la cantidad que quieres depositar:"))
            saldo=depositar(cantidad)
            print(f"Tu saldo actual es de: {consultar_saldo(saldo)}")
        except ValueError:
            print("Debes ingresar un número")

    elif opcion=="3":
        try:
            cantidad=float(input("Ingresa la cantidad a retirar:"))
            saldo=retirar(cantidad)
            print(f"Tu saldo actiual es de {consultar_saldo(saldo)}")
        except ValueError:
            print("Debes ingresar un número")

    elif opcion=="4":
        mostrar_historial(movimientos)

    elif opcion=="5":
        break
    else:
        print("Esa opción no es válida, ingresa otra")
        
