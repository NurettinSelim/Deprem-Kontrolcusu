from time import sleep
from winsound import Beep

import requests
from bs4 import BeautifulSoup


def liste_olustur(metin):
    liste = metin.split("\n")  # Metini satırlar halinde listeye ekliyor.
    temp_list = list()  # Fonksiyon için geçici bir liste
    for i in liste:
        temp_list.append(i.strip('\r'))  # Listenin her bir elemanın sonundaki gereksiz \r karakterini siliyor.
    temp_list.pop(501)  # Listenin sondaki boş 2 elemanını siliyor.
    temp_list.pop(500)
    return temp_list


class deprem:

    def __init__(self, deprem):
        # Satırlardaki deprem verisini ayıklayıp
        # teker teker değişkenlere kaydediyor
        # Ornek Veri:
        # 2020.01.29 08:09:57  39.0568   27.8267       11.1      -.-  2.0  -.-   MUSALAR-AKHISAR (MANISA)                          İlksel
        # Gün        # Saat    # Enlem   # Boylam      # Derinlik     # Şiddet   # Konum
        self.gun = deprem[:10]
        self.saat = deprem[11:19]
        self.enlem = deprem[21:28]
        self.boylam = deprem[31:37]
        if deprem[45] is " ":
            self.derinlik = deprem[46:49]
        else:
            self.derinlik = deprem[45:49]

        self.siddet = deprem[60:63]
        son_karakter = 122
        for i in range(71, 121):
            if deprem[i] == " " and deprem[i + 1] == " ":
                son_karakter = i
                break

        self.konum = deprem[71:son_karakter]

    def __str__(self):

        return "Şiddet: {}\nSaat: {}\nDerinlik: {}\nKonum: {}".format(self.siddet, self.saat, self.derinlik, self.konum)


def depremleri_yukle():
    r = None
    # try bloğu içindeki kod hata vermeden düzgün bir şekilde çalışıncaya kadar deniyor.
    while r is None:
        try:
            r = requests.get('http://www.koeri.boun.edu.tr/scripts/lst0.asp')
        except:
            print("Bir hata oluştu. Tekrar deneniyor")
            sleep(10)

    source = BeautifulSoup(r.content, 'html.parser')
    depremler_metin = source.find("pre").text[586:]  # pre etiketinin içindeki metinin depremleri içeren kısmını alıyor.
    deprem_list = liste_olustur(depremler_metin)

    deprem_dict = dict()
    for i in range(len(deprem_list)):
        deprem_dict["deprem" + str(i)] = deprem(deprem_list[i])
        # Deprem sınıflarını sözlük kullanarak deprem0, deprem1, deprem2 ...
        # şeklinde ekliyor.
    globals().update(deprem_dict)  # Sözlükleri değişkene çeviriyor.


def saat_hesapla(saat):  # Gelen hh:mm:ss verisini saniyeye çeviriyor
    liste = saat.split(":")
    saat = int(liste[0])
    dakika = int(liste[1])
    saniye = int(liste[2])
    toplam_sure = saat * 60 * 60 + dakika * 60 + saniye

    return toplam_sure


def deprem_uyari(siddet):  # Depremin şiddetine göre sesli uyarı veriyor.
    siddet = float(siddet)
    if siddet < 4:
        Beep(900, 160)
        Beep(900, 160)
    elif siddet < 5:
        Beep(900, 160)
        Beep(1500, 320)
    elif siddet < 6:
        Beep(1300, 250)
        Beep(1500, 500)
    elif siddet < 7:
        Beep(1800, 500)
        Beep(1800, 500)
        Beep(2500, 500)
        Beep(2500, 500)
    elif siddet < 8:
        Beep(2500, 200)
        Beep(3000, 600)
        Beep(2500, 600)
        Beep(3500, 800)
    elif siddet < 9:
        Beep(1800, 500)
        Beep(2300, 500)
        Beep(2100, 500)
        Beep(2600, 500)
        Beep(3000, 1000)
