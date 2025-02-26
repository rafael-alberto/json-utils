import json
import os
import argparse
import re



def limpiar_valor(valor):
    # Elimina caracteres especiales, comillas y saltos de línea del valor
    valor_limpio = re.sub(r'[^\w\s]', '', valor)
    valor_limpio = valor_limpio.replace('\n', '').replace('\r', '')
    return valor_limpio

#quita los elementos no necesarios del objeto json
def eliminar_elementos(json_data, elementos_a_eliminar):
    if isinstance(json_data, dict):
        # Si es un diccionario, recorre sus elementos
        return {k: eliminar_elementos(v, elementos_a_eliminar) for k, v in json_data.items() if k not in elementos_a_eliminar}
    elif isinstance(json_data, list):
        # Si es una lista, recorre sus elementos
        return [eliminar_elementos(item, elementos_a_eliminar) for item in json_data if item not in elementos_a_eliminar]
    else:
        # Si no es ni diccionario ni lista, retorna el valor tal cual
        return json_data
        

def json_to_sql(json_file, a_excluir):
    print("Leyendo Archivo Json")

    # Lee el archivo JSON
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Obtén el nombre de la tabla (sin la extensión del archivo)
    table_name = os.path.splitext(os.path.basename(json_file))[0]
    
    #elementos a excluir del proceso.
    if a_excluir != '':
        print("Eliminando los elementos a excluir")
        data = eliminar_elementos(data, a_excluir)
    

    # Obtén los nombres de las columnas a partir de las claves del primer objeto JSON
    columns = data[0].keys()

    # Genera las sentencias SQL INSERT
    sql_statements = []
    for entry in data:
        values = ', '.join([f"'{limpiar_valor(str(value))}'" for value in entry.values()])
        sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({values});"
        sql_statements.append(sql.replace("'None'", "null"))

    return sql_statements


# inicializar el parser
parser = argparse.ArgumentParser()

# agregar los parametros
parser.add_argument("-a", "--archivo", help = "nombre archivo json")
args = parser.parse_args()

json_file = ''
if args.archivo:
    #Lista de columnas que no se utilizaran
    col_excluidas = ["odataetag","city","hasPendingInvoices","invoicesCount","erpSenderBehavior","erpSenderBehaviorPayments"]
    
    #ponemos los nombres de archivos json y csv
    json_file = args.archivo
    sql_file = os.path.splitext(os.path.basename(json_file))[0] + ".sql"

    sql_statements = json_to_sql(json_file, col_excluidas)
    with open(sql_file, 'w') as archivo:
        print("Generando archivo SQL")
        for sql in sql_statements:
            archivo.write(f"{sql.strip()}\n")

else:
    print("Debe proporcionar un archivo de entrada")
