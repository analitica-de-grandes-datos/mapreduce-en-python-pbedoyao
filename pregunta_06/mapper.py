#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    
    # Se lee el archivo linea line.
    for line in sys.stdin:
        #se divide la linea del archivo por  (" ")
        lista = line.split(" ")
        # se escribe la salida del archivo obteniendo dos columna
        sys.stdout.write("{},{}\n".format(lista[0].strip(),lista[6].strip()))