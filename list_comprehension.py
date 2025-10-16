# List Comprehension (Liste Üretimi)

# 1'den 10'a kadar sayıların karesini üreten liste.
kareler = []
for x in range(1,11):
    kareler.append(x**2)

print(kareler)

#list comprehension ile aynı işlemi şu şekilde yapıyoruz:
kareler = [x**2 for x in range(1,11)]
print(kareler)


sayilar = [1,2,3,4,5,6,7,8,9,10]
ciftler = []

for x in sayilar:
    if x % 2 == 0:
        ciftler.append(x)  

print(ciftler)

# List Comprehension ile:
ciftler = [x for x in sayilar if x % 2 ==0]
print(ciftler)

#veya

ciftlerin_karesi = [x**2 for x in sayilar if x % 2 ==0]
print(ciftlerin_karesi)

# kelimeleri büyük harfe çevirme işlemi
kelimeler = ["python", "java", "csharp", "javascript"]
buyuk_harfler = []

for kelime in kelimeler:
    buyuk_harfler.append(kelime.upper())
print(buyuk_harfler)

# List Comprehension ile:
buyuk_harfler = [kelime.upper() for kelime in kelimeler]
print(buyuk_harfler)