def f(x):
    return x**3 - 2*x - 5

def df(x):
    return 3*x**2 - 2

def newton_raphson(x0, tol, max_iter):
    print("r |     x_n      |     x1-x0     ")
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            print("Turunan nol. Tidak dapat melanjutkan iterasi.")
            return None
        x1 = x0 - fx / dfx
        print(f"{i+1} | {x1:12.6f} | {abs(x1-x0):12.6f}")
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return None

print("===== NEWTON RAPHSON =====")
akar = newton_raphson(2, 1e-3, 100)
print("Akar hampiran =", akar)