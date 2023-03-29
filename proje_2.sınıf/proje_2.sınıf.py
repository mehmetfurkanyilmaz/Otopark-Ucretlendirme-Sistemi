# 1. ÇIKTILAR İÇİN
kullanilan_toplam_arac_sayisi = 0

# her araç sınıfı için araç sayıları:
# tüm araçlar içindeki oranı da bu verilerden elde edilecek
motosiklet_sayisi= 0   # kodu: 1 katsayısı: 1
binek_sayisi = 0       # kodu: 2 katsayısı: 2
minibus_sayisi= 0      # kodu: 3 katsayısı: 3
otobus_sayisi = 0      # kodu: 4 katsayısı: 3
kamyon_sayisi = 0      # kodu: 5 katsayısı: 4
tir_sayisi = 0         # kodu: 6 katsayısı: 4

# 2. ÇIKTILAR İÇİN
#otoparkin_toplam_geliri = 0
# her araç sınını için elde edilen toolam gelir:
# gelirin tüm araçlar içindeki oranı da bu verilerden elde edilecek
toplam_otopark_geliri =0
motosikletten_elde_edilen_gelir = 0
binekden_elde_edilen_gelir = 0
minibusten_elde_edilen_gelir = 0
otobusten_elde_edilen_gelir = 0
kamyondan_elde_edilen_gelir = 0
tirdan_elde_edilen_gelir = 0

# 3. ÇIKTILAR İÇİN
# her araç sınıfı için için araç başına otoparkta kalma süresi:
motosiklet_suresi = 0
binek_suresi = 0
minibus_suresi = 0
otobus_suresi = 0
kamyon_suresi = 0
tir_suresi = 0

toplam_gun = 0
toplam_saat = 0
toplam_dakika = 0
# araç başına ortalama gelir 1 ve 2. çıktılar yardımıyla bulunacaktır.

# 4. ÇIKTILAR İÇİN
agirligi_1_tondan_az_olan_binek_araclar = 0
# ve bu araclarin tüm binek araclar içindeki oranı

# 5. ÇIKTILAR İÇİN
agirligi_10_tondan_fazla_olan_otobus_kamyon_ve_tir_sinifi_araclar = 0
# ve bu araclarin tum otobus kamyon ve tir sinifi araclar icindeki orani

# 6. ÇIKTILAR İÇİN
otoparkta_30_dakika_veya_daha_kisa_sure_kalan_motosiklet_ve_binek_tipi_araclar = 0
# ve tüm motosiklet ve binek tipindeki araçlar içindeki oranı

# 7. ÇIKTILAR İÇİN
otoparkta_1_gunden_daha_uzun_sure_kalan_minibus_ve_otobus_tipi_araclar = 0
# ve tüm minibus ve otobus tipi araclar içindeki oranı

# 8. ÇIKTILAR İÇİN
otoparkta_30_gunden_daha_uzun_sure_kalan_ya_da_1000_tlden_daha_yuksek_gelir_elde_edilen_araclar=0
# yukarıdaki veriyi direkt kullanmayacazğız. bu verinin tüm veriler içindeki oranını bulacağız

# 9. ÇIKTILAR İÇİN
surucusu_gazi_veya_engelli_olan_araclarin_sayisi=0
surucusu_gazi_olan_araclarin_sayisi = 0
surucusu_engelli_olan_araclarin_sayisi = 0
# tüm araçlar içindeki oranları
surucusu_gazi_veya_engelli_olan_araclarin_otoparkta_kalma_suresi=0
surucusu_gazi_olan_araclarin_otoparkta_kalma_suresi = 0
surucusu_engelli_olan_araclarin_otoparkta_kalma_suresi = 0
# yukarıdaki veriyi direkt kullanmayacağız. araç başına ortalama otoparkta kalma sğresüni bulamak için kullanacağız.

# 10. ÇIKTILAR İÇİN
otoparkta_3_saatten_daha_uzun_sure_kalan_ve_indirim_uygulanan_araclar = 0
tum_indirim_uygulanan_araclar = 0
# bir üstteki veriyi direkt kullanmayacağız. oranı bulmak için kullanacağız.

# 11. ÇIKTILAR İÇİN
en_uzun_sure_otoparkta_kalan_arac = str
en_uzun_sure_otoparkta_kalan_aracin_otoparkta_kaldigi_sure = 0
en_uzun_sure_otoparkta_kalan_aracdan_elde_edilen_gelir = 0

# 12. ÇIKTILAR İÇİN
en_cok_gelir_elde_edilen_binek_arac = 0
en_cok_gelir_elde_edilen_binek_aracin_otoparkta_kaldigi_sure = 0
en_cok_gelir_elde_edilen_binek_aracdan_elde_edien_gelir = 0
#toplam değil de o anlık gelirleri kullanmada kullanıyoruz.

binek_geliri= 0
anlik_binek_suresi = 0


baska_surucu="e"

while baska_surucu == "E" or baska_surucu=="e":  # baska sürücüye evet yanıtı verildiği takdirde döngü dönmeye devam edecektir.
    print(" ")
    plaka = str(input("Araç plakası: "))

    arac_sinifi = int(input("Araç sınıfı kodu: tamsayı (1-6 arasında): "))
    while (arac_sinifi<1 or arac_sinifi>6):
        arac_sinifi = int(input("Lütfen belirtilen sayı aralığında kod giriniz: tamsayı (1-6 arasında): "))  # belirtilen aralıkta girilmezse tekrar girilmesi istenecektir.

    if (arac_sinifi==1):
        motosiklet_sayisi += 1

    elif (arac_sinifi==2):
        binek_sayisi += 1

    elif (arac_sinifi==3):
        minibus_sayisi += 1

    elif (arac_sinifi==4):
        otobus_sayisi += 1

    elif (arac_sinifi==5):
        kamyon_sayisi += 1

    elif (arac_sinifi==6):
        tir_sayisi += 1

    arac_agirligi = float(input("Araç ağırlığı (kg): reel sayı (0’dan büyük): "))
    while not (arac_agirligi > 0):
        arac_agirligi = float(input("Araç ağırlığı (kg): reel sayı (0’dan büyük): "))  # belirtilen aralıkta girilmezse tekrar girilmesi istenecektir.

    KG_BASINA_GIRIS_UCRETI = 0.0025    # burada sabit kullandık.
    giris_ucreti = arac_agirligi * KG_BASINA_GIRIS_UCRETI    # (1 ton için 2,5 TL)


    sure = int(input("Otoparkta kaldığı süre (dakika): tamsayı (0’dan büyük): "))
    while not (sure > 0):
        sure = int(input("Otoparkta kaldığı süre (dakika): tamsayı (0’dan büyük): "))  # belirtilen aralıkta girilmezse tekrar girilmesi istenecektir.

    ad_soyad = str(input("Sürücünün adı-soyadı: "))

    uygulanan_indirim_orani = 0
    if (arac_sinifi==1 or arac_sinifi==2):   # engelli ya da gazi inidrimi sadece 1 ve 2 nolu kodlarda geçerli olduğı için böyle bir yapı kullandık
        ozel_durum = str(input("Motosiklet veya binek sınıfı bir araç ise) Sürücünün özel durumu: Yok/Gazi/Engelli: (Y/y/G/g/E/e karakterleri): "))
        while not ((ozel_durum == "Y") or (ozel_durum == "y") or (ozel_durum == "G") or (ozel_durum == "g") or (ozel_durum == "E") or (ozel_durum == "e")):
            ozel_durum = str(input("Lütfen geçerli bir özel durum giriniz: Yok/Gazi/Engelli: (Y/y/G/g/E/e karakterleri): "))
        if (ozel_durum == "G" or ozel_durum == "g"):
            uygulanan_indirim_orani += 100

        elif (ozel_durum == "E" or ozel_durum == "e"):
            uygulanan_indirim_orani += 50

        else:
            uygulanan_indirim_orani = 0
    else:
        ozel_durum = "bilinmiyor"

    saat_bazinda_sure = sure // 60  # bu sayede saatlik kısmı öğreneceğiz.

    #ücret hesabı yapmak için
    saatlik_ucret = 0  # 24 saatten az olan durumlar için direkt bu ücreti alıyoruz.
    gunluk_ucret = 0
    gunluk_ucret1 = 0  # küsürattan önceki günlük ücret
    gunluk_ucret2 = 0  # bir veya birden fazla günün üstüne gelen küsüratla beraber olan ücret
    gunden_kalan_saatlar = 0

    # zaman hesabı yapmak için
    gun_sayisi = 0
    saat_sayisi = 0
    dakika_sayisi = 0

    son_otopark_ucreti = 0


    if saat_bazinda_sure < 1:    # bu ve altındaki statemant larda dakikayı gün saat ve dakika biçime dönüştürdük.

        saatlik_ucret = 3
        saat_sayisi = sure // 60
        dakika_sayisi = sure % 60

    elif saat_bazinda_sure < 3:
        saatlik_ucret = 5

        saat_sayisi = sure // 60
        dakika_sayisi = sure % 60

    elif saat_bazinda_sure < 5:
        saatlik_ucret = 7

        saat_sayisi = sure // 60
        dakika_sayisi = sure % 60

    elif saat_bazinda_sure < 10:
        saatlik_ucret = 10

        saat_sayisi = sure // 60
        dakika_sayisi = sure % 60

    elif saat_bazinda_sure < 24:
        saatlik_ucret = 14

        saat_sayisi = sure // 60
        dakika_sayisi = sure % 60

    elif saat_bazinda_sure == 24:
        saatlik_ucret = 15

        gun_sayisi = 1

    elif saat_bazinda_sure > 24:

        gunluk_ucret = saat_bazinda_sure // 24 # günlük ücreti bulmak için aşama olarak kullandın ayrıca kaç gün kalındığını da buradan görebildik.

        gunluk_ucret1 = gunluk_ucret * 15

        gunden_kalan_saatlar = saat_bazinda_sure % 24

        gunden_kalan_dakikalar = sure % 60

        gun_sayisi = sure // 1440
        saat_sayisi = (sure % 1440) //60
        dakika_sayisi = (sure % 60)

        ilave_saatlik_ucret=0
        if gunden_kalan_saatlar==0 and gunden_kalan_dakikalar==0:
            ilave_saatlik_ucret =0

        elif gunden_kalan_saatlar < 1:
            ilave_saatlik_ucret = 3

            dakika_sayisi = sure

        elif gunden_kalan_saatlar < 3:
            ilave_saatlik_ucret = 5
            saat_sayisi = (sure % 1440) //60
            dakika_sayisi = sure % 60

        elif gunden_kalan_saatlar < 5:
            ilave_saatlik_ucret = 7
            saat_sayisi = (sure % 1440) //60
            dakika_sayisi = sure % 60

        elif gunden_kalan_saatlar < 10:
            ilave_saatlik_ucret = 10
            saat_sayisi = (sure % 1440) //60
            dakika_sayisi = sure % 60

        elif gunden_kalan_saatlar < 24:
            ilave_saatlik_ucret = 14


        saat_sayisi = (sure % 1440) //60
        dakika_sayisi = sure % 60
        gunluk_ucret2 = gunluk_ucret1 + ilave_saatlik_ucret

    if (arac_sinifi == 1):        # bu koşul ifadelerin araçlara ayrı ayrı süre eklemesi yapıyoruz.
        motosiklet_suresi+= sure

    elif (arac_sinifi == 2):
        binek_suresi+= sure
        anlik_binek_suresi = sure

    elif (arac_sinifi == 3):
        minibus_suresi+= sure

    elif (arac_sinifi == 4):
        otobus_suresi+= sure

    elif (arac_sinifi == 5):
        kamyon_suresi+= sure

    elif (arac_sinifi == 6):
        tir_suresi+= sure


    aracin_ucreti = saatlik_ucret + gunluk_ucret2

    if (arac_sinifi==1):    # motosiklet için kat sayılar
        #son_otopark_ucreti = aracin_ucreti + giris_ucreti

        if (ozel_durum == "G" or ozel_durum == "g"):   # araç koduna ve özel duruma göre ücretlendirmeleri belirliyoruz.
            son_otopark_ucreti = 0
            motosikletten_elde_edilen_gelir += son_otopark_ucreti

        elif (ozel_durum == "E" or ozel_durum == "e"):
            son_otopark_ucreti = aracin_ucreti + giris_ucreti
            son_otopark_ucreti = son_otopark_ucreti / 2
            motosikletten_elde_edilen_gelir += son_otopark_ucreti

        elif (ozel_durum == "Y" or ozel_durum == "y"):
            son_otopark_ucreti = aracin_ucreti + giris_ucreti
            motosikletten_elde_edilen_gelir += son_otopark_ucreti


    elif (arac_sinifi==2):     # binek için kat sayılar
        #son_otopark_ucreti = aracin_ucreti * 2 + giris_ucreti

        if (ozel_durum == "G" or ozel_durum == "g"):
            son_otopark_ucreti = 0
            binekden_elde_edilen_gelir += son_otopark_ucreti
            binek_geliri = son_otopark_ucreti

        elif (ozel_durum == "E" or ozel_durum == "e"):
            son_otopark_ucreti = aracin_ucreti * 2 + giris_ucreti
            son_otopark_ucreti = son_otopark_ucreti / 2
            binekden_elde_edilen_gelir += son_otopark_ucreti
            binek_geliri = son_otopark_ucreti

        elif (ozel_durum == "Y" or ozel_durum == "y"):
            son_otopark_ucreti = aracin_ucreti * 2 + giris_ucreti
            binekden_elde_edilen_gelir += son_otopark_ucreti
            binek_geliri = son_otopark_ucreti

    elif (arac_sinifi==3): # or arac_sinifi==4):    # minibüs için katsayılar
        son_otopark_ucreti = (aracin_ucreti * 3) + giris_ucreti
        minibusten_elde_edilen_gelir += son_otopark_ucreti

    elif (arac_sinifi==4):    # otobüs için katsayılar
        son_otopark_ucreti = (aracin_ucreti * 3) +giris_ucreti
        otobusten_elde_edilen_gelir += son_otopark_ucreti

    elif (arac_sinifi==5 ):    # kamyon için katsayılar
        son_otopark_ucreti = (aracin_ucreti * 4) +giris_ucreti
        kamyondan_elde_edilen_gelir += son_otopark_ucreti

    elif (arac_sinifi==6):    #  tır için katsayılar
        son_otopark_ucreti = (aracin_ucreti * 4) +giris_ucreti

        tirdan_elde_edilen_gelir += son_otopark_ucreti



    if (ozel_durum=="G" or ozel_durum=="g" or ozel_durum=="E" or ozel_durum=="e"):  # ozel durumdaki sürücüler için ayrıntılı istatistikleri bulmak için koşulları
        surucusu_gazi_veya_engelli_olan_araclarin_otoparkta_kalma_suresi+= sure

    if (ozel_durum=="G" or ozel_durum=="g"):
        surucusu_gazi_olan_araclarin_otoparkta_kalma_suresi += sure

    if (ozel_durum=="E" or ozel_durum=="e"):
        surucusu_engelli_olan_araclarin_otoparkta_kalma_suresi += sure

    if (sure>180 and (ozel_durum=="G" or ozel_durum=="g" or ozel_durum=="E" or ozel_durum=="e")):
        otoparkta_3_saatten_daha_uzun_sure_kalan_ve_indirim_uygulanan_araclar+=1


    if (arac_agirligi<1000 and arac_sinifi==2):     #ağırlığı 1 tondan az olan binek araçların, tüm binek araçlar içindeki oranını bulmak için
        agirligi_1_tondan_az_olan_binek_araclar+=1

    if (arac_agirligi>10000) and (arac_sinifi==4 or arac_sinifi==5 or arac_sinifi==6):   # ağırlığı 10 tondan fazla olan otobüs, kamyon ve tır sınıfı araçların, tüm otobüs, kamyon ve tır sınıfı araçlar içindeki oranını bulmak için
        agirligi_10_tondan_fazla_olan_otobus_kamyon_ve_tir_sinifi_araclar+=1

    if (sure<=30 and (arac_sinifi==1 or arac_sinifi==2)):                                # otoparkta 30 dakika veya daha kısa süre kalan motosiklet ve binek tipi araçların, tüm motosiklet ve binek tipi araçlar içindeki oranını bulmak için
        otoparkta_30_dakika_veya_daha_kisa_sure_kalan_motosiklet_ve_binek_tipi_araclar+=1

    if (sure>1440 and(arac_sinifi==3 or arac_sinifi==4)):                                # otoparkta 1 günden daha uzun süre kalan minibüs ve otobüs tipi araçların, tüm minibüs ve otobüs tipi araçlar içindeki oranını bulmak için
        otoparkta_1_gunden_daha_uzun_sure_kalan_minibus_ve_otobus_tipi_araclar+=1

    if (sure > 43200 or son_otopark_ucreti > 1000):                                      # otoparkta 30 günden daha uzun süre kalan veya 1000 TL’den daha yüksek gelir edilen araçların, tüm araçlar içindeki oranını bulmak için
        otoparkta_30_gunden_daha_uzun_sure_kalan_ya_da_1000_tlden_daha_yuksek_gelir_elde_edilen_araclar+=1

    if (ozel_durum=="G" or ozel_durum=="g" or ozel_durum=="E" or ozel_durum=="e"):
        surucusu_gazi_veya_engelli_olan_araclarin_sayisi+=1

    if (ozel_durum=="G" or ozel_durum=="g"):
        surucusu_gazi_olan_araclarin_sayisi+=1

    if (ozel_durum=="E" or ozel_durum=="e"):
        surucusu_engelli_olan_araclarin_sayisi+=1

    if (sure>en_uzun_sure_otoparkta_kalan_aracin_otoparkta_kaldigi_sure):
        en_uzun_sure_otoparkta_kalan_aracin_otoparkta_kaldigi_sure = sure
        en_uzun_sure_otoparkta_kalan_aracdan_elde_edilen_gelir = son_otopark_ucreti


    if (anlik_binek_suresi > en_cok_gelir_elde_edilen_binek_aracdan_elde_edien_gelir):
        en_cok_gelir_elde_edilen_binek_aracdan_elde_edien_gelir = binek_geliri
        en_cok_gelir_elde_edilen_binek_aracin_otoparkta_kaldigi_sure = anlik_binek_suresi


    kullanilan_toplam_arac_sayisi += 1 # her döngü 1 araca tekabül ediyor.


    baska_surucu = str(input("Başka araç var mı? (E/e/H/h karakterleri): "))
    while not ((baska_surucu == "E") or (baska_surucu == "e") or (baska_surucu == "H") or (baska_surucu == "h")):
        baska_surucu = str(input("Başka araç var mı? (E/e/H/h karakterleri): "))

    print(" ")
    print("Araç plakası: ",plaka)
    print(" ")
    print("Araç sınıfı adı: ",arac_sinifi)
    print(" ")
    print("Araç ağırlığı (kg): ",arac_agirligi)
    print(" ")
    print("Otoparkta kaldığı süre (gün, saat, dakika): ",gun_sayisi ,"gün,", saat_sayisi,"saat,", dakika_sayisi, "dakika" )
    print(" ")
    print("Sürücünün adı-soyadı: ",ad_soyad)
    print(" ")
    print("(varsa) Sürücünün özel durumu: Gazi/Engelli: ",ozel_durum)
    print(" ")
    print("(Sürücünün özel durumu varsa) Uygulanan indirim oranı (%): %", uygulanan_indirim_orani)
    print(" ")
    print("Otopark ücreti (TL): " , "{:,.2f}".format(son_otopark_ucreti))
    print("******************************************************************************************************************")

motosiklet_orani= motosiklet_sayisi / kullanilan_toplam_arac_sayisi * 100  # araçların oranlarıyla ilgili işlemler
binek_orani = binek_sayisi / kullanilan_toplam_arac_sayisi * 100
minibus_orani = minibus_sayisi / kullanilan_toplam_arac_sayisi * 100
otobus_orani = otobus_sayisi / kullanilan_toplam_arac_sayisi * 100
kamyon_orani = kamyon_sayisi  / kullanilan_toplam_arac_sayisi * 100
tir_orani = tir_sayisi / kullanilan_toplam_arac_sayisi * 100

toplam_otopark_geliri = motosikletten_elde_edilen_gelir + binekden_elde_edilen_gelir + minibusten_elde_edilen_gelir + otobusten_elde_edilen_gelir + kamyondan_elde_edilen_gelir + tirdan_elde_edilen_gelir
motosiklet_gelir_orani = motosikletten_elde_edilen_gelir / toplam_otopark_geliri * 100  # gelirlerin oranıyla ilgili işlemler
binek_gelir_orani = binekden_elde_edilen_gelir / toplam_otopark_geliri * 100
minibus_gelir_orani = minibusten_elde_edilen_gelir / toplam_otopark_geliri * 100
otobus_gelir_orani = otobusten_elde_edilen_gelir / toplam_otopark_geliri * 100
kamyon_gelir_orani = kamyondan_elde_edilen_gelir / toplam_otopark_geliri * 100
tir_gelir_orani = tirdan_elde_edilen_gelir / toplam_otopark_geliri * 100

ortalama_motosiklet_suresi = motosiklet_suresi / motosiklet_sayisi  # ortalama sürelerle ilgili işlemler
motosiklet_gun = ortalama_motosiklet_suresi // 1440
motosiklet_saat = (ortalama_motosiklet_suresi % 1440) // 60
motosiklet_dakika = (ortalama_motosiklet_suresi % 1440) % 60

ortalama_binek_suresi = binek_suresi / binek_sayisi
binek_gun = ortalama_binek_suresi // 1440
binek_saat = (ortalama_binek_suresi % 1440) // 60
binek_dakika = (ortalama_binek_suresi % 1440) % 60

ortalama_minibus_suresi = minibus_suresi / minibus_sayisi
minibus_gun = ortalama_minibus_suresi // 1440
minibus_saat = (ortalama_minibus_suresi % 1440) // 60
minibus_dakika = (ortalama_minibus_suresi % 1440) % 60

ortalama_otobus_suresi = otobus_suresi / otobus_sayisi
otobus_gun = ortalama_otobus_suresi // 1440
otobus_saat = (ortalama_otobus_suresi % 1440) // 60
otobus_dakika = (ortalama_otobus_suresi % 1440) % 60

ortalama_kamyon_suresi = kamyon_suresi / kamyon_sayisi
kamyon_gun = ortalama_kamyon_suresi // 1440
kamyon_saat = (ortalama_kamyon_suresi % 1440) // 60
kamyon_dakika = (ortalama_kamyon_suresi % 1440) % 60

ortalama_tir_suresi = tir_suresi / tir_sayisi
tir_gun = ortalama_tir_suresi // 1440
tir_saat = (ortalama_tir_suresi % 1440) // 60
tir_dakika = (ortalama_tir_suresi % 1440) % 60

ort_motosiklet_geliri = motosikletten_elde_edilen_gelir / motosiklet_sayisi  # ortalama gelirler ile ilgili işlemler
ort_binek_geliri = binekden_elde_edilen_gelir / binek_sayisi
ort_minibus_geliri = minibusten_elde_edilen_gelir / minibus_sayisi
ort_otobus_geliri = otobusten_elde_edilen_gelir / otobus_sayisi
ort_kamyon_geliri = kamyondan_elde_edilen_gelir / kamyon_sayisi
ort_tir_geliri = tirdan_elde_edilen_gelir / tir_sayisi


hafif_binek_orani = agirligi_1_tondan_az_olan_binek_araclar / binek_sayisi * 100 # ağırlığı bir tondan az olan araçların toplam araçlar içindeki oranını veriyor.

agir_vasita_orani= agirligi_10_tondan_fazla_olan_otobus_kamyon_ve_tir_sinifi_araclar / (otobus_sayisi + kamyon_sayisi + tir_sayisi) * 100   # ağırlığı 10 tondan fazla olan otobüs, kamyon ve tır sınıfı araçların, tüm otobüs, kamyon ve tır sınıfı araçlar içindeki oranını verir

gecici_vasita = otoparkta_30_dakika_veya_daha_kisa_sure_kalan_motosiklet_ve_binek_tipi_araclar / (motosiklet_sayisi+ binek_sayisi) * 100  # Otoparkta 30 dakika veya daha kısa süre kalan motosiklet ve binek tipi araçların, tüm motosiklet ve binek tipi araçlar içindeki oranını verir.

mudavim_tasima_orani = otoparkta_1_gunden_daha_uzun_sure_kalan_minibus_ve_otobus_tipi_araclar / (minibus_sayisi + otobus_sayisi) * 100  # Otoparkta 1 günden daha uzun süre kalan minibüs ve otobüs tipi araçların, tüm minibüs ve otobüs tipi araçlar içindeki oranını verir

comert_surucu_orani= otoparkta_30_gunden_daha_uzun_sure_kalan_ya_da_1000_tlden_daha_yuksek_gelir_elde_edilen_araclar / kullanilan_toplam_arac_sayisi * 100 #Otoparkta 30 günden daha uzun süre kalan veya 1000 TL’den daha yüksek gelir edilen araçların, tüm araçlar içindeki oranını verir

gazi_engelli_oran= surucusu_gazi_veya_engelli_olan_araclarin_sayisi / kullanilan_toplam_arac_sayisi * 100 #Sürücüsü gazi veya engelli olan araçların  tüm araçlar içindeki oranlarını verir.
gazi_oran = surucusu_gazi_olan_araclarin_sayisi / kullanilan_toplam_arac_sayisi * 100
engelli_oran = surucusu_engelli_olan_araclarin_sayisi / kullanilan_toplam_arac_sayisi *100

ozel_durum_sure = surucusu_gazi_veya_engelli_olan_araclarin_otoparkta_kalma_suresi / surucusu_gazi_veya_engelli_olan_araclarin_sayisi
ozel_gun = ozel_durum_sure // 1440              # buradaki şablon özel durumdaki yani gazi ve engelli, otoparkta ortalama geçirdikleri süreyi gösteriyor.
ozel_saat = (ozel_durum_sure % 1440) // 60
ozel_dakika =( ozel_durum_sure % 1440) % 60

gazi_sure = surucusu_gazi_olan_araclarin_otoparkta_kalma_suresi / surucusu_gazi_olan_araclarin_sayisi
gazi_gun = gazi_sure // 1440
gazi_saat = (gazi_sure % 1440) // 60
gazi_dakika = (gazi_sure % 1440) % 60

engelli_sure =surucusu_engelli_olan_araclarin_otoparkta_kalma_suresi / surucusu_engelli_olan_araclarin_sayisi
engelli_gun = engelli_sure // 1440
engelli_saat = (engelli_sure % 1440) // 60
engelli_dakika = (engelli_sure % 1440) % 60

cok_indirim = otoparkta_3_saatten_daha_uzun_sure_kalan_ve_indirim_uygulanan_araclar / surucusu_gazi_veya_engelli_olan_araclarin_sayisi * 100 #Otoparkta 3 saatten daha uzun süre kalan indirim uygulanan araçların, tüm indirim uygulanan araçlar içindeki oranını verir

#uzun_kalan_arac_suresi = en_uzun_sure_otoparkta_kalan_aracin_otoparkta_kaldigi_sure // 1440
uzun_gun = en_uzun_sure_otoparkta_kalan_aracin_otoparkta_kaldigi_sure // 1440
uzun_saat = (en_uzun_sure_otoparkta_kalan_aracin_otoparkta_kaldigi_sure % 1440) // 60
uzun_dakika = (en_uzun_sure_otoparkta_kalan_aracin_otoparkta_kaldigi_sure % 1440) % 60

en_cok_gelirli_binek_arac_gunu = en_cok_gelir_elde_edilen_binek_aracin_otoparkta_kaldigi_sure //1440
en_cok_gelirli_binek_arac_saati = (en_cok_gelir_elde_edilen_binek_aracin_otoparkta_kaldigi_sure % 1440) // 60
en_cok_gelirli_binek_arac_dakikasi = (en_cok_gelir_elde_edilen_binek_aracin_otoparkta_kaldigi_sure % 1440) % 60

print(" ")
print("1- Otoparkı kullanan toplam araç sayısı: ", kullanilan_toplam_arac_sayisi, " her araç sınıfı için araç sayıları ve tüm araçlar içindeki oranları (%): ","Motosiklet oranı: %","{:,.2f}".format(motosiklet_orani)," Binek oranı: %","{:,.2f}".format(binek_orani)," Minibüs oranı: %","{:,.2f}".format(minibus_orani)," Otobüs oranı: %","{:,.2f}".format(otobus_orani)," Kamyon oranı: %","{:,.2f}".format(kamyon_orani)," Tır oranı: %","{:,.2f}".format(tir_orani))
print(" ")
print("2- Otoparkın toplam geliri (TL): ","{:,.2f}".format(toplam_otopark_geliri)," TL","Her araç sınıfı için toplam gelirler (TL) ve otoparkın toplam geliri içindeki oranları (%): Motosiklet geliri: ","{:,.2f}".format(motosikletten_elde_edilen_gelir)," TL, Oranı: %","{:,.2f}".format(motosiklet_gelir_orani),"Binek geliri: ","{:,.2f}".format(binekden_elde_edilen_gelir)," TL, Oranı: %","{:,.2f}".format(binek_gelir_orani),"Minibüs geliri: ","{:,.2f}".format(minibusten_elde_edilen_gelir)," TL, Oranı: %","{:,.2f}".format(minibus_gelir_orani),"Otobüs geliri: ","{:,.2f}".format(otobusten_elde_edilen_gelir)," TL, Oranı: %","{:,.2f}".format(otobus_gelir_orani),"Kamyon geliri: ","{:,.2f}".format(kamyondan_elde_edilen_gelir)," TL, Oranı: %","{:,.2f}".format(kamyon_gelir_orani),"Tır geliri: ","{:,.2f}".format(tirdan_elde_edilen_gelir)," TL, Oranı: %","{:,.2f}".format(tir_gelir_orani))
print(" ")
print("3- Her araç sınıfı için araç başına ortalama otoparkta kalma süresi (gün, saat, dakika): Motosiklet: ", motosiklet_gun ," gün" ,motosiklet_saat," saat",motosiklet_dakika," dakika" ,"Binek: ", binek_gun ," gün" ,binek_saat," saat",binek_dakika," dakika" " Minibüs: ", minibus_gun ," gün" ,minibus_saat," saat",minibus_dakika," dakika"" Otobüs: ", otobus_gun ," gün" ,otobus_saat," saat",otobus_dakika," dakika"," Kamyon: ", kamyon_gun ," gün" ,kamyon_saat," saat",kamyon_dakika," dakika"" Tır: ", tir_gun ," gün" ,tir_saat," saat",tir_dakika," dakika" ,"ve araç başına ortalama gelir (TL): ","Ortalama motosiklet geliri: ","{:,.2f}".format(ort_motosiklet_geliri)," TL"," Ortalama binek geliri: ","{:,.2f}".format(ort_binek_geliri)," TL"," Ortalama minibüs geliri: ","{:,.2f}".format(ort_minibus_geliri)," TL"" Ortalama otobüs geliri: ","{:,.2f}".format(ort_otobus_geliri)," TL"" Ortalama kamyon geliri: ","{:,.2f}".format(ort_kamyon_geliri)," TL"" Ortalama tır geliri: ","{:,.2f}".format(ort_tir_geliri)," TL")
print(" ")
print("4- Ağırlığı 1 tondan az olan binek araçların, tüm binek araçlar içindeki oranı (%): % ","{:,.2f}".format(hafif_binek_orani))
print(" ")
print("5- Ağırlığı 10 tondan fazla olan otobüs, kamyon ve tır sınıfı araçların, tüm otobüs, kamyon ve tır sınıfı araçlar içindeki oranı (%): % ","{:,.2f}".format(agir_vasita_orani))
print(" ")
print("6- Otoparkta 30 dakika veya daha kısa süre kalan motosiklet ve binek tipi araçların, tüm motosiklet ve binek tipi araçlar içindeki oranı (%): % ","{:,.2f}".format(gecici_vasita))
print(" ")
print("7- Otoparkta 1 günden daha uzun süre kalan minibüs ve otobüs tipi araçların, tüm minibüs ve otobüs tipi araçlar içindeki oranı (%): % ","{:,.2f}".format(mudavim_tasima_orani))
print(" ")
print("8- Otoparkta 30 günden daha uzun süre kalan veya 1000 TL’den daha yüksek gelir edilen araçların, tüm araçlar içindeki oranı (%): % ","{:,.2f}".format(comert_surucu_orani))
print(" ")
print("9- Sürücüsü gazi veya engelli olan araçların sayıları: ",surucusu_gazi_veya_engelli_olan_araclarin_sayisi ," tüm araçlar içindeki oranları (%): % ","{:,.2f}".format(gazi_engelli_oran) ," ve araç başına ortalama otoparkta kalma süreleri (gün, saat, dakika): ",ozel_gun," gün ", ozel_saat," saat ",ozel_dakika, " dakika")
print(" ")
print("9.1- Sürücüsü gazi olan araçların sayısı : ",surucusu_gazi_olan_araclarin_sayisi ," Tüm araçlar içindeki oranı: % ", "{:,.2f}".format(gazi_oran) ," Gazilerin araç başına otoparkta kalma süresi: ",gazi_gun, " gün ", gazi_saat," saat ",gazi_dakika, " dakika")
print(" ")
print("9.2- Sürücüsü engelli olan araçların sayısı : ",surucusu_engelli_olan_araclarin_sayisi ," Tüm araçlar içindeki oranı: % ","{:,.2f}".format(engelli_oran) ," Engellilerin araç başına otoparkta kalma süresi: ",engelli_gun, " gün " ,engelli_saat," saat, ",engelli_dakika, " dakika")
print(" ")
print("10- Otoparkta 3 saatten daha uzun süre kalan indirim uygulanan araçların, tüm indirim uygulanan araçlar içindeki oranı (%): % ","{:,.2f}".format(cok_indirim))
print(" ")
print("11- En uzun süre otoparkta kalan aracın otoparkta kaldığı süre (gün, saat, dakika): ",uzun_gun, " gün ",uzun_saat," saat ",uzun_dakika , " dakika "  " ve elde edilen gelir (TL): " ,"{:,.2f}".format(en_uzun_sure_otoparkta_kalan_aracdan_elde_edilen_gelir), " TL")
print(" ")
print("12- En çok gelir elde edilen binek aracın otoparkta kaldığı süre (gün, saat, dakika): ",en_cok_gelirli_binek_arac_gunu, " gün ",en_cok_gelirli_binek_arac_saati," saat ",en_cok_gelirli_binek_arac_dakikasi , " dakika " "ve elde edilen gelir (TL): ","{:,.2f}".format(en_cok_gelir_elde_edilen_binek_aracdan_elde_edien_gelir), " TL")