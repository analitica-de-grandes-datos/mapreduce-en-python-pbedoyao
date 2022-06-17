#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
#
import sys

if __name__ == "__main__":
    numprin = 0
    # Se lee el archivo linea line.
    for line in sys.stdin:
        #se divide la linea del archivo por coma ("   ")
        lista = line.split(",")
        # se escribe la salida del archivo obteniendo tres columna
        sys.stdout.write("{}   {}   {}\n".format(lista[1].strip(),lista[2].strip(),int(lista[0].strip())))
        numprin += 1
        if numprin == 6:
            # se interrumpe program
            break