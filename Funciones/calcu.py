memoria=[]
def suma(n):
    for i in range(n):
        total=0
        nro=int(input("Ingrese nro", i+1))
        total+=nro
    return
def resta(a,b):
    if a > b:
        
def division():
    pass

    while True:
        print("===Menu Calculadora===")
        print("1.SUMA ")
        print("2.RESTA ")
        print("3.DIVISION ")
        print("4.MULTIPLICACION ")
        print("5.SALIR")
    op=input("Ingrese la opcion que desea: ")
    match op:
        case "1":
            res=suma(int(input("Ingrese la cantidad de numeros que desea sumar: ")))
            memoria.append(res)
            
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            print("Saliendo del sistema... ")
            