#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    
    # Se lee el archivo linea line.
    for line in sys.stdin:
        #se divide la linea del archivo por coma (" ")
        lista = line.split(",")
        # se escribe la salida del archivo obteniendo dos columna
        sys.stdout.write("{}\t{}\t{}\n".format(lista[0].strip(),lista[2].strip(), int(lista[1].strip())))