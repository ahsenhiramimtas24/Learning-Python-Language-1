"""
- Programlarda döngüler (loops), belirli bir koşul sağlandığı sürece tekrar eden işlemleri 
yürütmek için kullanılır.

WHILE DÖNGÜSÜ, belirtilen bir koşul true olduğu sürece çalışmaya devam eder.
Koşul False olduğunda döngü sona erer. İşleyişi şu şekildedir:

while koşul:
    yap-işlem1
    yap-işlem2
    yapişlem3,
    ...

- Hangi durumda while döngüsü tercih edilmelidir?
    Döngü sayısı belli değilse veya Koşula bağlı tekrar eden işlemler için.

- For Döngüsü genellikle belirli bir sayıda işlem tekrar ettiğinde kullanılır.
    Örneğin; bir liste veya dizi elemanlarını tektek yazdırmak için for daha uygundur.

    """

sayi = 0 
toplam = 0

while sayi < 10:
    toplam += sayi
    #sayi += 1

print(toplam)