def f(x):
    return 2*x**2 + 3*x - 4

print("INTERVAL [-4,0]")
a = -4
b = 0

i = 1
while i <= 5:
    print(f"iterasi ke-{i} dengan interval [{a},{b}]")

    c = (a + b) / 2
    
    x = a
    while x <= b:
        print(f"x={x:.3f}, \t f(x)={f(x):.6f}")
        x+=(b-a)/10

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

    print()
    i+=1

print("INTERVAL [0,4]")
p = 0
q = 4

j = 1
while j <= 5:
    print(f"iterasi ke-{j} dengan interval: [{p},{q}]")

    r = (p + q) / 2

    x = p
    while x <= q:
        print(f"x={x:.3f}, \t f(x)={f(x):.6f}")
        x+=(q-p)/10

    if f(p) * f(r) < 0:
        q = r
    else:
        p = r

    print()
    j+=1