# for döngüsü ödev

baslangic = int(input("Başlangıç sayısını giriniz: "))
bitis = int(input("Bitiş sayısını giriniz: "))  

toplam = 0
print("Tek sayılar:")

for sayi in range(baslangic, bitis + 1):
    if sayi % 2 !=0:
        print(sayi)
        toplam += sayi

print( "Tek sayıların toplamı:", toplam)
