def change():
    expense = 23.75
    money = 100
    
    gasto = float(expense)
    dinero_recibido = float(money)
    print("Ingresar gasto:")
    print(f"{expense}")
    print("Dinero recibido")
    print(f"{money}")

    vuelto = dinero_recibido - gasto

    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)

    print("\nVuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
