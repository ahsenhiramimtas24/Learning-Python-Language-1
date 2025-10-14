#
# FOR DÖNGÜSÜ
# - Bir veri yapısının ( liste vb.) veya belirli bir sayı aralığının üzerinde sıralı
#   olarak gezinmemizi sağlayan bir döngü yapısıdır.
#
# - Tekrarlı görevleri otomatikleştirmede kullanılır.
#
# - Kullanım formatı:
#
#    for gecici_degisken in koleksiyon:
#      yapılacak işlemler1
#      yapılacak işlemler2
#      ...

meyveler = ["Elma" , "Armut" , "Muz" , "Çilek"]

for meyve in meyveler:
    print(meyve)
    print( "Benim en sevdiğim meyvelerden biri" , meyve )

print("\nbye...")

# range() fonksiyonu => range(stop) = range(5) => 0,1,2,3,4
#                     => range(start, stop) = range(2,5) => 2,3,4
#                     => range(start, stop, step) = range(2,10,2) => 2,4,6,8

for sayi in range(5):
    print(sayi)

# range() fonksiyonunu kullanarak otomatik bir liste oluşturma:
tam_sayilar = list(range(5))
print(tam_sayilar)

# SORU
# 1'den 100'e kadar olan sayılardan çift olanları ekrana yazdıran programı for döngüsü

toplam = 0
for sayi in range(1,101):
    toplam = toplam + sayi
    print(sayi)
print("Toplam: ", toplam)

print("\nbye...")
    
