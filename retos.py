from os import system;
import math;
system('cls');
opcion = 1;
while opcion != 0:
    print('***Escoger tipo de ejercicio***');
    print('1. Retos de listas');
    print('2. Retos de while');
    print('0. Salir');
    print('******************************** \n\n')
    opcion = int(input('Escoger la opción: '));
    system('cls');
    if opcion == 1:
        opcionRetoLista = 1;
        while opcionRetoLista != 0:
            print('\n***Escoger numero de ejercicio***');
            print('1. Construir un programa que reciba el tamaño de una lista  y la llene con múltiplos de 7');
            print('2. Construir un programa que reciba el tamaño de una lista y la llene con números entregados por el usuario');
            print('3. Leer 8 ciudades colombianas, guardarlas en una lista y mostrar en orden inverso los datos ingresados');
            print('4. Leer 20 números enteros y guardar en una lista, después permitir que el usuario busque un número y si este se encuentra en la lista indicar con un mensaje que el resultado es exitoso');
            print('0. Salir');
            print('********************************\n')
            opcionRetoLista = int(input('Escoger la opción: '));
            system('cls');
            if(opcionRetoLista == 1):
                tamañoLista = int(input('Tamaño de la lista:'));
                lista = [];
                for i in range(1,tamañoLista+1,1):
                    lista.append(i*7)
                print(lista);
                input('Presiona cualquier tecla para continuar...');
                system('cls');
            elif(opcionRetoLista == 2):
                tamañoLista = int(input('Tamaño de la lista:'));
                lista = [];
                for i in range(1,tamañoLista+1,1):
                    lista.append(int(input('Digite el numero: ')));
                print(lista);
                input('Finalizar...');
                system('cls');
            elif(opcionRetoLista == 3):
                tamañoLista = 8;
                lista = [];
                listaInvertida = [];
                for i in range(tamañoLista):
                    lista.append(input('Digite la ciudad: '));
                for elementoLista in lista: 
                    listaInvertida.insert(0,elementoLista);
                print(f'Lista ingresada: {lista}');
                print(f'Lista invertida: {listaInvertida}');
                input('Finalizar...');
                system('cls');
            elif(opcionRetoLista == 4):
                tamañoLista = 20;
                lista = [];
                for i in range(tamañoLista):
                    lista.append(int(input('Digite el número:')));
                
                seEncontróNumero:bool = False;
                numeroABuscar = int(input('Número a buscar: '));
                for i in range(tamañoLista):
                    if(lista[i] == numeroABuscar):
                        seEncontróNumero = True;
                
                if(seEncontróNumero == True):
                    print('Exitoso')
                else:
                    print('El número no se encontró');     
                input('Finalizar...');
                system('cls');
            else:
                system('cls');
                
    elif opcion == 2:
        opcionRetoWhile = 1;
        while opcionRetoWhile != 0:
            print('\n***Escoger numero de ejercicio***');
            print('1. Construir un programa que reciba números enteros y los sume mientras estos sean positivos, si se digita un número negativo el programa debe terminar');
            print('2. Codificar un programa que presente un menú de 4 opciones y reciba un numero natural  para realizar las siguientes operaciones:');
            print('3.Mostrar los números del 1 al 200 saltando de 12 en 12(1,12,24…)');
            print('4. Pedir 20 números y contar cuantos de los ingresados fueron negativos');
            print('0. Salir');
            print('********************************\n')
            opcionRetoWhile = int(input('Escoger la opción: '));
            system('cls');
            if(opcionRetoWhile == 1):
                suma = 0;
                numero = 1;
                while numero >= 0:
                    numero = int(input("Ingrese otro número entero positivo: "))
                    suma += numero
                print("La suma de los números ingresados es:", suma);
                input('Finalizar...');
                system('cls');
            elif(opcionRetoWhile == 2) :
                while True:
                 print("Menú:")
                 print("0: Salida")
                 print("1: Encuentre si el número es múltiplo de 2")
                 print("2: Encuentre la raíz cuadrada del número")
                 print("3: Sume 100 al número ingresado")
                 print("4: Eleve a la 2 el número ingresado")
                 opcion = int(input("Ingrese una opción: "))
                 system('cls')
                 if opcion == 0:
                     print("¡Hasta luego!")
                     break
                 numero = int(input("Ingrese un número natural: "))
                 if opcion == 1:
                     if numero % 2 == 0:
                         print("El número es múltiplo de 2")
                     else:
                         print("El número no es múltiplo de 2")
                     input('Finalizar...')
                     system('cls')
                 elif opcion == 2:
                     raiz_cuadrada = math.sqrt(numero)
                     print("La raíz cuadrada de", numero, "es:", raiz_cuadrada)
                     input('Finalizar...');
                     system('cls');
                 elif opcion == 3:
                     numero += 100
                     print("El resultado de sumar 100 a", numero - 100, "es:", numero)
                     input('Finalizar...');
                     system('cls');
                 elif opcion == 4:
                     numero_cuadrado = numero ** 2
                     print("El resultado de elevar", numero, "a la 2 es:", numero_cuadrado)
                     input('Finalizar...');
                     system('cls');
                 else:
                     print("Opción inválida. Intente de nuevo.")
                
                system('cls');
            elif(opcionRetoWhile == 3):
                for i in range(1, 201, 12):
                    print(i)
                input('Finalizar...');
                system('cls');
            elif(opcionRetoWhile ==4):
                contador_negativos = 0
                for i in range(20):
                 numero = int(input("Ingrese un número: "))
                 if numero < 0:
                     contador_negativos += 1
                print("Se ingresaron", contador_negativos, "números negativos.")
                input('Finalizar...');
                system('cls');

print('**************************')
print('***Programa finalizado.***')
print('**************************')
input();
