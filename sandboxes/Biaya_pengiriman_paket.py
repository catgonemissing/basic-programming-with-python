Berat_paket = int(input("Berapa berat paketmu dalam kg? "))

if Berat_paket <= 0:
    print("Negatif dan 0 tidak boleh!")
elif Berat_paket > 0 and Berat_paket <= 2:
    print("Biaya pengiriman adalah RP. 10,000")
elif Berat_paket > 2 and Berat_paket <= 5:
    print("Biaya pengiriman adalah RP. 20,000")
elif Berat_paket > 5 and Berat_paket <= 10:
    print("Biaya pengiriman adalah RP. 35,000")
else:
    print("Berat paket melebihi batas layanan")