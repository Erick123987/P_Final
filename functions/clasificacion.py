from granulometria import function_granulometria
from valoresdeentrada import valoresdeentrada

def clasificar_suelo():
    granulometria, suelo = valoresdeentrada()  # Obtener los valores de granulometría y el tipo de suelo

    resultados_granulometria = function_granulometria()  # Obtener los valores de Cc y Cu

    Cc = resultados_granulometria["Cc"]  # Obtener el valor de Cc desde los resultados
    Cu = resultados_granulometria["Cu"]  # Obtener el valor de Cu desde los resultados

    print('El suelo es', suelo)

    if suelo == 'Fino':
        LL = float(input("Ingrese el valor del Limite Liquido: "))
        LP = float(input("Ingrese el valor del Límite de Plasticidad: "))
        IP = LL - LP
    else:
        LL = None
        LP = None
        IP = None

    # Clasificación del suelo
    if suelo == "Grueso":
        print("El coeficiente de uniformidad es:", Cu)
        print("El coeficiente de curvatura es:", Cc)
        if Cu >= 4 and Cc <= 1:
            print("Grava bien graduada")
            print("USCS: GW")
        elif Cu >= 6 and 1 < Cc < 3:
            print("Grava pobremente graduada")
            print("USCS: GP")
        elif Cu < 4 and Cc <= 1:
            print("Grava uniforme")
            print("USCS: GU")
        elif 1.5 < Cc < 3:
            print("Grava mal graduada")
            print("USCS: GM")
        elif Cc >= 3 and Cu < 5:
            print("Arena bien graduada")
            print("USCS: SW")
        elif Cc >= 1 and (Cu >= 3 and Cu < 5):
            print("Arena mal graduada")
            print("USCS: SM")
        elif Cc < 1:
            print("Suelo de grano fino o limo")
            print("USCS: ML")
        else:
            print("Suelo de grano fino o arcilla")
            print("USCS: CL")
    elif suelo == "Fino":
        if Cu >= 6 and 1 <= Cc <= 3:
            print("SW (Arena bien graduada)")  # se imprime el tipo de suelo
        elif Cu < 6 and (1 > Cc or Cc > 3):
            print("SP (Arena mal graduada)")  # se imprime el tipo de suelo
        else:
            print("No aplica a la clasificación")  # se imprime que no entra en la clasificación
        if granulometria.loc[6, 'Porcentaje_pasa'] > 12:  # Usar el valor correspondiente a No.200 del código 1
            if IP < 4:  # se clasifica usando el IP
                print("SM (Arena limosa)")  # se imprime el tipo de suelo
            elif IP > 7:  # se clasifica usando el IP
                print("SC (Arena arcillosa)")  # se imprime el tipo de suelo
            else:
                print("No aplica a ninguna clasificación")  # se imprime que no entra en la clasificación
        else:
            if Cu >= 6 and 1 <= Cc <= 3:
                if IP < 4:  # se clasifica usando el IP
                    print("SW_SM (Arena bien graduada con limo)")  # se imprime el tipo de suelo
                elif IP > 7:  # se clasifica usando el IP
                    print("SW_SC (Arena bien graduada con arcilla")  # se imprime el tipo de suelo
                else:
                    print("No aplica a ninguna clasificación")  # se imprime que no entra en la clasificación
            elif Cu < 6 and (1 > Cc or Cc > 3):
                if IP < 4:  # se clasifica usando el IP
                    print("SP_SM (Arena mal graduada con limo)")  # se imprime el tipo de suelo
                elif IP > 7:  # se clasifica usando el IP
                    print("SP_SC (Arena mal graduada con arcilla)")  # se imprime el tipo de suelo
                else:
                    print("No aplica a ninguna clasificación")  # se imprime que no entra en la clasificación

    else:
        print("No se puede clasificar el suelo")  # se imprime que no se puede clasificar el suelo

    # Crear el diccionario con los datos LL e IP
    resultados_1 = {"LL": LL, "IP": IP}
    return resultados_1

# Llamar a la función y obtener los resultados
resultados = clasificar_suelo()
print(resultados)
