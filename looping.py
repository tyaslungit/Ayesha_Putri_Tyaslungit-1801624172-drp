for baris in range(8):
    for kolom in range(8):
        if (baris + kolom) % 2 == 0:
            print("⬜", end="")
        else:
            print("⬛", end="")
    print()

aktivitas_list = []

jumlah = int(input("Berapa aktivitas yang ingin dimasukkan? "))

for i in range(jumlah):
    print("\nAktivitas ke-", i + 1)

    aktivitas = input("Masukkan aktivitas: ")
    durasi = input("Berapa lama aktivitas tersebut? ")

    aktivitas_list.append(aktivitas + " (" + durasi + ")")

print("\n=== DAFTAR AKTIVITAS ===")

for aktivitas in aktivitas_list:
    print("-", aktivitas)
