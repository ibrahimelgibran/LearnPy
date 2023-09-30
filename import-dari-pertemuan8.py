import Class as c

d = c.Divisi('D01', 'Personalisa')

k1 = c.Karyawan('K01', 'Ibrahim')
k2 = c.Karyawan('K02', 'Gibran')
k1.set_gaji(2000000)
k2.set_gaji(2500000)

m = c.Manager('M01', 'El')
m.set_gaji(3000000)
m.set_bonus(1500000)

d.karyawan.append(k1)
d.karyawan.append(k2)

k1.presensi = c.Presensi()  
k2.presensi = c.Presensi()  
k1.presensi.set_presensi('2023-06-13', 'Hadir')
k2.presensi.set_presensi('2023-06-17', 'Tidak Hadir')
pk1 = k1.presensi.get_presensi()
pk2 = k2.presensi.get_presensi()

print('Divisi', d.nama)
print('Data Karyawan pada divisi ini')
for kk in d.karyawan:
    print('nip:', kk.nip, 'nama:', kk.nama)
    print('Data Presentasi')
    for pp in kk.presensi.get_presensi():
        print('Tanggal:', pp[0], 'Status:', pp[1])
    print()
