import string
import glob
import os

def Cargar_Data(file_path, numdefialini, numdefilaFin):
    # -----------------------------------------------------------------------------------
    def make_iterator_from_single_file(file_path):
        
        primera_linea = True
        
        with open(file_path, "rt") as file: ##Reading and text mode (default)
            for line in file:
                if primera_linea is True:
                    primera_linea = False
                    continue
                line = line.split(";")[numdefialini.int()]+";"+line.split(";")[numdefilaFin.int()]
                yield line
    # -----------------------------------------------------------------------------------
    if os.path.isfile(file_path):
        return make_iterator_from_single_file(file_path)
   
def tolower(x):
    return x.lower()

def remove_punctuation(x):
    return x.translate(str.maketrans("", "", string.punctuation))

def remove_newline(x):
    return x.replace("\n", "")

def split_lines(x, separador):
    return x.split(separador.str())

def make_counts(acc, nxt):
    acc[nxt] = acc.get(nxt, 0) + 1
    return acc


def sum_counts(left, right):
    for key in right.keys():
        left[key] = left.get(key, 0) + right[key]
    return left