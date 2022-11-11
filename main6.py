from main0 import b

if b == 5:
    print('''Siz Funksiya mavzusini tanladingiz.
    Funksiya pythonda def bilan belgilanadi, boshqa dastur tillarida funcsion ko'rinishida bo'ladi.
    Funksiya qavslari ichidagi o'zgaruvchilar uning argumentlari hisoblanadi.
    Funksiya argumentlari faqat funksiya ichida ishlaydi.
    ''')

    print("Sizga misollar keltiraman.")

    a = int(input("1-sonni kiriting: "))
    b = int(input("2-sonni kiriting: "))
    amal = input("amalni tanlang: ")

    def calc(a,b):
        if amal == "+":
            print("natijangiz: ", a + b )
        elif amal == "*":
            print("natijangiz: ",a * b)
        elif amal == "-":
            print("natijangiz: ",a- b)
        elif amal == "/":
            print("natijangiz: ", a / b)
        else:
            print("amalni xato kiritdingiz")
    calc(a,b) 

    print("Sizga vazifa funksiyada huddi hozirgidek calc tuzing.")                       

