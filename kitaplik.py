import sqlite3
connect = sqlite3.connect("kitaplık.db")
imlec = connect.cursor()

class Kitaplar():
    def __init__(self,):
        self.kitapAdet = 1

    def KitapEkle(self, kitapismi, yazar, tur, ucret):
        imlec.execute("CREATE TABLE IF NOT EXISTS kitaplar (İsim TEXT,Yazar TEXT,Tür TEXT,Ücret INT,Adet INT)")
        connect.commit()
        imlec.execute("INSERT INTO kitaplar VALUES (?,?,?,?,?)", (kitapismi, yazar, tur, ucret, self.kitapAdet))
        connect.commit()

    def KitapSil(self, kitapismi):
        imlec.execute("DELETE FROM kitaplar WHERE İsim = ?", (kitapismi,))
        connect.commit()

    def AdetArttir(self, kitapismi, eklenecekAdet):
        global adet
        imlec.execute("SELECT Adet FROM kitaplar WHERE İsim = ?", (kitapismi,))
        adetlist = imlec.fetchall()
        for i in adetlist:
            for j in i:
                adet = int(j)
        adet += int(eklenecekAdet)


        imlec.execute("UPDATE kitaplar SET Adet = ? WHERE İsim = ?", (adet, kitapismi))
        connect.commit()
    def FiyatGuncelle(self, kitapismi, yeniFiyat):
        imlec.execute("UPDATE kitaplar Set Ücret = ? WHERE İsim = ?", (yeniFiyat, kitapismi))
        connect.commit()

    def KitapTurListele(self, kitapTur):
        imlec.execute("SELECT * FROM kitaplar Where Tür = ?", (kitapTur,))
        liste = imlec.fetchall()
        print("\n\n")
        for i in liste:
            print(i)
        print("\n\n")
    def KitapListele(self):
        imlec.execute("SELECT * FROM kitaplar")
        liste = imlec.fetchall()
        print("\n\n")
        for i in liste:
            print(i)
        print("\n\n")


class Roman(Kitaplar):
    def __init__(self):
        super().__init__()
        self.kitapTur = "Roman"

    def KitapEkle(self, kitapismi, yazar, ucret):
        imlec.execute("CREATE TABLE IF NOT EXISTS kitaplar (İsim TEXT,Yazar TEXT,Tür TEXT,Ücret INT,Adet INT)")
        connect.commit()
        imlec.execute("INSERT INTO kitaplar VALUES (?,?,?,?,?)", (kitapismi, yazar, self.kitapTur, ucret, self.kitapAdet))
        connect.commit()
class Edebiyat(Kitaplar):
    def __init__(self):
        super().__init__()
        self.kitapTur = "Edebiyat"

    def KitapEkle(self, kitapismi, yazar, ucret):
        imlec.execute("CREATE TABLE IF NOT EXISTS kitaplar (İsim TEXT,Yazar TEXT,Tür TEXT,Ücret INT,Adet INT)")
        connect.commit()
        imlec.execute("INSERT INTO kitaplar VALUES (?,?,?,?,?)",
                      (kitapismi, yazar, self.kitapTur, ucret, self.kitapAdet))
        connect.commit()
class KisiselGelisim(Kitaplar):
    def __init__(self):
        super().__init__()
        self.kitapTur = "Kişisel Gelişim"

    def KitapEkle(self, kitapismi, yazar, ucret):
        imlec.execute("CREATE TABLE IF NOT EXISTS kitaplar (İsim TEXT,Yazar TEXT,Tür TEXT,Ücret INT,Adet INT)")
        connect.commit()
        imlec.execute("INSERT INTO kitaplar VALUES (?,?,?,?,?)",
                      (kitapismi, yazar, self.kitapTur, ucret, self.kitapAdet))
        connect.commit()
class Bilim(Kitaplar):
    def __init__(self):
        super().__init__()
        self.kitapTur = "Bilim"

    def KitapEkle(self, kitapismi, yazar, ucret):
        imlec.execute("CREATE TABLE IF NOT EXISTS kitaplar (İsim TEXT,Yazar TEXT,Tür TEXT,Ücret INT,Adet INT)")
        connect.commit()
        imlec.execute("INSERT INTO kitaplar VALUES (?,?,?,?,?)",
                      (kitapismi, yazar, self.kitapTur, ucret, self.kitapAdet))
        connect.commit()
class Felsefe(Kitaplar):
    def __init__(self):
        super().__init__()
        self.kitapTur = "Felsefe"

    def KitapEkle(self, kitapismi, yazar, ucret):
        imlec.execute("CREATE TABLE IF NOT EXISTS kitaplar (İsim TEXT,Yazar TEXT,Tür TEXT,Ücret INT,Adet INT)")
        connect.commit()
        imlec.execute("INSERT INTO kitaplar VALUES (?,?,?,?,?)",
                      (kitapismi, yazar, self.kitapTur, ucret, self.kitapAdet))
        connect.commit()
