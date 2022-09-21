import json

KaryawanBaru = int((input('Masukkan jumlah Karyawan baru anda: ')))
for i in range(KaryawanBaru):
    nama = input('Masukkan nama anda : ')
    list_karyawan = list()
    dict_karyawan = dict()
    dict_biodata = dict()
    jml_kolega = int(input('Masukkan jumlah kolega anda: '))
    list_kolega = list()
    for j in range(jml_kolega):
        kolega = input('Masukkan kolega ke-{}: '.format(str(j + 1)))
        list_kolega.append(kolega)
    dict_biodata['Hobi'] = list_kolega
    alamat = input('Masukkan alamat Anda: ')
    dict_biodata['alamat'] = alamat
    dict_karyawan['BioData'] = dict_biodata
    list_karyawan.append(dict_karyawan)
    with open('karyawan.json', 'r') as datafile:
        data = json.load(datafile)
        data[nama] = list_karyawan
    with open('karyawan.json', 'w') as datafile:
        json.dump(data, datafile)
    print('=== Data berhasil ditambahkan ===\n')