def xr(x):
    return ((x**2-3)/2)

def titik_tetap(x0, toleransi, max_iter=5):
    print("Iter\t   x_r\t\t|xr+1-xr|\tgalat")
    for i in range(1, max_iter + 1):
        x1 = xr(x0)
        error = abs(x1 - x0)
        print(f"{i}\t{x0:.6f}\t{x1:.6f}\t{error:.6f}\t")
        if error < toleransi:
            print("\nHasil Titik Tetap =", x1, "\n")
            return x1
        x0 = x1
        
print("===== TITIK TETAP =====")
titik_tetap(4, 1e-6)