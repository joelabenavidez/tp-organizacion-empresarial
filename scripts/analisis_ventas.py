
# SCRUM-2 - Análisis de ventas

archivo_entrada = "datos/ventas.csv"
archivo_salida = "resultados/ventas_total.csv"

with open(archivo_entrada, "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

nuevas_lineas = []

encabezado = lineas[0].strip() + ",total\n"
nuevas_lineas.append(encabezado)

for linea in lineas[1:]:
    datos = linea.strip().split(",")

    fecha = datos[0]
    producto = datos[1]
    cantidad = int(datos[2])
    precio = int(datos[3])

    total = cantidad * precio

    nueva_linea = f"{fecha},{producto},{cantidad},{precio},{total}\n"
    nuevas_lineas.append(nueva_linea)

with open(archivo_salida, "w", encoding="utf-8") as archivo_nuevo:
    archivo_nuevo.writelines(nuevas_lineas)

with open(archivo_salida, "r", encoding="utf-8") as nuevo_csv:
    print(nuevo_csv.read())
