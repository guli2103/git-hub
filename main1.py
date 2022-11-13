try:
    a = input('''Salom. 
    Siz python kurslari saytiga kirdingiz.
    Darslarimizga qatnashmoqchi bo'lsangiz quyidagilardan birini tanlang:
    Ha
    Yoq
    ''')
    if a.lower() == "ha":
        ism = input("Ismingizni kiriting: ")
        familiya = input("Familiyangizni kiriting: ")
        email = input("Emailingizni kiriting: ")
        tel = int(input("Telefon raqamingizni kiriting: "))
        print(ism,familiya, "siz bizning python kursimizga kirdingiz, to'liq ma'lumotni bilish uchun adminlarimiz bilan bog'lansangiz bo'ladi")
    elif a.lower() == "yoq":
        print("Kuningiz hayrli o'tsin")
    else:
        print("xatolik bor") 


    from main2 import *
    from main3 import *
    from main4 import *
    from main5 import *
    from main6 import *
    from main7 import *
    from main8 import *
    from main9 import *

except ValueError:
    print("Siz text ma'lumot turi kiritdiz")


