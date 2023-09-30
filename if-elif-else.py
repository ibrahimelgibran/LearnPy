



# soal 2
nilai = 9

print("Selamat Anda Lulus")

if(nilai > 10):
    print("Selamat Anda Lulus")

# soal 3
print("Masukkan dua buah angka..") 
print("Dan Anda akan check hubungan kedua angka tersebut")
angkal = input("Masukkan angka pertama : ")
angkal = int(angkal)
angka2 = input("Masukkan angka kedua : ")
angka2 = int(angka2) 
if angkal == angka2 :
    print(angkal, "sama dengan angka2", ) 
else:
    print (angkal, "tidak sama dengan ", angka2)
 
# soal 4
gaji = int(input("Masukkan gaji: "))
berkeluarga = bool(int(input("Masukkan 0/1: ")))
punya_rumah = input("Masukkan yes/no: ")

if gaji > 3000000:
    print("Gaji sudah di atas UMR")
    if berkeluarga:
        print("Wajib ikutan asuransi dan menabung untuk pensiun")
    else:
        print("Tidak perlu ikutan asuransi")
    if punya_rumah == "yes":
        print("Wajib bayar pajak rumah")
    else:
        print("Tidak wajib bayar pajak rumah")
else:
    print("Gaji belum UMR")

# soal 6
hari_ini = "Minggu"
if hari_ini == "Senin":
    print("Saya akan kuliah")
elif hari_ini == "Selasa":
    print("Saya akan kuliah")
elif hari_ini == "Rabu":
    print("Saya akan kuliah")
elif hari_ini == "Kamis":
    print("Saya akan kuliah")
elif hari_ini == "Jumat":
    print("Saya akan kuliah")
elif hari_ini == "Sabtu":
    print("Saya akan kuliah")
elif hari_ini == "Minggu":
    print("Saya akan libur")

# soal 1
total_belanjaan = float(input("Masukkan total belanjaan: "))
if total_belanjaan >= 500000:
    diskon = 0.25 * total_belanjaan
elif total_belanjaan >= 100000:
    diskon = 0.1 * total_belanjaan
elif total_belanjaan >= 50000:
    diskon = 0.05 * total_belanjaan
else:
    diskon = 0
total_bayar = total_belanjaan - diskon
print("Diskon belanja: Rp. ", diskon)
print("Total bayar: Rp. ", total_bayar)