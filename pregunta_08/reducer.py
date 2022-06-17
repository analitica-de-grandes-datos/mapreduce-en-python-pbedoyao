#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys


if __name__ == '__main__':

    #Se crea una lista vacia para los tipo de atributos
    anteratributo = None
    suma = 0
    numrep = 0
    
    # Se lee el archivo de entrada linea a linea
    for line in sys.stdin:
        
        # se obtiene el atribito de tipo de credito y el valor 1
        atributo, valor = line.split(",")
        # Se convierte el valor a entero
        valor = int(valor)
        
        #se compara el atributo si son iguales se le suma 1 al valor
        if atributo == anteratributo:
            suma += valor
            numrep += 1
            
        else:
            #se el anterior atributo no es vacio se inmprime la linea
            if anteratributo is not None:
                promedio = suma/numrep
                sys.stdout.write("{}\t{}\t{}\n".format(anteratributo, float(suma), promedio))

            #se reinicia los valores de atributo y valor con el nuevo atributo
            anteratributo = atributo
            suma = valor
            numrep = 1

    promedio = suma/numrep
    sys.stdout.write("{}\t{}\t{}\n".format(anteratributo, float(suma), promedio))