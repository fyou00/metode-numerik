# # 3.1 Boolean
# print(10 < 9)
# print(10 == 9)
# print(10 > 9)

# a = 200
# b = 33

# if b > a:
#   print("b lebih besar dari a")
# else:
#   print("a lebih besar dari b")

# # 3.2 Bool
# print(bool("Hello"))
# print(bool(15))

# # 3.3 Kebanyakan nilai adalah benar
# print(bool("abc"))
# print(bool(123))
# print(bool(["apple", "cherry", "banana"]))

# # 3,4 Beberapa nilai adalah salah
# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))

# 3.5 Fungsi bool()
# class myclass():
#   def __len__(self):
#     return 0
# myobj = myclass()
# print(bool(myobj))

# # 3.6 Fungsi dapat mengembalikan nilai boolean
# def myFunction() :
#   return True
# print(myFunction())

# def myFunction() :
#   return True
# if myFunction():
#   print("YES!")
# else:
#   print("NO!")

# # 3.7 Isinstance
# x = 200
# print(isinstance(x, int))