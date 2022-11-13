from main0 import *

if b==7:
    print('''Siz OOP mavzusini tanladingiz.
    OOP - bu Object Oriented Programming ya'ni ob'ektlarga asoslangan dasturlar deganidir
    OOPning 4 ta ustunlik tarafi bor
    1.Abstraction
    2.Poliymorphism
    3.Inheritance
    4.Encapsulation
    OOP class va ob'ektlardan tashkil topadi.
    class bitta , ob'ekt bir nechta bo'ladi.
    classlar ham ikkiga bo'linadi 
    1.Abstrak
    2.oddiy
    Abstrak classda ob'ekt bo'lmaydi yani pass ko'rinishida bo'ladi, ko'rinishi:
    class Odam:
        def __init__(self) -> None:
            pass

    Oddiy classda esa ob'ektlar bo'ladi,ko'rinishi:
    class Odam:
        def __init__(self,ism,familiya,yoshi):
            self.ism = ism
            self.familiya = familiya
            self.yoshi = yoshi
        def __str__(self):
            return f' {self.ism} {self.familiya} tabriklaymiz siz {self.yoshi} ga kirdingiz'

    o1 = Odam("Gulbahor","Ergasheva",19)
    print(o1)
    ''')

    print("Sizga misollar keltiraman")

    class Gul:
        def __init__(self,turi,rangi,soni):
            self.turi = turi
            self.rangi = rangi
            self.soni = soni
        def __str__(self):
            return f'Siz dokonimizdan {self.turi} gulini {self.rangi} rangidan {self.soni} dona tanladingiz'
    g1 = Gul("lola","oq",7)
    print(g1)

    print('''Sizga vazifa
    3ta class va har biriga 3 tadan ob'yekt tuzing ''')        
                

            

                


                
    