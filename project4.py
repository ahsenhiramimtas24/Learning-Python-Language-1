"""
isimler = [ "Ali", "Ece", "Kaan", "Mete", "Batu", "Veli", "Ayşe"]
numaralar = ["145", "178", "164", "175", "185", "180", "134"]

max_numara = 0
max_ogrenci = ""
for i in range(len(numaralar)):
    if int(numaralar[i]) > max_numara:
        max_numara = int(numaralar[i])
        max_ogrenci = isimler[i]
print(f"En büyük numaraya sahip öğrenci: {max_ogrenci}, Numarası: {max_numara}")

min_numaara = 999
min_ogrenci = ""
for i in range(len(numaralar)):
    if int(numaralar[i]) < min_numaara:
        min_numaara = int(numaralar[i])
        min_ogrenci = isimler[i]
print(f"En küçük numaraya sahip öğrenci: {min_ogrenci}, Numarası: {min_numaara}")
"""

# 2. çözüm yolu (kısa yol)

isimler = [ "Ali", "Ece", "Kaan", "Mete", "Batu", "Veli", "Ayşe"]
numaralar = ["145", "178", "164", "175", "185", "180", "134"]

max_numara = max(numaralar)
max_index = numaralar.index(max_numara) # 4
max_ogrenci = isimler[max_index]
print(f"En büyük numaraya sahip öğrenci: {max_ogrenci}, Numarası: {max_numara}")
min_numara = min(numaralar)
min_index = numaralar.index(min_numara) # 6
min_ogrenci = isimler[min_index]
print(f"En küçük numaraya sahip öğrenci: {min_ogrenci}, Numarası: {min_numara}")



