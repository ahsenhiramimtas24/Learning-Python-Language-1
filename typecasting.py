# Python'da Type Cast / Tür dönüşümü
## Implict Type Casting

a = 10 # int
b = 2.5 # float
print( a + b ) # int -> float'a çevrilir.
sonuc = a + b
print(sonuc)
print(type(sonuc))


## Explicit Type Casting

x = "123"
y = int(x) # str -> int ddönüştürülür.
print(type(y))
print( y + 7) 

a = 10
b = "10"
print(a + int(b))