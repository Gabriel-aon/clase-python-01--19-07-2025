print("----Bienvenido----")

print("\n1. Promedio de notas")
print("2. Valor abosoluto")
print("3. Calculadora")
print("4. Saludo personalizado")
opcion = int(input("\nIngrese la opcion que desea: "))

if opcion == 1:
    nombre = input("Ingrese el nombre del estudiante: ")
    not1 = float(input("Ingrese la primera nota: "))
    not2 = float(input("Ingrese la segunda nota: "))
    not3 = float(input("Ingrese la tercera nota: "))

    if not1 > 20 or not2 > 20 or not3 > 20:
        print("No se evalua sobre 20 o menos de 0")
    else:
        prom = (not1 + not2 + not3)/3
        print("El promedio de notas es: ", prom)

elif opcion == 2:
    numero = float(input("Ingrese un numero: "))

    if numero >= 0:
        absoluto = numero
    else: 
        absoluto = numero * -1
    print(f"El valor absoluto de {numero} es: ", absoluto)

elif opcion == 3:
    numero = float(input("Ingrese un numero: "))
    numero2 = float(input("Ingrese otro numero: "))
    operacion = input("Inegre se la opcion que desea (1.Suma/2.Resta/3.Multiplicacion/4.Division): ")
    
    if operacion == 1:
        suma = numero + numero2
        print ("La suma de los dos numeros es: ", suma)

    elif operacion == 2:
        resta = numero - numero2
        print ("La resta de los dos numeros es: ", resta)

    elif operacion == 3:
        multiplicacion = numero * numero2
        print ("La multiplicacion de los dos numeros es: ", multiplicacion)
        
    elif operacion == 4:
        if numero2 != 0:
            division = numero / numero2
            print ("La division de los dos numeros es: ", division)
    else:
        print("No se puede dividir entre 0")

elif opcion == 4:
    nombre = input("Ingrese su nombre: ")
    print(f"Hola {nombre}. Bienvenido al curso de python.")

else:
    print("Opcion invalida")
    