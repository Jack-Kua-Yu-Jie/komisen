jumlah = 0
jualan = 0
komisen = 0
ulang = "Y"
while ulang == "Y":
    jualan = float(input("Masukkan jumlah jualan: RM"))
    if jualan > 80:
        kadar_komisen = 0.055
    elif jualan > 70:
        kadar_komisen = 0.05
    elif jualan > 60:
        kadar_komisen = 0.04
    elif jualan > 50:
        kadar_komisen = 0.03
    else:
        kadar_komisen = 0.02
    komisen = jualan*kadar_komisen
    print("Komisen anda ialah RM",komisen)
    jumlah = jumlah + komisen
    ulang = str(input("Masukkan Y untuk teruskan pengiraan atau N untuk hentikan pengiraan."))
print("\nJumlah komisen ialah RM",round(jumlah,2))
print("...Anda telah selesai membuat pengiraan...")
