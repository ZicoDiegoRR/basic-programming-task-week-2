n, m = list(map(int, input().split()))
isi = {"keys": "*#", "*": 0, "#": 1}

string = []
for i in range(n):
    if not string:
        string = [isi["keys"][int((num)/2)%2] for num in range(m)]
    else:
        string = [isi["keys"][isi[huruf] - 1] for huruf in string]
    print(*string)
