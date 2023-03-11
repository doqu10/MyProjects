import  sqlite3
from kitaplik import *








kitap = Kitaplar()
roman = Roman()
edebiyat = Edebiyat()
kisiselGelisim = KisiselGelisim()
bilim = Bilim()
felsefe = Felsefe()


while True:
    print("""\n  ******************************************

    Kütüphaneye Hoşgeldiniz:

    1 - Kitaplari Göster
    2 - Kitap Ekle
    3 - Kitap Sil
    4 - Fiyat Güncelle
    5 - Adet Arttır
    Çıkmak için q'ya basınız.
  ******************************************\n""")
    giris = input("Yapmak istediginiz islemi giriniz: ")

    if giris == "1":
        secim = input("1 - Bütün Kitapları Listele\n2 - Kategori İsmiyle Listele (Roman - Edebiyat - Kişisel Gelişim - Bilim - Felsefe) ")
        if secim == "1":
            kitap.KitapListele()
        elif secim == "2":
            tur = input("Listelenmesini istediğiniz kitabın türünü giriniz (Roman - Edebiyat - Kişisel Gelişim - Bilim - Felsefe): ")
            if tur == "Roman":
                roman.KitapTurListele("Roman")
            elif tur == "Edebiyat":
                edebiyat.KitapTurListele("Edebiyat")
            elif tur == "Kişisel Gelişim":
                kisiselGelisim.KitapTurListele("Kişisel Gelişim")
            elif tur == "Bilim":
                bilim.KitapTurListele("Bilim")
            elif tur == "Felsefe":
                roman.KitapTurListele("Felsefe")
    elif giris == "2":
        tursecim = input("Eklemek istediğiniz kitabın türünü giriniz (Roman - Edebiyat - Kişisel Gelişim - Bilim - Felsefe): ")
        if tursecim == "Roman":
            kitapismi = input("Kitabınızın ismini giriniz: ")
            yazarismi = input("Yazarın ismini giriniz: ")
            ucret = input("Kitabın ücretini giriniz: ")
            roman.KitapEkle(kitapismi, yazarismi, ucret)
        elif tursecim == "Edebiyat":
            kitapismi = input("Kitabınızın ismini giriniz: ")
            yazarismi = input("Yazarın ismini giriniz: ")
            ucret = input("Kitabın ücretini giriniz: ")
            edebiyat.KitapEkle(kitapismi, yazarismi, ucret)
        elif tursecim == "Kişisel Gelişim":
            kitapismi = input("Kitabınızın ismini giriniz: ")
            yazarismi = input("Yazarın ismini giriniz: ")
            ucret = input("Kitabın ücretini giriniz: ")
            kisiselGelisim.KitapEkle(kitapismi, yazarismi, ucret)
        elif tursecim == "Bilim":
            kitapismi = input("Kitabınızın ismini giriniz: ")
            yazarismi = input("Yazarın ismini giriniz: ")
            ucret = input("Kitabın ücretini giriniz: ")
            bilim.KitapEkle(kitapismi, yazarismi, ucret)
        elif tursecim == "Felsefe":
            kitapismi = input("Kitabınızın ismini giriniz: ")
            yazarismi = input("Yazarın ismini giriniz: ")
            ucret = input("Kitabın ücretini giriniz: ")
            felsefe.KitapEkle(kitapismi, yazarismi, ucret)
    elif giris == "3":
        kitapismi = input("Silmek istediğiniz kitabin ismini giriniz: ")
        kitap.KitapSil(kitapismi)
    elif giris == "4":
        kitapismi = input("Fiyatını güncellemek istediğiniz kitabin ismini giriniz: ")
        ucret = input("Kitabınızın yeni fiyatını giriniz: ")
        kitap.FiyatGuncelle(kitapismi, ucret)
    elif giris == "5":
        kitapismi = input("Adet eklemek istediğiniz kitabin ismini giriniz: ")
        eklenecekadet= input("Eklemek istediğiniz adet sayisini giriniz: ")
        kitap.AdetArttir(kitapismi, eklenecekadet)
    elif giris == "q":
        break
    else:
        print("\n\n!!!Hatali bir giris yaptınız.\n\n")

print("Uygulama Kapatıldı.")




connect.close()