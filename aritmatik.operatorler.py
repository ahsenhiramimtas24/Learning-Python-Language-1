
print(3 + 5)
print(34 - 25)
print( 4*78)
print(100/5) #ondalıklı bölüyor
print(100//4) #tam sayı bölüyor
print(100 % 3) #kalanı gösteriyor
print(4**2) #üs alma işlemi
print( -10 // 4) # az olan sayıya doğru yuvarladığı için sonuç -3 olacak


#PYTHON'DA ARİTMATİK İŞLEMLER ÖNCELİĞİ
# 1. parantez ()
# 2. üslü işlemler **
# 3. çarpma ve bölme * , / , //, %
# 4. toplama ve çıkarma + , -
sonuc =  7 + 3 * 2 ** 6 - ( 10 // 4) % 3
print( "Sonuç: " , sonuc)
print(2%3) # bölen küçük olduğu için sonuç kendisi çıkacak


sayi1 = 12
sayi2 = 3
toplam = sayi1 + sayi2
 
sayi3 = 5
#toplam += sayi3 # toplam = toplam + sayi3 anlamına geliyor.
#toplam -= sayi3 # toplam = toplam - sayi3 anlamına geliyor.
#toplam *= sayi3 # toplam = toplam * sayi3 anlamına geliyor.
toplam /= sayi3 # toplam = toplam / sayi3 anlamına geliyor.
print(toplam)
print(type(toplam)) 


#sayi1 = input( Lütfen birinci sayıyı giriniz: )
#sayi2 = input( Lütfen ikinci sayıyı giriniz: )
#toplam = sayi1 + sayi2
#print( "Toplam: ", toplam) ---> Bu işlem string olarak toplama yapar, sayıları topalamz ve sırayla yazar.

sayi1 = input("Lütfen birinci sayıyı giriniz: ")
sayi2 = input("Lütfen ikinci sayıyı giriniz: ")
# input fonksiyonu string olarak alır, bu yüzden sayıları toplamak için önce integer'a çevirmemiz gerekiyor.
sayi1 = int(sayi1) # string olan sayıyı integer'a çeviriyoruz.
sayi2 = int(sayi2)
toplam = sayi1 + sayi2
print( "Toplam: ", toplam)
# int'i yazdığımız gibi float da yapabiliriz