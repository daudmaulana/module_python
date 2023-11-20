import module_bangunruang as br

print('Pilih bangun ruang yang akan dihitung : ')
print('1. Lingkaran')
print('2. Segitiga')
print('-----------------------------------------')

pilih = input('Masukkan pilihan : ')
if pilih == '1':
    r = int(input('Masukkan ruas : '))
    luas, keliling = br.lingkaran(r)
    print(f'Luas : {luas}')
    print(f'Keliling : {keliling}')
elif pilih == '2':
    a = int(input('Masukkan alas : '))
    t = int(input('Masukkan tinggi : '))
    s = int(input('Masukkan sisi : '))
    luas, keliling = br.segitiga(a,t,s)
    print(f'Luas : {luas}')
    print(f'Keliling : {keliling}')