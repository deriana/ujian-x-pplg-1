x = int(input("Masukkan Angka x :"))
y = int(input("Masukkan Angka y :"))
z = int(input("Masukkan Angka z :"))

max = x
min = x

if y > z:
    max = y
if y < z:
    min = y
if z > y:
    max = z
if z < y:
    min = z
    
print (f"Max Number = {max}")
print (f"Min Number = {min}")