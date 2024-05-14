"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Tomáš Komárek
email: tomaskomi@gmail.com
discord: tomaskomi
"""

import sys
import requests
from bs4 import BeautifulSoup
import csv


def stahni_stranku(url):
    """Stáhne stránku a vrátí BeautifulSoup objekt"""
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")


def najdi_vysledky_stran(soup):
    """Najde počet hlasů pro jednotlivé kandidující strany"""
    vysledky_stran = soup.find_all("table", {"class": "table"})[1:]
    return [td.text.strip() for tabulka in vysledky_stran for td in tabulka.find_all("td")][2:-5:5]


def najdi_souhrnne_vysledky(soup):
    """Najde souhrné hodnoty na úrovni jednotlivých obcí"""
    vysledky = soup.find_all("td", {"class": "cislo"})
    indexy = [3, 4, 7]
    return [vysledky[i].text for i in indexy]


def najdi_nazev_obce(soup):
    """Najde název obce pro příslušný cyklus"""
    return [td.text for index, td in enumerate(soup.find_all('td', {'class': 'overflow_name'})) if index == pocet_cyklu]


def najdi_kod_obce(soup):
    """Najde kód obce pro příslušný cyklus"""
    return [td.text for index, td in enumerate(soup.find_all("td", {"class": "cislo"})) if index == pocet_cyklu]


def vypis_vysledky(plny_odkaz, url):
    """Vypíše kompletní data o výsledcích v obci"""
    global pocet_cyklu
    pocet_cyklu += 1
    soup_obce = stahni_stranku(plny_odkaz)
    soup = stahni_stranku(url)
    return najdi_kod_obce(soup) + najdi_nazev_obce(soup) + najdi_souhrnne_vysledky(soup_obce) + najdi_vysledky_stran(
        soup_obce)


def zapis_prvni_radek(writer):
    """Vypíše první řádek tabulky s názvy sloupců"""
    sloupce = ["Kód obce", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy",
               "Občanská demokratická strana", "Řád národa - Vlastenecká unie", "CESTA ODPOVĚDNÉ SPOLEČNOSTI",
               "Česká str.sociálně demokrat.", "Radostné Česko", "STAROSTOVÉ A NEZÁVISLÍ",
               "Komunistická str.Čech a Moravy", "Strana zelených", "ROZUMNÍ-stop migraci,diktát.EU",
               "Strana svobodných občanů", "Blok proti islam.-Obran.domova", "Občanská demokratická aliance",
               "Česká pirátská strana", "Referendum o Evropské unii", "TOP 09", "ANO 2011", "Dobrá volba 2016",
               "SPR-Republ.str.Čsl. M.Sládka", "Křesť.demokr.unie-Čs.str.lid.", "Česká strana národně sociální",
               "REALISTÉ", "SPORTOVCI", "Dělnic.str.sociální spravedl.", "Svob.a př.dem.-T.Okamura (SPD)",
               "Strana Práv Občanů"]
    writer.writerow(sloupce)


def scrapuj_a_zapis(url, vystupni_soubor):
    """Scrapuje data a zapisuje je do CSV souboru"""
    global pocet_cyklu
    pocet_cyklu = -1

    with open(vystupni_soubor, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        zapis_prvni_radek(writer)
        soup = stahni_stranku(url)
        odkazy = soup.find_all("td", class_="center")

        for odkaz in odkazy:
            a_tag = odkaz.find("a")
            if a_tag:
                href = a_tag["href"]
                plny_odkaz = f"https://www.volby.cz/pls/ps2017nss/{href}"
                try:
                    data = vypis_vysledky(plny_odkaz, url)
                    writer.writerow(data)
                except Exception as e:
                    continue


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Zadejte správné argumenty (URL a název výstupního souboru).")
        sys.exit(1)

    url = sys.argv[1]
    vystupni_soubor = sys.argv[2]

    scrapuj_a_zapis(url, vystupni_soubor)
