# Ask for status first and format the string to handle uppercase/lowercase/spaces
status = input("Apakah kamu mahasiswa aktif? (ya/tidak): ").strip().lower()

if status == "tidak":
    print("Tidak memenuhi syarat")
elif status != "ya":
    print("Input salah: Harap masukkan 'ya' atau 'tidak'.")
else:
    # Only ask the rest of the questions IF they are an active student
    try:
        penghasilan_ortu = int(input("Berapa penghasilan orang tuamu? (Rupiah): "))
        ipk = float(input("Berapa IPKmu?: "))
        prestasi = input("Apakah punya prestasi? (ya/tidak): ").strip().lower()

        if ipk >= 3.50:
            if penghasilan_ortu <= 4000000:
                print("Beasiswa penuh")
            else:
                print("Beasiswa parsial")
                
        elif 3.00 <= ipk < 3.50 and penghasilan_ortu <= 4000000 and prestasi == "ya":
            print("Beasiswa parsial")
            
        else:
            print("Tidak memenuhi syarat beasiswa") 

    except ValueError:
        print("Harap masukkan angka yang valid untuk penghasilan dan IPK!")