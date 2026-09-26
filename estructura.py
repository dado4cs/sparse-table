from math import log2

# clase principal de la sparse table
class MinSparseTable:
    def __init__(self, arr: list):
        self.n = len(arr)
        y = int(log2(self.n)) + 1
        self.mat = [[0 for _ in range(self.n)] for _ in range(y)]
        
        # llenado de la primera fila
        for i in range(0, self.n):
            self.mat[0][i] = arr[i]
            
        # llenado de las potencias de 2
        for j in range(1, y):
            rango = self.n - 2**j + 1
            for i in range(0, rango):
                off = i + 2 ** (j - 1)
                self.mat[j][i] = min(self.mat[j - 1][i], self.mat[j - 1][off])

    # funcion de consulta
    def query(self, left, right):
        size = right - left + 1
        y = int(log2(size))
        op1 = self.mat[y][left]
        op2 = self.mat[y][right - 2**y + 1]
        return min(op1, op2)

# datos de prueba y constantes
INPUT_ARRAY = [5, 6, 9, 12, 2, 18, 15, 11, 7, 1]
QUERIES = [(1, 5), (0, 9), (3, 7), (3, 3)]
CELL_SIZE = 0.60
FONT = 24
SMALL_FONT = 18

# caracteres para superindices
_SUPERSCRIPTS = "⁰¹²³⁴⁵⁶⁷⁸⁹"

def _sup(num):
    return "".join(_SUPERSCRIPTS[int(d)] for d in str(num))
