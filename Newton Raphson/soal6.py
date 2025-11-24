import math 

def f(x):
    return math.sin(x) - 0.5

def df(x):
    return math.cos(x)

def newton_raphson(x0, tol, max_iter):
    print("r |   x_n    |   error   ")
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            print("Turunan nol. Tidak dapat melanjutkan iterasi.")
            return None
        x1 = x0 - fx / dfx
        print(f"{i+1} | {x1:.6f} | {abs(x1-x0):.6f}")
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return None

print("===== NEWTON RAPHSON =====")
akar = newton_raphson(1, 1e-4, 100)
print("Akar hampiran =", akar)