a = "HEllo, World!"
print(a[1]) # string adalah array

for x in "banana":
  print(x)

print(len(a)) # menghitung panjang string

## memeriksa
txt = "The best things in life are free!"
print("free" in txt) # true

if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("free" not in txt) # false

# string multi baris
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# mengiris string
b = "Hello, World!"
print(b[2:5]) # mulai dari index 2 sampai 5
print(b[:5]) # mulai dari index 0 sampai 5
print(b[2:]) # mulai dari index 2 sampai akhir
print(b[-5:-2]) # mulai dari index -5 sampai -2

a = "Hello, World!"
print(a.upper()) # huruf besar
print(a.lower()) # huruf kecil
print(a.strip()) # menghapus spasi di awal/akhir
print(a.replace("H", "J")) # mengganti karakter
print(a.split(",")) # memecah string menjadi list

a = "Hello"
b = "World"
c = a + " " + b # menggabungkan string
print(c)

age = 36
txt = "My name is John, I am " + str(age) # menggabungkan string dan integer
print(txt)

age = 36
txt = "My name is John, I am {}" # placeholder
print(txt.format(age))

quantitiy = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantitiy, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# method string
capitaliza(txt) # mengubah huruf pertama menjadi kapital
print(txt.capitalize())
print(txt.count("o")) # menghitung jumlah karakter
print(txt.endswith("north.")) # memeriksa akhiran string
print(txt.find("Vikings")) # mencari posisi karakter
print(txt.index("Vikings")) # mencari posisi karakter
print(txt.isalnum()) # memeriksa apakah semua karakter alfanumerik
print(txt.isalpha()) # memeriksa apakah semua karakter alfabet

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b > a:
 print("b is greater than a")
else:
 print("b is not greater than a")