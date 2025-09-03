"""
x = 10
y = 9

print(x == y)  #eşit mi?
print(x != y)  #eşit değil mi?

if x < y:
    print("x, y'den küçüktür.")
else :
    print("x, y'den büyüktür.")

# and kullanımı

yas = 10

if yas > 18 and yas < 35:
    print("Genç Yetişkin.")
else: 
    print("Genç Yetişkin değil.")


# or kullanımı

hava_sicakligi = 40

if hava_sicakligi < 25 or hava_sicakligi > 35:
    print("Dışarı çıkmak için uygun değil.")    
else:
    print("Dışarı çıkmak için uygun.")
"""

# not kulllanımı

gunluk_odev_var_mi = False

if not gunluk_odev_var_mi:
    print("Oyun oynayabilirsin.")
else:
    print("Önce ödevini yapmalısın.") 

