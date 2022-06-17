#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys 
 
if __name__ == '__main__': 
 
    anteratributo = None 
    total = 0 
 
    for line in sys.stdin: 
 
        atributo, valor = line.split("-") 
        valor = valor.strip() 
 
        if atributo == anteratributo: 
            numeros = numeros + ',' + str(int(valor)) 
        else: 
            if anteratributo is not None: 
                sys.stdout.write("{}\t{}\n".format(anteratributo, numeros)) 
 
            anteratributo = atributo 
            numeros = str(int(valor)) 
 
    sys.stdout.write("{}\t{}\n".format(anteratributo, numeros))