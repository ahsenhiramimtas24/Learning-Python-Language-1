#lists
#
# Birden fazla veriyi sıralı ve değiştirilebilir bir şekilde tutmak için kullanılır.
"""
sinav_notlari = [90 , 70 , 27 , 45 , 80]
print(sinav_notlari)
print(type(sinav_notlari))
print(type(sinav_notlari[1]))
sinav_notlari[1] = 75.9
print(sinav_notlari)
print(type(sinav_notlari[1]))
"""

sehirler = ["İstanbul" , "Ankara" , "İzmir" ]
print(len(sehirler)) # listede kaç eleman var

sehirler.append("Bursa") # listeye eleman ekleme
print(sehirler)

sehirler.insert(1,"Antalya") # listeye eleman ekleme
print(sehirler)

sehirler.extend(["Adana","Trabzon"]) # listeye birden fazla eleman ekleme
print(sehirler)

sehirler.remove("Adana") # listeden eleman silme
print(sehirler)

sehirler.pop() # listeden sondaki elemanı siler
print(sehirler)

sehirler.pop(2) # listeden belirtilen indexteki elemanı siler
print(sehirler)

#index
if "Aydın" in sehirler:
    indeks = sehirler.index("Aydın")
    print(indeks)
else: 
    print("Aydın listede yok!")

adet = sehirler.count("İzmir") # listede belirtilen elemanın kaç tane olduğunu sayar
print(adet)

sehirler.sort() # listeyi alfabetik olarak sıralar
print(sehirler)

sehirler.reverse() # listeyi ters çevirir
print(sehirler) 

sehirler.clear() # listeyi temizler
print(sehirler)

