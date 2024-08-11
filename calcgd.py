print("""======================
         =CALCULADORA DE ORBES=
         ======================\n""")
print("este programa te dira un calculo de cuanto vale la cantidad de orbes a diferentes monedas populares")

infinito = 0

while infinito == 0:

    opcion1 = 0
    resultado = 0
    orbes = 0

    print("""porfavor seleccione la moneda a usar
    1: Dolares $
    2: Euros €
    3: Bolivares Venezolanos bs""")
    opcion1 = int(input(">>>>"))

    print("\nahora indique la cantidad de orbes a calcular")
    orbes = int(input(">>>>"))

    if opcion1 == 1:
        resultado = (orbes * 0.1)
        print(orbes, " a dolares son ", resultado, "$")
    elif opcion1 == 2:
        resultado = (orbes * 0.2)
        print(orbes, " a dolares son", resultado, "€")
    elif opcion1 == 3:
        resultado = (orbes * 462)
        print(orbes, " a bolivares venezolanos son", resultado, "Bs")
    else:
        print("porfavor seleccione una opcion valida")
