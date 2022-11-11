from main0 import b

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
    