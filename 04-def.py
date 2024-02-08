# Define - def , Kendi fonksiyonumuzu yazmak

# def ile kendi fonksiyonumuzu yazabiliriz. İki nokta (:)'dan sonra altında bulunanlar fonksiyonun bir parçasıdır.
def hello(to): # to, parametredir
    print("hello,", to)

name = input("What's your name?:")
# hello fonksiyonunun aldığı parametreyi name ile eşitledik. name değişkenini argüman olarak ilettik.
hello(name)


# Functionun aldığı argümanı içeride bir veriye eşitleyebiliriz.
def func(arg = "Ozan"):
    print("Hi!,", arg)

func()



# SCOPE - Kapsam
# Burada hata almamım sebebi, myName func, sadece içerisinde bulunan func'da çalışır.
'''

def main():
    myName = input("What's your name ?")
    hi()


def hi():
    print("hello", myName)

main()

'''


# Ancak bu kullanım sırasında hi2 func bir argüman aldığı için, main içerisinde hi2(myname) ile bu sorunu çözmüş oluyoruz.
def main2():
    myname = input("What's your name?")
    hi2(myname)

def hi2(to):
    print("hello", to)


# RETURN - DÖNÜŞ

# karesini döndüren func
def mainCal():
    x = int(input("What's x?"))
    print("x squared is", square(x))

# bir sayının karesi kendisinin çarpımına eşittir.
def square(n):
    return n * n # n ** 2 ya da pow(n,2) şeklinde yazılabilir
    
mainCal()

