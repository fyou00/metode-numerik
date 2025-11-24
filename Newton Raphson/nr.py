import math

# Definisi fungsi dan turunannya
def f(x):
    return math.cos(x) - x

def df(x):
    return math

# Implementasi metode Newton-Raphson
def newton_raphson(x0, tol, max_iter):
    print("Iterasi |     x_n      |     x1-x0     ")
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            print("Turunan nol. Tidak dapat melanjutkan iterasi.")
            return None
        x1 = x0 - fx / dfx
        print(f"{i+1:7d} | {x1:12.6f} | {abs(x1-x0):12.6f}")
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return None

akar = newton_raphson(2, 0.001, 100)
print("Akar hampiran =", akar)