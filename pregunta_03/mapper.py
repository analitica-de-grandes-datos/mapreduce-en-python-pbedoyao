#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    
    # Se lee el archivo linea line.
    for line in sys.stdin:
        #se divide la linea del archivo por coma (,)
        lista = line.split(",")
        # se escribe la salida del archivo obteniendo la columna 2 separada por ,
        sys.stdout.write("{}\n".format(lista[1].strip()))
        