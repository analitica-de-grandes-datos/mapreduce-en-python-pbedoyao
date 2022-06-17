#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

atributos = []
if __name__ == '__main__':
    
    for line in sys.stdin:
        #se divide la linea del archivo por coma ("-")
        lista = line.split("-")
        # se escribe la salida del archivo obteniendo una columna
        atributos.append(int(lista[1].strip()))
        atributos.sort(reverse=False)
        
    anteratributo = None
    total = 1
    
    for elemento in atributos:
        
        valor = int(1)
        
        #se compara el atributo si son iguales se le suma 1 al valor
        if elemento == anteratributo:
            total += valor
        else:
            #se el anterior atributo no es vacio se inmprime la linea
            if anteratributo is not None:
                if len(str(anteratributo)) == 1:
                    sys.stdout.write("0{}\t{}\n".format(anteratributo, total))
                else:
                    sys.stdout.write("{}\t{}\n".format(anteratributo, total))
                total = 1

            #se reinicia los valores de atributo y total con el nuevo atributo
            anteratributo = elemento
            total = valor
    
    if len(str(anteratributo)) == 1:
        sys.stdout.write("0{}\t{}\n".format(anteratributo, total))
    else:
        sys.stdout.write("{}\t{}\n".format(anteratributo, total))

            