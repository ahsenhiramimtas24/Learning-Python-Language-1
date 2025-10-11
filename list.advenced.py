"""
otel_zinciri_1 = [ "Ankara", "İstanbul"]
otel_zinciri_2 = ["İzmir", "Antalya"]
otel_zincirleri = otel_zinciri_1 + otel_zinciri_2
# print(otel_zincirleri)

abc_turizm = [ otel_zinciri_1, otel_zinciri_2]
print(type(abc_turizm))
print(type(abc_turizm[0][1])) # İstanbulu verir
otel_zinciri_1[0] = "Bursa"
print(abc_turizm)


liste1 = [ "Ali Kaya", 75, [ 60, 30, 90]]

liste1[2][2] = 100
print(liste1)

list1 = [ 30, 45, 80, 90]
print(list1[len(list1)-1]) # son elemanı verir
                            
                           # best practice
"""

# : : operatörü (Sliciing - dilimleme)
#    Bir diziyi (string, liste, vb.) belirli bir aralıkta veya belirli bir adımla almak demektir.

meyveler = [ "elma", "armut", "muz", "çilek", "karpuz", "kavun"]

# 2. indeksten başlayarak 5. indekse kadar (5. indeks dahil değil)
orta_meyveler = meyveler[2:5]
print(orta_meyveler) # ['muz', 'çilek', 'karpuz']

# ilk 3 meyveyi alalım.
ilk_uc = meyveler[:3]
print(ilk_uc) # ['elma', 'armut', 'muz']

son_uc = meyveler[-3:] # sondan 3 elemanı alır
print(son_uc)

meyveler_2_3_sondan = meyveler[-3:-1] # sondan 3. ile sondan 1. arasını alır (sondan 1. dahil değil)
print(meyveler_2_3_sondan)

cift_indeksler = meyveler[::2] # baştan sona kadar 2 şer atlayarak alır
print(cift_indeksler) # ['elma', 'muz', 'karpuz']

ters_meyveler = meyveler[::-1] # baştan sona kadar -1 er atlayarak alır yani ters çevirir
print(ters_meyveler) 

meyveler_2 = meyveler[::] # baştan sona kadar alır (kopyasını oluşturur)
meyveler_kopya = meyveler.copy() # baştan sona kadar alır (kopyasını oluşturur)
print(meyveler_2)
print(meyveler_kopya) #aynı şeyi verirler.

meyveler_3 = meyveler # bu şekilde atama yaparsak kopya oluşturulmaz, referans atanır.
print(meyveler_3)
meyveler_3[0] = "karadut"
print(meyveler) # meyveler listesinin de ilk elemanı değişir.

