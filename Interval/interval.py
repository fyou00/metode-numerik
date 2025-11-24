# 2x^2+3x-4

def f(x):
  return 2*x**2 + 3*x - 4

print("\nInterval 1")
x = -3
while x <= 3:
  print("x=", x, "\tf(x)=", f(x))
  x += 1
  
print("\nInterval 2")
x = -3.0
while x <= -1.9:
  print(f"x= {x:.1f}\tf(x)= {f(x):.2f}")
  x += 0.1
  
print("\nInterval 3")
x = -2.40
while x <= -2.30:
  print(f"x= {x:.2f}\tf(x)= {f(x):.4f}")
  x += 0.01
  
print("\nInterval 4")
x = -2.360
while x <= -2.350:
  print(f"x= {x:.3f}\tf(x)= {f(x):.4f}")
  x += 0.001
  
print("\nInterval 5")
x = -2.3510
while x <= -2.3498:
  print(f"x= {x:.4f}\tf(x)= {f(x):.4f}")
  x += 0.0001