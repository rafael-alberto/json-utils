Coleccion de scripts python para trabjar con archivos JSON.

json2csv
---------
convierte un archivo json en un csv. 
uso: python.exe json2csv.py -e {archivo_entrada} -s {archivo_salida}
   {archivo_entrada} Nombre del archivo Json a procesar
   {archivo_salida} Nombre del archivo CSV en el que se escribiran los valores



json2sql
---------
convierte un archivo json en un archivo sql con las instrucciones insert para llenar una tabla con la informacion del Json. Toma como nombre de la tabla el nombre del archivo y como columnas los elementos del archivo json. Asume que es un arregrlo de elementos json.
uso: python.exe json2sql.py -a {nombre_arch_json}
   {nombre_arch_json} Nombre del archivo Json a procesar, el nombre del archivo sql es el mismo del json con la extencion SQL
