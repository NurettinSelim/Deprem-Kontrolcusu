import son_depremler
import time
from beep_sound import do_beep

i = 0
while True:
    son_depremler.depremleri_yukle()
    ilk_deprem = son_depremler.deprem0
    if i > 0:
        if ilk_deprem.saat != ikinci_deprem.saat:
            print("--------------Yeni Deprem--------------\n", ilk_deprem)
            do_beep("warning")
            time.sleep(25)
    else:
        i += 1

    time.sleep(10)

    son_depremler.depremleri_yukle()
    ikinci_deprem = son_depremler.deprem0

    print(ilk_deprem.konum, ikinci_deprem.konum)

    if ilk_deprem.saat != ikinci_deprem.saat:
        print("--------------Yeni Deprem--------------\n", ikinci_deprem)
        do_beep("warning")

        time.sleep(25)

    time.sleep(10)
