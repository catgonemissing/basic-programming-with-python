try:
    berat_paket = float(input("Berapa berat paketmu dalam kg? "))
    
    if berat_paket < 0:
        print("Input tidak valid: Angka negatif tidak diperkenankan.")
    elif berat_paket <= 2:
        print("Biaya pengiriman adalah RP. 10,000")
    elif berat_paket <= 5:
        print("Biaya pengiriman adalah RP. 20,000")
    elif berat_paket <= 10:
        print("Biaya pengiriman adalah RP. 35,000")
    else:
        print("Berat paket melebihi batas layanan")

except ValueError:
    print("Input tidak valid: Harap masukkan angka bulat.")