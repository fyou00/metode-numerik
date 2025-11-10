def xr(x):
    return (3/(x-2))

def xr1(xr):
    return (3/(xr-2))

def titik_tetap(x0 = 4, tolerasi=1e-5, max_iter=100):
    print("Iter\t   x_r\t\t|xr+1-xr|\t")
    for i in range(max_iter):
        x1 = xr(x0)
        error = abs(x1 - x0)
        print(f"{i}\t{x0:.6f}\t{error:.6f}\t")
        if error < tolerasi:
            print(f"\nHasil Titik Tetap = {x1:.3f} \n")
            return x1
        x0 = x1
        
print("===== TITIK TETAP =====")
titik_tetap()