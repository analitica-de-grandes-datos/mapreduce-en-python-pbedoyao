#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    
    # Se lee el archivo linea line.
    for line in sys.stdin:
        
        #se divide la linea del archivo por coma ("\t")
        atributo, valor = line.split('\t')
        #se divide la segunda columna del archivo por coma (",")
        valor =list(valor.split(','))
        
        for letra in valor:
            #se se obtienen los valores separador por archivo por coma ("-")
            sys.stdout.write("{}-{}\n".format(letra.strip() ,atributo.zfill(4)))
        