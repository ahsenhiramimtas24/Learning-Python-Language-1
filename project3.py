"""
tamsayi = int(input("Lütfen bir tamsayı giriniz: "))
çiftsayi = tamsayi % 2

if tamsayi > 20 and tamsayi != çiftsayi:
    print("Sayı 20'den büyük ve tek sayıdır.")
else: 
    print("Sayı istenilen kriterleri karşılamıyor.")

"""

tamsayi = int(input("Lütfen bir tamsayı giriniz: "))
teksayi = tamsayi % 2 == 1

if tamsayi > 20 and teksayi:
    print(f"{tamsayi},20'den büyük ve tek sayıdır.")
else: 
    print(f"{tamsayi},sayı istenilen kriterleri karşılamıyor.")