import random # from random import shuffle
              # from random import randint  şeklinde de import edebiliriz.

sayi = random.randint(1,100)
print("Tutulan sayı: ", sayi)  

#shuffle(list) => verilen listedeki elemanları rastgele karıştırır.

isimler = ["Ahsen", "Zeynep", "Emel", "Nisa", "Eylül"]
print("Karıştırmadan önce isimler: ", isimler)

random.shuffle(isimler)

print("Karışık isimler: ", isimler)