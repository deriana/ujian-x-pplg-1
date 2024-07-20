#Soal 7

print ("===========================")
print ("PROGRAM LINGKARAN")
print ("===========================")

phi = 3.14
luas = lambda r:phi*r**2
keliling = lambda r:2*phi*r
r =float(input("Masukkan Jari Jari :"))

print (f"Luas : {luas(r)}")
print (f"Keliling : {keliling(r)}")