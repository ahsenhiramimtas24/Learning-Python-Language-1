#kullanıcıdan sıcaklığın değerini al (float)
sicaklik = float(input("Lütfen sıcaklık değerini giriniz: "))

# gerekli sıcaklık bilgisini al ve kontrol edip gerekli mesajı yazdır
if sicaklik > 37:
    print("Ateş değeriniz yüksek!.")
    print("Lütfen doktorunuza başvurunuz.")
else: 
    print("Ateş değeriniz normal.")
    print("Geçmiş olsun.")