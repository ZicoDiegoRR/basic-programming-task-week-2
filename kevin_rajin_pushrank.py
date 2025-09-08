#@markdown Kevin Rajin Pushrank
masukan = int(input("Masukkan skor: "))
rank_skor = {
    "Bronze": 899,
    "Warrior": 1097,
    "Mythic": 3500,
    "Legend": 4737,
    "Epic": "Infinite" # akan diprint ketika mencapai elemen ini pada loopnya
}

for rank, skor in rank_skor.items():
    if masukan <= skor or rank == list(rank_skor.keys())[-1]:
        print(rank)
        break
