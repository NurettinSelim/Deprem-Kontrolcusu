import time

import deprem

ikinci_deprem = None
while True:
    deprem.depremleri_yukle()  # Depremleri yüklüyor
    ilk_deprem = deprem.deprem0
    if ikinci_deprem is not None: # Bu kısmı programın ilk turda karşılaştırma yapmadan atlaması için yazdım
        if deprem.saat_hesapla(ilk_deprem.saat) > deprem.saat_hesapla(ikinci_deprem.saat):
            print("--------------Yeni-Deprem--------------")
            print(ilk_deprem)
            deprem.deprem_uyari(ilk_deprem.siddet)
            time.sleep(25)

    time.sleep(10)

    deprem.depremleri_yukle()
    ikinci_deprem = deprem.deprem0

    # print(ilk_deprem.konum, ikinci_deprem.konum)

    if deprem.saat_hesapla(ikinci_deprem.saat) > deprem.saat_hesapla(ilk_deprem.saat):
        print("--------------Yeni Deprem--------------")
        print(ikinci_deprem)
        deprem.deprem_uyari(ikinci_deprem.siddet)
        time.sleep(25)

    time.sleep(10)
