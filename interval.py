# 2x^2+3x-4

def f(x):
  return 2*x**2 + 3*x - 4

i = 1
while i <= 1:
  print("interval", i)
  x = -3
  # x_pos = None
  # x_neg = None
  while x <= 3:
    print("x=", x, end="\t f(x)= ")
    print(f(x))
    # y = f(x)
    # if y > 0 and x_pos is None:
    #   x_pos = y
    # elif y < 0 and x_pos is not None:
    #   x_neg = y
    #   break
    x += 1
  i += 1
  print()