import math

def newton_raphson(f, df, x0, tol=1e-3, max_iter=50):
    print("Iter\t   x_n\t\t   f(x_n)\t\tError")
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            print("Turunan nol! Metode gagal.")
            return None
        x1 = x0 - fx/dfx
        error = abs(x1 - x0)
        print(f"{i}\t{x0:.6f}\t{fx:.6f}\t{error:.6f}")
        if error < tol:
            print("\nHasil Akar Hampiran =", x1, "\n")
            return x1
        x0 = x1

print("===== SOAL 4 =====")
f  = lambda x: x**3 - 9*x + 3
df = lambda x: 3*x**2 - 9
newton_raphson(f, df, x0=0.5, tol=1e-3)
