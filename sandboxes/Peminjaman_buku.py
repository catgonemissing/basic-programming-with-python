Buku_BelumBalik = int(input("Berapa buku yang belum engkau kembalikan? "))

if Buku_BelumBalik < 3 and Buku_BelumBalik > 0:
    print("Boleh minjam buku!")
elif Buku_BelumBalik >= 3:
    print("Tidak boleh minjam buku")
else:
    print("Angka negatif dan 0 tidak boleh diinput!")