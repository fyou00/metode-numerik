def f(x):
  return 2*x**2 + 3*x - 4

a = 0
b = 2

i = 1
while i <= 5:
  print(f"iterasi", i, f"[{a:.5f}, {b:.4f}]")
  
  c = (b-(f(b)*(b-a))/(f(b)-f(a)))
  
  print(f"a = {a:.5f} \tf(a)= {f(a):.5f}")
  print(f"b = {b:.5f} \tf(b)= {f(b):.5f}")
  print(f"c = {c:.5f} \tf(c)= {f(c):.5f}")

  if f(a)*f(c)>0:
    b = c
  else:
    a = c
  i += 1