import sys

with open("20010011520.txt", "w") as ogrenciler:
    ilk = ["100 Ali Cetin 20 erkek turk 91 standart\n",
         "101 Gulperi Gunay 22 kadin turk 83 ekonom\n",
         "102 Burak Hasanoglu 20 erkek turk 76 standart\n",
         "103 Melek Sari 22 kadin turk 60 ekonom\n",
         "104 Esma Burak 20 kadin turk 94 ekonom\n",
         "105 Busra Kaya 22 kadin turk 67 ekonom\n",
         "106 Ayse Seda 20 kadin turk 80 ekonom\n",
         "107 Asya Guler 20 kadin turk 51 ekonom\n",
         "108 Jorge Ofman 20 erkek alman 82 ekonom\n",
         "109 Luis Kosan 25 erkek fransiz 93 lux\n",
         "110 Rossi Romano 25 kadin italyan 87 ekonom\n",
         "111 Julie Rono 22 kadin italyan 75 ekonom\n",
         "112 Ola Buzova 25 kadin rus 40 ekonom\n",
         "113 Ihtina Seyelna 25 kadin arab 65 ekonom\n",
         "114 Meerim Ulanova 22 kadin kirgiz 72 ekonom\n",
         "115 Elena Fanuk 25 kadin ukrain 85 ekonom\n"]
    ogrenciler.writelines(ilk)


def ekle():
    print("Lutfen ad soyad haric metinsel bilgilerin hepsi kucuk harf olacak sekilde yeni ogrencinin bilgilerini giriniz->")
    numaralar = list()
    with open("20010011520.txt", "r") as dosya:
        data = dosya.readlines()
    for bilgi in data:
        ogr_bilgi = bilgi.split(" ")
        numaralar.append(ogr_bilgi[0])
    # ayni numarali kisi varsa baska girsin
    while True:
        no = int(input("Yeni ogrencinin numarasi:"))
        if str(no) in numaralar:
            print("Bu numara kullanilmistir. Tekrar giriniz->")
        else:
            break
    ad = input("Yeni ogrencinin adi:")
    soyad = input("Yeni ogrencinin soyadi:")
    yas = int(input("Yeni ogrencinin yasi:"))
    while True:
        cins = input("Yeni ogrencinin cinsiyeti:")
        if cins == "erkek" or cins == "kadin":
            break
        else:
            print("Yanlis giris! Tekrar giriniz (buyuk harfle yazdiysaniz hepsi kucuk harf olacak sekilde)->")
    uyruk = input("Yeni ogrencinin uyrugu:")
    ortalama = int(input("Yeni ogrencinin ortalamasi:"))
    print("ekonom oda-500TL | standart oda-1000TL | lux oda-1500TL")
    while True:
        oda = input("Oda turunu seciniz:")
        if oda == "ekonom" or oda == "standart" or oda == "lux":
            break
        else:
            print("Yanlis secim! Tekrar seciniz->")
    with open("20010011520.txt", "a") as Ogrenciler:
        Ogrenciler.write(str(no)+" "+ad+" "+soyad+" "+str(yas)+" "+cins+" "+uyruk+" "+str(ortalama)+" "+oda+"\n")  #sep=" ", end="\n"
    with open("20010011520.txt", "r") as ogrencies:
        print("*************************************\n")
        print(ogrencies.read(), end="\n")
        print("*************************************")


def sil():
    ktrl = ""
    silogr = ""
    with open("20010011520.txt", "r") as dosya:
        data = dosya.readlines()
    print(data)
    silinecek = input("Kaydini silmek istediginiz ogrencinin numarasi:")

    for bilgi in data:
        ogr_bilgi = bilgi.split(" ")
        if ogr_bilgi[0] == silinecek:
            silogr = (ogr_bilgi[0] + " " + ogr_bilgi[1] + " " + ogr_bilgi[2] + " " + ogr_bilgi[3] + " " + ogr_bilgi[4] + " " + ogr_bilgi[5] + " " + ogr_bilgi[6] + " " + ogr_bilgi[7])
            ktrl = silinecek
            pass
    if ktrl == silinecek:
        with open("20010011520.txt", "r") as byline:
            satirlar = byline.readlines()
        with open("20010011520.txt", "w") as f:
            for line in satirlar:
                if line.strip("]") != silogr:
                    f.write(line)
        with open("20010011520.txt", "r") as guncel:
            print("Guncellenmis ogrenci listesi:")
            print(guncel.read(), end="\n")
    else:
        print("Boyle bir numarali ogrenci yok!")


def ara():
    kontrol = ""
    with open("20010011520.txt", "r") as dosya:
        data = dosya.readlines()
    aranan = int(input("Bilgilerini gormek istediginiz ogrencinin numarasi:"))
    for bilgi in data:
        ogr_bilgi = bilgi.split(" ")
        nu = ogr_bilgi[0]
        if nu == str(aranan):
            kontrol = aranan
            print("No:"+ogr_bilgi[0]+" Ad:"+ogr_bilgi[1]+" Soyad:"+ogr_bilgi[2]+" Yas:"+ogr_bilgi[3]+" Cinsiyet:"+ogr_bilgi[4]+" Uyruk:"+ogr_bilgi[5]+" Ortalama:"+ogr_bilgi[6]+" Oda turu:"+ogr_bilgi[7])
    if kontrol == "":
        print("Boyle bir numarali ogrenci yok!")


def hesaplama(hesaplanacak):
    with open("20010011520.txt", "r") as dosya:
        data = dosya.readlines()
    for bilgi in data:
        ogr_bilgi = bilgi.split(" ")
        nom = ogr_bilgi[0]
        if nom == str(hesaplanacak):
            # oda bilgisinin sonundaki \n almamasi icin ogr_bilgi[7][:-1]
            if ogr_bilgi[7][:-1] == "ekonom":
                ucret = 500
            elif ogr_bilgi[7][:-1] == "standart":
                ucret = 1000
            else:
                ucret = 1500
            if int(ogr_bilgi[6]) >= 85:
                indirim = 0.25
            elif int(ogr_bilgi[6]) >= 70:
                indirim = 0.15
            elif int(ogr_bilgi[6]) >= 50:
                indirim = 0.5
            else:
                indirim = 0
            print("Aylik ucretiniz - {}, Indiriminiz - {}".format(ucret, indirim))
            fiyat = 9*(ucret - (ucret*indirim))  # 9 ay yurtta kalacagini varsayarak (*9)
            print("Hesaplanan fiyat-", fiyat)
            return fiyat


def guncelle():
    kontrol = ""
    ucret = 0.0
    with open("20010011520.txt", "r") as dosya:
        data = dosya.readlines()
    guncellenen = int(input("Hesabini guncellemek istediginiz ogrencinin numarasi:"))
    for bilgi in data:
        ogr_bilgi = bilgi.split(" ")
        num = ogr_bilgi[0]
        if num == str(guncellenen):
            kontrol = guncellenen
            ucret = hesaplama(guncellenen)
    if kontrol == "":
        print("Boyle bir numarali ogrenci yok!")
    else:
        print("Odemeniz gereken para miktari: ", ucret)
        odeme = int(input("Odemek istediginiz para miktari:"))
        kalan = ucret - odeme
        print("Kalan odenecek para:", kalan)


def degistir():
    kontrol = ""
    degisti = 0
    with open("20010011520.txt", "r") as dosya:
        data = dosya.readlines()
    open("20010011520.txt", "w").close()
    guncellenecek = int(input("Oda turunu degistirmek istediginiz ogrencinin numarasi:"))
    for bilgi in data:
        ogr_bilgi = bilgi.split(" ")
        nu = ogr_bilgi[0]
        if nu == str(guncellenecek):
            kontrol = guncellenecek
            print("ekonom oda-500TL | standart oda-1000TL | lux oda-1500TL")
            while True:
                yenioda = input("Yeni oda turunu seciniz:")
                if yenioda == "ekonom" or yenioda == "standart" or yenioda == "lux":
                    break
                else:
                    print("Yanlis secim! Tekrar seciniz->")
            if ogr_bilgi[7][:-1] == "ekonom":
                eskifiyat = 500
            elif ogr_bilgi[7][:-1] == "standart":
                eskifiyat = 1000
            else:  # ogr_bilgi[7] == "lux":
                eskifiyat = 1500
            print("Eski odanizin turu-{}, fiyat-{}".format(ogr_bilgi[7], eskifiyat))
            ogr_bilgi[7] = yenioda+"\n"
            degisti = 1
        with open("20010011520.txt", "a") as yenihal:
            yenihal.write(ogr_bilgi[0] + " " + ogr_bilgi[1] + " " + ogr_bilgi[2] + " " + ogr_bilgi[3] + " " + ogr_bilgi[4] + " " + ogr_bilgi[5] + " " + ogr_bilgi[6] + " " + ogr_bilgi[7])
    if degisti == 1:
        with open("20010011520.txt", "r") as dos:
            dt = dos.readlines()
        for blg in dt:
            ogr_bilgi = blg.split(" ")
            no = ogr_bilgi[0]
            if no == str(guncellenecek):
                print("Yeni odaniza gore:")
                hesaplama(guncellenecek)
    if kontrol == "":
        print("Boyle bir numarali ogrenci yok!")


def sec():
    secen = input("Secim yapacak ogrencinin numarasi:")
    with open("20010011520.txt", "r") as dosya:
        data = dosya.readlines()
    nations = set()
    mates = list()
    samemates = list()
    sayac = 0
    kontrol = ""
    for bilgi in data:
        ogr_bilgi = bilgi.split(" ")
        if ogr_bilgi[0] == secen:
            kontrol = secen
            if ogr_bilgi[7][:-1] == "ekonom":
                kisi_sayisi = 6
            elif ogr_bilgi[7][:-1] == "standart":
                kisi_sayisi = 4
            else:  # ogr_bilgi[7][-1] == "lux"
                kisi_sayisi = 2
            while True:
                choise = int(input("1-Yabanci uyruklu arkadaslar olsun\n2-Ayni uyrunklu arkadaslar olsun\nSizin seciminiz:"))
                if choise == 1:
                    while sayac < kisi_sayisi - 1:
                        for Bilgi in data:
                            ogr_veri = Bilgi.split(" ")
                            if ogr_bilgi[5] != ogr_veri[5] and ogr_bilgi[7] == ogr_veri[7] and ogr_bilgi[4] == ogr_veri[4]:
                                if ogr_bilgi[0] == ogr_veri[0]:  #kendisini dahil etmsin
                                    pass
                                else:
                                    uzunluk = len(nations)
                                    nations.add(ogr_veri[5])  # yabanci uyruklu ama ayni uyruklu olmamalari icin (mix nationalities room)
                                    if len(nations) > uzunluk:
                                        mates.append(ogr_veri)
                                        sayac += 1
                        break  # odayi doldurmak icin ogrenci yetmediyse break etsin
                    if len(mates) < kisi_sayisi-1:
                        print("Odaniz dolmadi!")
                    print("Sizin oda arkadaslariniz:\n", mates)
                    break
                elif choise == 2:
                    while sayac < kisi_sayisi - 1:
                        for BILGI in data:
                            ogr_veri = BILGI.split(" ")
                            if ogr_bilgi[5] == ogr_veri[5] and ogr_bilgi[7] == ogr_veri[7] and ogr_bilgi[4] == ogr_veri[4]:
                                if ogr_bilgi[0] == ogr_veri[0]:
                                    pass
                                else:
                                    samemates.append(ogr_veri)
                                    sayac += 1
                        break
                    if len(samemates) < kisi_sayisi-1:
                        print("Odaniz dolmadi!")
                    print("Sizin oda arkadaslariniz:\n", samemates)
                    break
                else:
                    print("Yanlis secim! Tekrar seciniz->")
    if kontrol == "":
        print("Boyle bir numarali ogrenci yok!")


def listele():
    liste = dict()
    with open("20010011520.txt", "r") as dosya:
        data = dosya.readlines()
    while True:
        print(" Tumunu listele-0\n Yasa gore siniflandir-1\n Cinsiyete gore siniflandir-2\n Uyruga gore siniflandir-3\n Oda turune gore siniflandir-4\n ")
        tur = int(input("Nasil bir liste istiyorsunuz:"))
        if tur == 0:
            for bilgi in data:
                ogr_bilgi = bilgi.split(" ")
                print(ogr_bilgi)
            break
        if tur == 1:
            for bilgi in data:
                ogr_bilgi = bilgi.split(" ")
                if ogr_bilgi[3] in liste.keys():
                    liste[ogr_bilgi[3]] += ogr_bilgi[1] + "-" + ogr_bilgi[2] + " | "
                else:
                    liste[ogr_bilgi[3]] = ogr_bilgi[1] + "-" + ogr_bilgi[2] + " | "
            print(liste)
            break
        if tur == 2:
            for bilgi in data:
                ogr_bilgi = bilgi.split(" ")
                if ogr_bilgi[4] in liste.keys():
                    liste[ogr_bilgi[4]] += ogr_bilgi[1] + "-" + ogr_bilgi[2] + " | "
                else:
                    liste[ogr_bilgi[4]] = ogr_bilgi[1] + "-" + ogr_bilgi[2] + " | "
            print(liste)
            break
        if tur == 3:
            for bilgi in data:
                ogr_bilgi = bilgi.split(" ")
                if ogr_bilgi[5] in liste.keys():
                    liste[ogr_bilgi[5]] += ogr_bilgi[1] + "-" + ogr_bilgi[2] + " | "
                else:
                    liste[ogr_bilgi[5]] = ogr_bilgi[1] + "-" + ogr_bilgi[2] + " | "
            print(liste)
            break
        if tur == 4:
            for bilgi in data:
                ogr_bilgi = bilgi.split(" ")
                if ogr_bilgi[7] in liste.keys():
                    liste[ogr_bilgi[7]] += ogr_bilgi[1] + "-" + ogr_bilgi[2] + " | "
                else:
                    liste[ogr_bilgi[7]] = ogr_bilgi[1] + "-" + ogr_bilgi[2] + " | "
            print(liste)
            break
        else:
            print("Yanlis secim! Tekrar seciniz->")


while True:
    print("---------------------------------")
    print("             MENU")
    print("---------------------------------")
    print(" |Yeni ogrenci kaydi-1           |\n",
          "|Ogrenci kaydi silme-2          |\n",
          "|Ogrenci arama-3                |\n",
          "|Ogrenci hesabini guncelleme-4  |\n",
          "|Kayit listeleme-5              |\n",
          "|Oda arkadas secimi-6           |\n",
          "|Oda turu degistirme-7          |\n",
          "|Cikis-0                        |")
    print("---------------------------------")
    while True:
        secim = int(input("Lutfen gerekli islem numarasini giriniz:"))
        if secim == 1:
            ekle()
        elif secim == 2:
            sil()
        elif secim == 3:
            ara()
        elif secim == 4:
            guncelle()
        elif secim == 5:
            listele()
        elif secim == 6:
            sec()
        elif secim == 7:
            degistir()
        elif secim == 0:
            sys.exit()
        else:
            print("Yanlis islem numarasi girildi! Tekrar giriniz->")
        if secim in [1, 2, 3, 4, 5, 6, 7]:
            while True:
                print("MENUye don-1 | Cik-0")
                karar = int(input("Sonraki adimi seciniz:"))
                if karar == 1:
                    break
                elif karar == 0:
                    sys.exit()
                else:
                    print("Yanlis secim! Tekrar seciniz->")
        break
