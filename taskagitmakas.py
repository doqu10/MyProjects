import random
import time

secenekler = ["taş", "kağıt", "makas"]
playerScore = 0
bilgisayarScore = 0

while(True):
    giris = input("Sıra sizde(Taş/Kağıt/Makas):  ")
    bilgisayar_random = random.randint(0,2)
    bilgisayar_secim = secenekler[bilgisayar_random]
    time.sleep(0.5)
    if(bilgisayar_secim == giris):
        print("Berabere ({} / {})".format(giris, bilgisayar_secim))
        print("{} - {}".format(playerScore, bilgisayarScore))
    elif(bilgisayar_secim == secenekler[0] and giris == secenekler[1]):
        playerScore += 1
        print("Sen kazandın. Tebrikler({} / {})".format(giris, bilgisayar_secim))
        print("{} - {}".format(playerScore, bilgisayarScore))
    elif(bilgisayar_secim ==secenekler[0] and giris == secenekler[2]):
        bilgisayarScore += 1
        print("Kaybettin. :( ({} / {})".format(giris, bilgisayar_secim))
        print("{} - {}".format(playerScore, bilgisayarScore))
    elif(bilgisayar_secim == secenekler[1] and giris == secenekler[0]):
        bilgisayarScore += 1
        print("Kaybettin. :( ({} / {})".format(giris, bilgisayar_secim))
        print("{} - {}".format(playerScore, bilgisayarScore))
    elif(bilgisayar_secim == secenekler[1] and giris == secenekler[2]):
        playerScore += 1
        print("Sen kazandın. Tebrikler({} / {})".format(giris, bilgisayar_secim))
        print("{} - {}".format(playerScore, bilgisayarScore))
    elif(bilgisayar_secim == secenekler[2] and giris == secenekler[0]):
        playerScore += 1
        print("Sen kazandın. Tebrikler({} / {})".format(giris, bilgisayar_secim))
        print("{} - {}".format(playerScore, bilgisayarScore))
    elif(bilgisayar_secim == secenekler[2] and giris == secenekler[1]):
        bilgisayarScore += 1
        print("Kaybettin. :( ({} / {})".format(giris, bilgisayar_secim))
        print("{} - {}".format(playerScore, bilgisayarScore))
    elif(giris == "q"):
        print("Oyun Bitti!\nScore: {} - {}".format(playerScore, bilgisayarScore))
        break
    else:
        print("Hatali bir giriş yaptiniz!")