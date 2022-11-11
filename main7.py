from main0 import b
 
if b == 6:
    print('''Siz Exception mavzusini tanladingiz.
    Bu try va except ga bo'linadi'
    try faqat to'g'ri kod yozish uchun,
    except esa xatoliklar bilan ishlash uchun kerak bo'ladi.
    ''') 

    print("Sizga misollar keltiraman.")

    try:
        a = input("Loginingizni kiriting: ")
        b = int(input("Parolingizni kiriting: "))
        if a == "guli" and b == 2103:
            print("Siz tizimga muvaffaqiyatli kirdingiz")
        elif a == "guli" and b != 2103:
            print("Parolingiz xato")
        elif a != "guli" and b == 2103:
            print("Loginingiz xato ")
        else:
            print("Login va parolingiz xato")
    except ValueError:
        print("Parolga harf kiritdingiz")
    except:
        print("Qandaydir xatolik bor")  

    print("Sizga vazifa hozir exceptga kiritgan ValueError xatoligimdan 6 ta turli xilidan chiqaring")

        
