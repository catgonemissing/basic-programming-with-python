Buku_dikembalikan = int(input("Masukkan buku yang engkau belum kembalikan:  "))

try:
    if Buku_dikembalikan < 0:
        print("Input tidak valid: Angka negatif tidak diperkenankan.")
    elif Buku_dikembalikan < 3:
        print("Boleh minjam buku!")
    else:
        print("Tidak boleh minjam buku")

except ValueError:
    print("Input tidak valid: Harap masukkan angka bulat.")