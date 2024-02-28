x = int(input("What's x?"))
y = int(input("What's y?"))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("Ne yazdın sen??")

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

if x != y:
    print("x ve y birbirine eşit değildir")


score = int(input("What's score?:"))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score <70:
    print("Grade: D")
else:
    print("Grade: F")

"""
+
-
*
/
%

"""

number = int(input("What's number?:"))

if number % 2 == 0:
    print("Çift Sayıdır")
else:
    print("Tek Sayıdır")

def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()


# match

name = input("What's your name?:")

if name == "Harry":
    print("Gyrffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Grtffindor")
elif name == "Draco":
    print("Slytherin")
else: 
    print("Who?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gyrffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")