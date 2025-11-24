import math

def xr(x):
    return math.sqrt(2*x + 3)

def titik_tetap(x0, toleransi, max_iter=100):
    print("r\t x_r\t\t|xr+1-xr|\tgalat")
    for i in range(max_iter):
        x1 = xr(x0)
        error = abs(x1 - x0)
        print(f"{i}\t{x0:.6f}\t{x1:.6f}\t{error:.6f}\t")
        if error < toleransi:
            print("\nHasil Titik Tetap =", x1, "\n")
            return x1
        x0 = x1
        
print("===== TITIK TETAP =====")
titik_tetap(4, 1e-6)