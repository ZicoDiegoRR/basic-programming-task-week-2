n, m = map(int, input().split())

for i in range(n):
    isi_string = "#*" if i % 2 == 1 else "*#"
    print(*[isi_string[num%2] for num in range(m)])
