import requests
from bs4 import BeautifulSoup


def clear_list(liste):
    temp_list = list()
    for i in liste:
        temp_deprem = i.strip('\r')
        temp_list.append(temp_deprem)
    temp_list.pop(501)
    temp_list.pop(500)
    return temp_list


class deprem():

    def __init__(self, deprem):
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

def son_depremler():

    r = requests.get('http://www.koeri.boun.edu.tr/scripts/lst0.asp')
    source = BeautifulSoup(r.content, 'html.parser')
    depremler_metin = source.find("pre").text[586:]
    deprem_list = depremler_metin.split("\n")
    deprem_list = clear_list(deprem_list)

    deprem_dict = dict()
    for i in range(len(deprem_list)):
        deprem_dict["deprem" + str(i)] = deprem(deprem_list[i])
    globals().update(deprem_dict)
