def xr(x):
    return (3/(x-2))

def titik_tetap(x0, toleransi, max_iter=100):
    print("r\t   x_r\t\t|xr+1-xr|\tgalat")
    for i in range(max_iter):
        x1 = xr(x0)
        galat = abs(x1 - x0)
        print(f"{i}\t{x0:.6f}\t{x1:.6f}\t{galat:.6f}\t")
        if galat < toleransi:
            print(f"\nHasil Titik Tetap = {x1:.3f} \n")
            return x1
        x0 = x1
        
print("===== TITIK TETAP =====")
titik_tetap(4, 1e-6)