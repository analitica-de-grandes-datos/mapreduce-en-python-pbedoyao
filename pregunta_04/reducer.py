#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    #Se crea 2 variables 
    anteratributo = None
    total = 1
    
    # Se lee el archivo de entrada linea a linea
    for line in sys.stdin:
        
        # se obtiene el atribito de tipo de credito y el valor 1
        atributo = line.strip()
        # Se convierte el valor a entero
        valor = int(1)
        
        #se compara el atributo si son iguales se le suma 1 al valor
        if atributo == anteratributo:
            total += valor
        else:
            #se el anterior atributo no es vacio se inmprime la linea
            if anteratributo is not None:
                sys.stdout.write("{},{}\n".format(anteratributo, total))
                total = 1

            #se reinicia los valores de atributo y total con el nuevo atributo
            anteratributo = atributo
            total = valor

    sys.stdout.write("{},{}\n".format(anteratributo, total))