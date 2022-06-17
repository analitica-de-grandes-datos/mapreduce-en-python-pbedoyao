#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#
import sys

if __name__ == "__main__":
    
    # Se lee el archivo linea line.
    for line in sys.stdin:
        #se divide la linea del archivo por coma (" ")
        lista = line.split("   ")
        # se escribe la salida del archivo obteniendo tres columna
        sys.stdout.write("{},{},{}\n".format(lista[2].strip().zfill(4),lista[0].strip(),lista[1].strip()))