Status = input("Apakah kamu mahasiswa aktif? (Ya/Tidak) ")
Penghasilan_ortu = int(input("Berapa penghasilan orang tuamu? (Rupiah) "))
IPK = float(input("Berapa IPKmu? "))
Prestasi = ("Apakah punya prestasi? (Ya/Tidak)")

if Status == "Ya" :
    if Penghasilan_ortu <= 4000000 and IPK >= 3.50:
        print("Beasiswa penuh")
    elif Penghasilan_ortu >4000000 and IPK >= 3.50:
        print("Beasiswa parsial")
    elif IPK >= 3.00 and IPK <= 3.50 and Penghasilan_ortu < 4000000 and Prestasi == "Ya":
        print("Beasiswa parsial")
    else :
        print("Anda memiliki salah input")
elif Status == "Tidak":
    print("Tidak memenuhi syarat")
else :
    print("anda memiliki salah input")