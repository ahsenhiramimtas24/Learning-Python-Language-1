sayi1 = input( "Lütfen birinci notu giriniz: ")
sayi2 = input( "Lütfen ikinci notu giriniz: ")
sayi3 = input( "Lütfen üçüncü notu giriniz: ")

toplam = int(sayi1) + int(sayi2) + int(sayi3)
ortalama = toplam / 3

sonuc = round(ortalama,1)

print(f"Not ortalamanız: {sonuc}")