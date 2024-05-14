**Popis projektu:**

Tento projekt extrahuje vysledky voleb do Poslanecké sněmovny Parlamentu České republiky z roku 2017 a ukládá jej do souboru ve formátu CSV. Odkaz je k nahlédnutí zde: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ



**Instalace knihoven:**

V dokumentu requirements.txt se nachází knihovny, které byly použity v kódu. Jejich instalaci doporučuji v novém virtuílním prostředí a s nainstalovaným manažerem spustit tato: 

$ pip --version    #ověření verze manažeru

$ pip install -r requirements.txt    #instalace knihoven


**Spouštění projektu:**

Spušění souboru v rámci příkazového řádku vyžaduje dva argumenty. Po spuštění program uloží výsledky do souboru s příponou .csv. 

python election_scraper.py <url_uzemniho_celku> <vysledny_soubor> 


**Ukázka projektu:**

Výsledky hlasování pro okres Prostějov:

1. argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
2. argument: vysledky_prostejov.csv

Spuštění projektu: 

python elections_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "vysledky_prostejov.csv"

Ukázka výstupu:

![Obrázek 14 05 2024 v 23 26](https://github.com/tomaskomi/tomas_komarek_python_project_3/assets/158574466/45cb537e-6c3e-4652-8a90-6a47d46ab634)


