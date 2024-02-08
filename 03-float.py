# Float Data Type - Ondalıklı Sayı

x = float(input("What's x?"))
y = float(input("What's y?"))

print(x + y)

# round Methodu: Veriyi en yakın tam sayıya yuvarlamaya yarar.

z = round(x + y)
print(z)
print(f"{z:,}") # bu şekilde verilen sayıya "," işareti koyarak floata çevirir.

k1 = float(input("What's k1?"))
k2 = float(input("What's k2?"))

# 2, kaç basamaklı olmasını istediğimi döndürür
k_result = round (k1 / k2, 2)
print(k_result)
