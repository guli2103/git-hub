from main0 import b

if b == 2:
    print('''Siz shart operatorlari mavzusini tanladingiz.
    Shart operatorlari quyidagilar:
    if elif va else 
    if -- bu  agar degan ma‘noni bildiradi, ifdan faqatgina kiritadigan kodlarimizni boshida bir marotaba foydalana olamiz.Ifga shart kiritiladi.
    elif -- bu agarda dedan ma‘noni bilidiradi,elifni istaganimizcha ifdan so'ng ishlatamiz .Elifga ham shart kiritamiz.
    else -- bu bo‘lmasa degan ma‘noni bildiradi ,else if bilan elif ishlamaganda, kiritgan kodlarimiz oxirida bir marotaba ishlatilinadi.Elsega shart kiritmaymiz.  
    ''')

    m = input('''Sizga misollar keltiraman:''')
    a = int(input("1-sonni kiriting: "))
    b = int(input("2-sonni kiriting: "))
    if a > b:
        print('a son b sondan katta')
    elif a < b:
        print('a son b sondan kichik')
    else:
        print('Ikkala son bir-biriga teng')         
 

    m1 =input('''Sizga vazifa:
    Shart operatorlaridan foydalanib kalkulyator tuzing ''')
