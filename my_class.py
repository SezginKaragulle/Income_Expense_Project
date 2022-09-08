class Araba:

    def __init__(self) -> None:
        print("FONSİYON ÇAĞIRILDI")
    model = ""
    renk = ""
    beygir_gucu =0
    silindir =0
    
    def arac_bilgileri(self,modelim,renk,beygir_gucu,silindir):
        print("MODEL       : ",modelim)
        print("RENK        : ",renk)
        print("BEYGİR GÜCÜ : ",beygir_gucu)
        print("SİLİNDİ     : ",silindir)


myNewAraba = Araba()
myNewAraba.model = "RENAULT CLİO"
myNewAraba.renk = "MAVİ"
myNewAraba.beygir_gucu = 130
myNewAraba.silindir = 4

myNewAraba.arac_bilgileri(myNewAraba.model,myNewAraba.renk,myNewAraba.beygir_gucu,myNewAraba.silindir)
        