import son_depremler
import time

while True:
    time.sleep(10)
    son_depremler.son_depremler()
    ilk_deprem = son_depremler.deprem0
    son_depremler.son_depremler()
    ikinci_deprem = son_depremler.deprem0

    if ilk_deprem.saat != ikinci_deprem.saat:
        print("deprem")

    print(ilk_deprem.konum, ikinci_deprem.konum)