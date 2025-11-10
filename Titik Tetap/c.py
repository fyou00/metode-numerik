def xr(x):
    return ((x**2-3)/2)

def xr1(xr):
    return ((xr**2-3)/2)

def titik_tetap(x0 = 4, tolerasi=1e-5, max_iter=5):
    print("Iter\t   x_r\t\t|xr+1-xr|\t")
    for i in range(1, max_iter + 1):
        x1 = xr(x0)
        error = abs(x1 - x0)
        print(f"{i}\t{x0:.6f}\t{error:.6f}\t")
        if error < tolerasi:
            print("\nHasil Titik Tetap =", x1, "\n")
            return x1
        x0 = x1
        
print("===== TITIK TETAP =====")
titik_tetap()