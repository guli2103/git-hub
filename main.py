try:
    import time
   
    ism = input("Ismingizni kiriting: ")
    fam = input("Familiyangizni kiriting: ")
    login = input("Loginingizni kiriting: ") 
    parol = int(input("Parolingizni kiriting: "))
    email = input("Emailingizni kiriting: ")
    if login == "guli" and parol == 2103 and email == "guli@gmail.com":
        print("Siz tizimga muvaffaqiyatli kirdingiz ")
    elif login == "guli" and parol == 2103 and email != "guli@gmail.com":
        print("Siz emailni xato kiritdingiz. 5 soniya kuting")
        a = 0
        while a < 5:
            a += 1
            time.sleep(1)
            print(a)
        print("5 soniya tugadi.Qaytadan urinib ko'ring")
    elif login == "guli" and parol != 2103 and email == "guli@gmail.com":
        print("Siz parolni xato kiritdingiz. 10 soniya kuting")
        b = 0
        while b < 10:
            b += 1
            time.sleep(1)
            print(b)
        print("10 soniya tugadi. Qaytadan urinib ko'ring ") 
    elif login != "guli" and parol == 2103 and email == "guli@gmail.com":
        print("Siz loginni xato kiritdingiz. 15 soniya kuting ")
        for x in range(15):
            time.sleep(1)
            print(x)
        print("15 soniya tugadi.Qaytadan urinib ko'ring")
    elif login == "guli" and parol != 2103 and email != "guli@gmail.com":
        print("Siz parol va emailni xato kiritdingiz. 20 soniya kuring")
        for x in range(20):
            time.sleep(1)
            print(x)
        print("20 soniya tugadi,qaytadan urinib ko'ring")
    elif login != "guli" and parol != 2103 and email == "guli@gmail.com":
        print("Siz login va parolni xato kiritdingiz, 25 soniya kuting")
        for x in range(25):
            time.sleep(1)
            print(x)
        print("25 soniya tugadi, qaytadan urinib ko'ring")
    elif login != "guli" and parol == 2103 and email != "guli@gmail.com":
        print("Siz login va emailni xato kiritdingiz, 30 soniya kuting ")
        c = 0 
        while c < 30:
            c += 1
            time.sleep(1)
            print(c)
        print("30 soniya tugadi, qaytadan urinib ko'ring")
    else:
        print("Siz login,parolva emailni xato kiritdingiz.60 soniya kuting")
        for x in range(60):
            time.sleep(1)
            print(x)
        print("60 soniya tugadi,Qaytadan urinib ko'ring")  
except ValueError:
    print("Siz string ma'lumot turi kiritgansiz")
except:
    print("Qandaydir xatolik bor")                              


