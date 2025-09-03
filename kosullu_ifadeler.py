#kullanıcıdan sıcaklığın değerini al (float)
"""
sicaklik = float(input("Lütfen sıcaklık değerini giriniz: "))

#gerekli sıcaklık bilgisini al ve kontrol edip gerekli mesajı yazdır

if sicaklik > 37:
    print("Ateş değeriniz yüksek!.")
    print("Lütfen doktorunuza başvurunuz.")
else: 
    print("Ateş değeriniz normal.")
    print("Geçmiş olsun.")

sayi = 8

if  sayi > 0:
    print("Sayı pozitiftir.")
elif sayi < 0:
    print("Sayı negatiftir.")
else: 
    print("Sayı sıfırdır.")
   """

#daha dikkatli sıcaklık ölçümü

sicaklik = float(input("Lütfen sıcaklık değerini giriniz: "))

if sicaklik < 36.1:
    print( " Sıcaklık değeri düşük, hipotermi riski var.")
elif sicaklik <= 37.2:
    print("Sıcaklık değeri normal.")
elif sicaklik <= 38.0:
    print("Sıcaklık değeri hafif yüksek, dikkatli olun.")
elif sicaklik <= 39.0:
    print("Sıcaklık değeri yüksek, dinlenin ve bol sıvı alın.")
else:
    print("Sıcaklık değeri çok yüksek, acilen tıbbi yardım alın.")