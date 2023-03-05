opcion = 1;
while opcion != 0:
    print('***Escoger tipo de ejercicio***');
    print('1. Retos de listas');
    print('2. Retos de while');
    print('0. Salir');
    print('******************************** \n\n')
    opcion = int(input('Escoger la opción: '));
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
            if(opcionRetoLista == 1):
                tamañoLista = int(input('Tamaño de la lista:'));
                lista = [];
                for i in range(1,tamañoLista+1,1):
                    lista.append(i*7)
                print(lista);
                input('Finalizar...');
            elif(opcionRetoLista == 2):
                tamañoLista = int(input('Tamaño de la lista:'));
                lista = [];
                for i in range(1,tamañoLista+1,1):
                    lista.append(int(input('Digite el numero: ')));
                print(lista);
                input('Finalizar...');
            elif(opcionRetoLista == 3):
                tamañoLista = 8;
                lista = [];
                for i in range(tamañoLista):
                    lista.append(input('Digite la ciudad: '));
                lista.reverse();
                print(lista);
                input('Finalizar...');
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
            else:
                print('Esta opción no esta caremonda');
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
            
    

print('********************************')
print('Programa finalizado.')