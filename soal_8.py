#Soal 8

print ("===========================")
print ("PROGRAM TABUNG")
print ("===========================")

phi = 3.14
luas = lambda r,t:phi*r**2+2*phi*r*t
keliling = lambda r,t:2*phi*r*t
r =float(input("Masukkan Jari Jari :"))
t =float(input("Masukkan Tinggi :"))

print (f"Luas : {luas(r,t)}")
print (f"Keliling : {keliling(r,t)}")