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

if b == 4:
    print('''Siz listlar mavzusini tanladingiz
    List - bu ma'lumotlar bazasi bilan ishlash va ma'lumotlafrni o'zida saqlash vazifasini bajaradi.
    Listlar [] qavslar orqali ifodalanadi.
    Ular indextlangan tartibda bo'ladi yani dasturlash tilida sanoq boshi noldan boshlanadi.
    Listlarni ichiga 5 ta ma'lumot turini kiritsak bo'ladi bular: string,integer,float,boolean va listlarni o'zini kiritsak ham bo'ladi   ''')

    print("Sizga misollar keltiraman")

    a =["salom",21, 21.03,True,[ 55,"hello",[21.033, " GULI"]]]
    print(a[2])
    print(a[4][2][1])
    print(a[0],a[4][2][1])

    print('''Sizga vazifa
    O'zgaruvchini yozib listdan [3][2][1] yozganizda ismingizni chiqarsin ''')
    