#@markdown Huruf Dikali
masukan = input().replace(" ", "").lower()
# lower() membuat semua huruf menjadi huruf kecil

data_huruf = {ch: i+1 for i, ch in enumerate(list("abcdefghijklmnopqrstuvwxyz"))} # membuat elemen dictionary dengan menggunakan looping

hasil = 1
for huruf in masukan:
    hasil *= data_huruf[huruf]

print(hasil)
