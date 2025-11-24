# 2x^2+3x-4

def f(x):
  return (((-x**3)+3)/6)

print("\nInterval 1")
x = -3
while x <= 3:
  print(f"x= {x}, \tf(x)= {f(x):.1f}")
  x += 1
  
print("\nInterval 2")
x = 1
while x <= 2.1:
  print(f"x= {x:.1f}\tf(x)= {f(x):.2f}")
  x += 0.1
  
print("\nInterval 3")
x = 1.4
while x <= 1.5:
  print(f"x= {x:.2f}\tf(x)= {f(x):.4f}")
  x += 0.01
  
print("\nInterval 4")
x = 1.44
while x <= 1.45:
  print(f"x= {x:.3f}\tf(x)= {f(x):.4f}")
  x += 0.001
  
print("\nInterval 5")
x = 1.442
while x <= 1.443:
  print(f"x= {x:.4f}\tf(x)= {f(x):.4f}")
  x += 0.0001