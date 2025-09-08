panjang = int(input())
isi_string = "#*" if panjang % 2 == 1 else "*#"

string = [isi_string[num%2] for num in range(panjang)]
print(*string)
