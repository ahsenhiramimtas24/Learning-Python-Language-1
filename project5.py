while True:
    print("\n -------- MENÜ --------")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")

    secim = input("Bir işlem seçin (1-5): ")

    if secim == '5':
        print("Çıkış yapılıyor...")
        break
    if secim in ['1', '2', '3', '4']:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        
        if secim == '1':
            sonuc = sayi1 + sayi2
            print(f"{sayi1} + {sayi2} = {sonuc}")
        elif secim == '2':
            sonuc = sayi1 - sayi2
            print(f"{sayi1} - {sayi2} = {sonuc}")
        elif secim == '3':
            sonuc = sayi1 * sayi2
            print(f"{sayi1} * {sayi2} = {sonuc}")
        elif secim == '4':
            if sayi2 != 0:
                sonuc = sayi1 / sayi2
                print(f"{sayi1} / {sayi2} = {sonuc}")
            else:
                print("Hata: Bir sayı sıfıra bölünemez.")
    else: 
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        continue

   
    print("Hoşçakalın!")