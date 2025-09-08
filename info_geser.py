masukan = [input().replace(" ", "").lower() for _ in range(2)] #replace(" ", "") mengabaikan spasi
masukan[1] = masukan[1][::-1] # Reverse

data_huruf = {huruf: i+1 for i, huruf in enumerate(list("abcdefghijklmnopqrstuvwxyz"))}
assert len(masukan[0]) == len(masukan[1]), "Masukan pertama dan masukan kedua memiliki panjang yang berbeda"

jarak_per_karakter = []
for char, val in zip(masukan[0], masukan[1]):
    jarak = data_huruf[val] - data_huruf[char]
    if jarak < 0:
        jarak = 26 - jarak*(-1)
    jarak_per_karakter += [jarak] # Tidak boleh pakai append, sehingga pakai operator hehe

if len(set(jarak_per_karakter)) == 1:
    jarak_akhir = jarak_per_karakter[0] if jarak_per_karakter[0] != 0 else "0 atau 26" # Penggeseran 0 huruf dan 26 huruf sedikit ambigu
    print("Silahkan berjalan sejauh", jarak_akhir , "meter")
else:
    print("Mending pulang aja")
