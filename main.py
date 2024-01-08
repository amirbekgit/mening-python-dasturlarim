#kankuliyator dasturi

amallar = input('+/-/x/: |')

if amallar == "+":
    print("siz qo`shish amalini tanladingiz")
    a = input("Birinchi ihtiyoriy sonni kiriting: ")
    b = input("Ikkinchi ihtiyoriy sonni kiriting: ")

    c = int(a) + int(b)

    print('Natija: ', c)


if amallar == "-":
    print("siz ayirish amalini tanladingiz")
    a = input("Birinchi ihtiyoriy sonni kiriting: ")
    b = input("Ikkinchi ihtiyoriy sonni kiriting: ")

    c = int(a) - int(b)

    print('Natija: ', c)
    

if amallar == "x":
    print("siz ko`paytirish amalini tanladingiz amalini tanladingiz")
    a = input("Birinchi ihtiyoriy sonni kiriting: ")
    b = input("Ikkinchi ihtiyoriy sonni kiriting: ")

    c = int(a) * int(b)

    print('Natija: ', c)
    

if amallar == ":":
    print("siz bo`lish amalini tanladingiz")
    a = input("Birinchi ihtiyoriy sonni kiriting: ")
    b = input("Ikkinchi ihtiyoriy sonni kiriting: ")

    c = int(a) / int(b)

    print('Natija: ', c)