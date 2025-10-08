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
"""

liste1 = [ "Ali Kaya", 75, [ 60, 30, 90]]

liste1[2][2] = 100
print(liste1)

list1 = [ 30, 45, 80, 90]
print(list1[len(list1)-1]) # son elemanı verir
                            
                           # best practice