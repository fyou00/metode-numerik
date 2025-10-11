x = "awesome" # variabel global

def myfunc():
  x = "fantastic" # variabel lokal
  print("Python is " + x)

myfunc()
print("Python is " + x)