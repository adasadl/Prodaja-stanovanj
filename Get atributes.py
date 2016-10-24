import re
import orodja

# id, naslov, opis, velikost, cena, prodajalec, leto, nadstopje
def ustvari_csv_datoteke():
    regex_oglasa = re.compile(
        r'<h2><a href=.*? title=(?P<id>.*?)><span class="title">(?P<naslov>.*?)</span></a></h2>.+?'
        r'<div class="kratek">(?P<opis>.*?)</div>.*?'
        r'<span class="velikost">(?P<velikost>.*?)</span><br />.*?'
        r'<span class="cena">(?P<cena>.*?)&euro.*?'
        #r'<span class="atribut">Leto: <strong>(?P<cena>\d{4})</strong></span>.*?'
        ,
        flags=re.DOTALL)


    for html_datoteka in orodja.datoteke('stanovanja/'):
        for oglas in re.finditer(regex_oglasa, orodja.vsebina_datoteke(html_datoteka)):
            print(oglas.groupdict())



ustvari_csv_datoteke()
