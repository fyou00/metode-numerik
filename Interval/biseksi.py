def f(x):
  return 2*x**2 + 3*x - 4

a = -3.0
b = 3.0

i = 1
while i <= 5:
  print(f"iterasi", i, f"[{a}, {b}]")
  c = (a + b) / 2
  print("a = ", a, "\tf(a)=", f(a))
  print("b = ", b, "\tf(b)=", f(b))
  print("c = ", c, "\tf(c)=", f(c))

  if f(a)*f(c)<0:
    b = c
  else:
    a = c
  i += 1
  