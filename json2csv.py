import pandas as pd
import json
import argparse


# inicializar el parser
parser = argparse.ArgumentParser()

# agregar los parametros
parser.add_argument("-e", "--entrada", help = "nombre archivo entrada")
parser.add_argument("-s", "--salida", help = "nombre archivo salida")

args = parser.parse_args()


#revisar los argumentos
arch_entrada = ''
arch_salida = ''
if args.entrada:
    arch_entrada = args.entrada

if args.salida:
    arch_salida = args.salida

 
if arch_entrada != '' and arch_salida != '':
    # Carga el archivo JSON
    print('Cargando el archivo JSON')
    with open(arch_entrada, encoding='utf-8') as f:
        data = json.load(f)

    # Convierte los datos a un DataFrame de pandas
    print('Convierte los datos a un DataFrame de pandas')
    df = pd.DataFrame(data)

    # Guarda el DataFrame en un archivo CSV
    print('Guarda el DataFrame en un archivo CSV')
    df.to_csv(arch_salida, index=False, sep=';', encoding='utf-8', header=True, quoting=1)
else:
    print("Debe poner los dos parametros")