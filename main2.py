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

QAYSI MAVZUNI TANLAY
'''))

if b == 1:
    print('''Siz Data type mavzusini tanladingiz. Data type bu ma'lumotlar turi hisoblanadi.
    Data typening 4 ta asosiy ma'lumot turi mavjud. Bular:
    String -- bu text malumot turi hisoblanadi va qo‘shtirnoq ichida yoziladi.
    Integer -- bu haqiqiy sonlar to‘plamidir bunga hamma butun sonlar kiradi
    Float -- bu kasr sonlar to'plamidir yani vergul orqali ifodalanadigan sonlar kiradi 
    Boolean -- bu mantiqiy amallar to‘plamifdir, True va False orqali ifodalanadi
    ''')

    m = input('''Sizga misollar keltiraman: ''')
    print("String:")
    a = "Hello"
    print(a)

    print("Integer:")
    b = 122
    print(b)

    print("Float:")
    c = 3.14
    print(c)

    print("Boolean:")
    d = 8
    f =10
    print(d > f)
   

    m1 = input('''Sizga vazifa:
    Ismingiz ,familiyangiz , yoshingizni kiriting''')
