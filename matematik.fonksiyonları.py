x = 4.6

print(round(x)) # x sayısını en yakın tam sayıya yuvarlar

y= 4.678
print(round(y,2)) # y sayısını virgülden sonra 2 basamağa yuvarlar => 4.68
print(round(y,3)) # y sayısını virgülden sonra 3 basamağa yuvarlar => 4.678
print(round(y,1)) # y sayısını virgülden sonra 1 basamağa yuvarlar => 4.7

z = -10
print(abs(z)) # z sayısının mutlak değerini alır => 10


import math

print(math.floor(4.6))  #4.6 sayısını en küçük tam sayıya yuvarlar => 4

print(math.ceil(4.6))   #4.6 sayısını en büyük tam sayıya yuvarlar => 5

print(math.sqrt(16))   #16 sayısının karekökünü alır => 4.0

print(math.pow(2, 3))  #2 sayısının 3. kuvvetini alır => 8.0

#log =>> math.log(x, base) x sayısının base tabanındaki logaritmasını alır

print(math.log(100, 10))  # 100 sayısının 10 tabanındaki logaritması => 2.0
print(math.log(8, 2))    #ln(8) / ln(2) => 3.0
