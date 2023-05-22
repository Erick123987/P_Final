import pandas as pd

def valoresdeentrada():
    # Valores iniciales, granulometría dada por el usuario al realizar el ensayo de granulometría por tamizado.
    # Tamices en pulgadas.
    Denominacion = pd.Series(["No. 4", "No. 10", "No. 20", "No. 40", "No. 60", "No. 140", "No. 200", "Fondo"])
    # Abertura de los tamices en mm.
    Abertura = pd.Series([4.75, 2.00, 0.85, 0.425, 0.25, 0.106, 0.075, 0])
    # Porcentaje que pasa cada malla.
    Porcentaje_pasa = pd.Series([100, 80, 78, 70, 69, 59, 53])
    # Creación del dataframe.
    granulometria = pd.DataFrame({
        'Denominacion': Denominacion,
        'Abertura (mm)': Abertura,
        'Porcentaje_pasa': Porcentaje_pasa,
    })

    # Determinamos si el suelo es grueso o fino, basado en el porcentaje que pasa por el tamiz 'No. 200'
    suelo = 'Fino' if granulometria.loc[6, 'Porcentaje_pasa'] >= 50 else 'Grueso'

    return granulometria, suelo
# Llamada a la función y almacenamiento del resultado en una variable
resultado, suelo = valoresdeentrada()

# Imprimir el resultado
print(resultado)
print('El suelo es', suelo)
