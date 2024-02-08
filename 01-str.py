'''
Kullanıcıdan girdi almak için input kullanırız. Bunu JS'de prompt ile yapıyorduk.

docs.python.org, python ile ilgili tüm dökümantasyonların tutulduğu yerdir.

'''

name = input("What's your name?")

# end="" operatörü satırı alıp bir alt satıra taşır. Bu sayede 2 print yazısıda aynı satırda gözükür.
print("hello,", end="")
print(name)

# sep="" operatörü ayırıcı işlevi görür
print("Hi!", name, sep="???")

# Kaçış çizgisi kullanarak çizgileri anlamlı kılmak
print("hello! \"friend\"")


# Değişlenleri yazdırmak

print(f"hello!,", {name})

# STR Methods

names = input("What's your name? :")

# strip(), Dizedeki fazladan olan boşlukları kaldırır.
names = names.strip()
print(f"Hello my frineds", {names})

# capitalize(), girilen verinin sadece ilk harfini büyük harf ile başlamasını sağlar.
names = names.capitalize()
print(f"Büyük harf:", names)

# title(), girilen verinin başlangıç harflerini büyük harf ile yazar.

names = names.title()
print(f"Big Title:", {names})

# Tüm Methodsları birleştirirek yazmak

names = names.strip().title()
print(f"Methods with: ", names)

# Ve daha kısa bir hali

job = input("What's your job? :").strip().title()



