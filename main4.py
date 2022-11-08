b = int(input('''Bizning python darsimizning mavzulari:
1:Data Type
2:Shart operatorlari
3:Takrorlash operatorlari
4:Listlar
5:Funksiya
6:Exception
7:OOP
8:Inhertance
9:Tuple
10:Dictonaries
11:Import
12:Threading

QAYSI MAVZUNI TANLAYSIZ
'''))

if b == 3:
    print('''Siz takrorlash operatorlari mavzusini tanladingiz
    Takrorlash operatorlari 
    while va for 
    while -- qachonki degan ma‘noni bildiradi ,whileda biz o‘garuvchilar kiritib ishlaymiz
    for -- uchun degan ma‘noni bildiradi , forda biz o‘zgaruvchi kiritmasdan ishlasak ham bo‘ladi
    break -- bu bizga to‘xtatish vazifasini bajaradi
    ''')

    m = input('''Sizga misollar keltiraman: ''')
    
    a = 0
    b= 900 
    while a < b:
        a += 1
        print(a)
        
    for x in range(900):
        print(x)
    

    a = 0
    b = int(input("sonni kiriting:"))
    while a < b:
        a += 1
        print(a)
        if a == b/2:
            print("siz kiritgan sonni yarmiga yetib keldik")
            break

   

    m1 = input('''Sizga vazifa:
    Toq sonlarni while va forda ifodalang
    ''')

