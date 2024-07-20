#Soal 21

akhir = 6
awal = 1
total = 0

while awal < akhir:
    print (awal,end="")
    awal += 2
    if awal < akhir:
        print (" + ", end="")
    total += 3
print (f" = {total}")
