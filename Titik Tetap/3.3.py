def xr(x):
    return ((-x**3+3)/6)

def xr1(xr):
    return ((-xr**3+3)/6)

def titik_tetap(x0, tolerasi=1e-5, max_iter=100):
    print("Iter\t   x_r\t\t|xr+1-xr|\t")
    for i in range(1, max_iter + 1):
        x1 = xr(x0)
        galat = abs(x1 - x0)
        print(f"{i}\t{x0:.6f}\t{galat:.6f}\t")
        if galat < tolerasi:
            print("\nHasil Titik Tetap =", x1, "\n")
            return x1
        x0 = x1
        
print("===== TITIK TETAP =====")
titik_tetap(0.5)