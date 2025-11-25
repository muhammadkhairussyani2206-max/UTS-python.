try:
    nilai = int(input("masukkan nilai 10 digit:"))

    if 0<= nilai <= 9999999999:
        miliaran = nilai // 1000000000
        sisa_miliaran = nilai % 1000000000

        ratusan_juta = sisa_miliaran // 100000000
        sisa_ratusan_juta = sisa_miliaran % 100000000

        puluhan_juta = sisa_ratusan_juta // 10000000
        sisa_puluhan_juta = sisa_ratusan_juta % 10000000

        jutaan = sisa_puluhan_juta // 1000000
        sisa_jutaan = sisa_puluhan_juta  % 1000000

        ratusan_ribu = sisa_jutaan // 100000
        sisa_ratusan_ribu = sisa_jutaan % 100000

        puluhan_ribu = sisa_ratusan_ribu // 10000
        sisa_puluhan_ribu = sisa_ratusan_ribu % 10000

        ribuan = sisa_puluhan_ribu // 1000
        sisa_ribuan = sisa_puluhan_ribu % 1000

        ratusan = sisa_ribuan // 100
        sisa_ratusan = sisa_ribuan % 100

        puluhan = sisa_ratusan // 10
        sisa_puluhan = sisa_ratusan % 10

        satuan = sisa_puluhan // 1
        sisa_satuan = sisa_puluhan % 1

    if nilai >=1000000000:
        print(f"{miliaran} merupakan miliaran")

    if nilai >=100000000:
        print(f"{ratusan_juta} merupakan ratusan juta")

    if nilai >=10000000:
        print(f"{puluhan_juta} merupakan puluhan juta")  
   
    if nilai >= 1000000:
        print(f"{jutaan} merupakan jutaan")

    if nilai >= 100000:
        print(f"{ratusan_ribu} merupakan ratusan ribu")

    if nilai >= 10000:
        print(f"{puluhan_ribu} merupakan puluahan ribu")

    if nilai >= 1000:
        print(f"{ribuan} merupakan ribuan")

    if nilai >= 100:
        print(f"{ratusan} merupakan ratusan")

    if nilai >= 10:
        print(f"{puluhan} merupakan puluhan")

    if nilai >= 1:
        print(f"{satuan} merupakan satuan")

    else:
        print("masukkan ulang")
except ValueError:
    print("tidak valid")