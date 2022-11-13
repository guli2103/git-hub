from main0 import *

if b==8:
    print('''Siz Inhertance mavzusini tanladingiz.
    Inhertance - meros olish degan ma'noni bildiradi.
    Esingizda bo'lsa OOP ning 4 ta ustunlik tamonining 3-chisi Inhertance edi.
    ''')
    print("Sizga misollar keltiraman.")
    class Odam:
        def __init__(self,ismi,familiyasi):
            self.ismi = ismi
            self.familiyasi = familiyasi
        def __str__(self):
            return f'{self.ismi}'

    class Dasturchi(Odam):
        def __init__(self, ismi, familiyasi,toifasi):
            super().__init__(ismi, familiyasi) 
            self.toifasi = toifasi
        def chiqarish(self):
            print({self.ismi} ,{self.familiyasi}, "siz dasturlashning", {self.toifasi}, "toifasidasiz")
    d1 = Dasturchi("Gulbahor","Ergasheva","junior")
    print(d1.chiqarish()) 

    print('''Sizga vazifa 
    Inhertancedan 3 ta har xil yaratish ''')        
                    


     

