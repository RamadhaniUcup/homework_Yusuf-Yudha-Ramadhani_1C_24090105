#Data mahasiswa beasiswa informatika
print('DATA MAHASISWA')
nama = (input('Masukkan nama : '))
nim = int(input('Masukkan nim : '))
prodi = (input('masukkan asal prodi : '))
ipk = float(input('masukkan ipk : '))
no = int (input('masukkan no hp : '))
kampus = (input('masukkan kampus : '))
print()

#syarat mendapatkan beasiswa
print('SYARAT MENDAPATKAN BEASISWA')
lomba = (input('masukkan lomba yang anda pernah ikuti : '))
bahasa_asing = (input('menguasai bahasa asing : '))
prestasi = (input('masukkan prestasi : '))


#syarat
nilai = ('tinggi')
bahasa = ( 'jepang ')
poltek = ('poltek harber')




if (ipk > 3.4) and (bahasa_asing in bahasa) and (kampus in poltek) and (lomba) and (prestasi):
    hasil=('MENDAPTAKAN BEASISWA')
else:
    hasil=('TIDAK MENDAPATKAN BEASISWA')

print("-"*25)
print('Nama : ', nama)
print("NIM : ", nim)
print('Prodi : ', prodi)
print('IPK : ', ipk)
print("Nomor Handphone : ", no)
print(hasil)


