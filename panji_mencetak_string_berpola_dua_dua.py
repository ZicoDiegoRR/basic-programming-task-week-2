panjang = int(input())
isi_string = "#*"

print("".join([
    isi_string[int(num/2)%2] for num in range(panjang)
]))
