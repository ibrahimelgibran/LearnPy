#praktek 1
jawab ='ya'
hitung = 0
while (jawab == 'ya'):
  hitung += 1
  jawab = input("Ulang lagi tidak?") 
print ("Total perulagan: ", hitung)

#praktek 2
count = 0
while (count < 10):
  print("jumlah adalah: ", count)
  count = count + 1
print("selamat tinggal")

#praktek 3
ulang = 5
for i in range(ulang):
  print("perulangan ke-1"+str(i+1))

#praktek 4
item = ['kopi','nasi', 'teh', 'jeruk']
for isi in item:
  print(isi)

#praktek 5
i = 0
while i < 5:   
    print("Nilai i saat ini:", i)
    i += 1     
print("selesai")
i = 0
while i < 5:   
    j = 0
    while j < 5:   
        if j < 4:
            print("A", end=" ")
        else:
            print("B\t")
        j += 1    
    i += 1         