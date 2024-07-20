#Soal 11

barang = int(input("Masukkan Harga Barang :"))

if barang >= 100000:
    diskon = barang * 0.05
    harga = barang - diskon
    print ("Selamat Anda Mendapat Diskon 5%")
else:
    diskon = 0
    harga = barang
    
print (f"Diskon = {diskon}")
print (f"Harga = {harga}")