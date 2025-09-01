#kullanıcıdan sıcaklığın değerini al (float)
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