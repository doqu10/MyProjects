#çarpım tablosu
import random
import time
import datetime
import timeit

baslangic = time.time()

min = 1
max = 9
dogrusayisi = 0




while(True):


    sayi1 = random.randint(min, max)
    sayi2 = random.randint(min, max)
    sonuc = sayi1 * sayi2

    print("{} X {} = ".format(sayi1, sayi2),end="")
    cevap = input()
    if(cevap == "q"):
        bitis = time.time()
        gecensure = bitis - baslangic
        gecensure = round(gecensure, 2)
        puan = dogrusayisi / gecensure
        puan = round(puan, 2)
        print("Süre: {}\nDogru Sayisi: {}\nPuan: {}\nOyundan çıkılıyor...".format(gecensure, dogrusayisi, puan))
        break

    if(sonuc == int(cevap)):
        print("Bravo. Doğru cevap")
        dogrusayisi+= 1
    else:
        print("Maalesef bilemedin. Doğru cevap {}".format(sonuc))
        bitis = time.time()
        gecensure = bitis - baslangic
        gecensure = round(gecensure, 2)
        puan = dogrusayisi / gecensure
        puan = round(puan, 2)
        print("Süre: {}\nDogru Sayisi: {}\nPuan: {}\nOyundan çıkılıyor...".format(gecensure, dogrusayisi, puan))
        break



