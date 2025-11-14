# 2x^2+3x-4

def f(x):
  return 2*x**2 + 3*x - 4
    
for x in range(-3, 3):
  print("x=", x, end="\t f(x)= ")
  print(f(x))