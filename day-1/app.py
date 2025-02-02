# region Değişkenler ve Veri Tipleri

# variable -> Değişken

"""
değişkenler tekrarlı kullanılan verileri bir yerde tutup gerektiğinde çağırabilmemizi sağlar ve ayrıca onu değiştirmeyi kolaylaştırır.

print("hi") bu çok fazla yerde tekrar tekrar kullandıgımızda değiştirmemiz gerekirken işlemi zorlaştırır

x = "hi"

print(x) bu şekilde değişken atayarak daha kolay bir şekilde değiştirebiliriz.

bazı dillerdeki gibi ön tanımlı veri tipi belirtme zorunluluğu yoktur.

int x = 5; veya string name = "Ali"; gibi bir kullanım yoktur.

x = 5 veya name = "Ali" şeklinde kullanılır. 
"""

x = 5
print(x)  

x = "Ali"
print(x)

# x tekrar tanımlandığı için hata vermez çünkü kod okunurken en son tanımlanan x değeri alınır.

# type() -> Değişkenin tipini öğrenmek için kullanılır.

y = 5.5
z = "Ali"
a = True

print(type(x), type(y), type(z), type(a))

# Değişken atarken dikkat edilmesi gereken kurallar:
# 1. Değişkenler özel karakter ve sayı ile başlayamaz, sadece harfler ve alt çizgi (_) ile başlayabilir.
# 2. Python'un anahtar kelimeleri değişken adı olarak kullanılamaz.
# 3. İsimlendirme formatları önemlidir. En yaygın olarak snake_case kullanılır.

customer_name = "Ali" # snake_case
customerName = "Ali" # camelCase
CustomerName = "Ali" # PascalCase

# numbers -> Sayılar

# Python'da int, float ve complex olmak üzere 3 sayı türü vardır.

x = 5 # int (Tamsayı)
y = 5.5 # float (Ondalıklı sayı)
z = 2 + 3j # complex (Karmaşık sayı, nadir kullanılır)

# int ve float birbirine dönüştürülebilir ve birlikte işlem yapılabilir.
print(x + y)  # 10.5 

# str -> Metin (String)

text = "Merhaba, Python!"
print(text)

# String birleştirme
name = "Ali"
greeting = "Merhaba, " + name
print(greeting)

# String çoğaltma
print("Python! " * 3) # "Python! Python! Python! "

# str methodları
print(text.upper())  # Bütün harfleri büyük yapar.
print(text.lower())  # Bütün harfleri küçük yapar.
print(text.replace("Python", "Dünya"))  # Belirtilen metni değiştirir.

# bool -> Mantıksal (Boolean)

a = True
b = False
print(a and b)  # False
print(a or b)   # True

# list -> Liste

my_list = [1, 2, 3, "Ali", 5.5]
print(my_list[0])  # 1\my_list.append(10)  # Listeye eleman ekler
print(my_list)

# dict -> Sözlük (Dictionary)

my_dict = {"isim": "Ali", "yaş": 25}
print(my_dict["isim"])  # "Ali"

# region Operatörler

# Aritmetik Operatörler
x = 10
y = 3
print(x + y)  # Toplama
print(x - y)  # Çıkarma
print(x * y)  # Çarpma
print(x / y)  # Bölme
print(x // y) # Tam sayı bölme
print(x % y)  # Mod (Kalanı bulma)
print(x ** y) # Üst alma

# Karşılaştırma Operatörleri
print(x == y)  # Eşit mi?
print(x != y)  # Eşit değil mi?
print(x > y)   # Büyük mü?
print(x < y)   # Küçük mü?
print(x >= y)  # Büyük veya eşit mi?
print(x <= y)  # Küçük veya eşit mi?

# Mantıksal Operatörler
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# endregion

# region Tip Dönüşümleri

# int() -> Tam sayıya dönüştürme
print(int(5.9))

# float() -> Ondalıklı sayıya dönüştürme
print(float(5))

# str() -> Metin tipine dönüştürme
print(str(10))

# endregion

# region Egzersizler

# 1. Kullanıcıdan iki sayı alıp dört işlem yapan bir program yaz.
a = float(input("Birinci sayıyı girin: "))
b = float(input("İkinci sayıyı girin: "))
print(f"Toplam: {a + b}")
print(f"Çıkarma: {a - b}")
print(f"Çarpma: {a * b}")
print(f"Bölme: {a / b}")

# hesap_makinesi()

# 2. Girilen metni ters çeviren bir kod yaz.
# ilerideki konuları içerir.
def reverse_text(text):
    return str(text).strip()[::-1]

print(reverse_text("Ali"))

# endregion
