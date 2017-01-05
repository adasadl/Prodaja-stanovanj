import re
import orodja


def pocisti_oglas(oglas):
    podatki = oglas.groupdict()
    podatki['id'] = int(podatki['id'])
    podatki['naslov'] = podatki['naslov'].strip()
    
    velikost = ''
    for i in podatki['velikost']: 
        if i == ',':
            velikost = velikost + '.'
        else:
            velikost = velikost + i
    
    podatki['velikost'] = ("%.2f" % float(velikost))

    cena = ''
    for i in podatki['cena']:
        if i == '.':
            cena = cena
        elif i == ',':
            cena = cena + '.'
        else:
            cena = cena + i
            
    if float(cena) < 16000:
        
        cena = float(cena) * float(velikost)
            
    podatki['cena'] = ("%.2f" % float(cena))

    podatki['prodajalec'] = podatki['prodajalec'].strip()
    return podatki


# id, naslov, opis, velikost, cena, prodajalec, leto, nadstopje
def ustvari_csv_datoteke():
    regex_oglasa = re.compile(
        r'<div class="oglas_container oglasbold oglas.*?<h2><a href=.*? title="(?P<id>\d{7})">.*?'
        r'<span class="title">(?P<naslov>.*?)</span></a></h2>.+?'
        r'<span class="velikost">(?P<velikost>.*?) m2</span><br />.*?'
        r'<span class="cena">(?P<cena>.*?) &euro.*?'
        r'<div class="prodajalec_o" title="(?P<prodajalec>.*?)"><div class="logo">.*?'
        ,
        flags=re.DOTALL)

    oglasi = []
    for html_datoteka in orodja.datoteke('stanovanja_html/'):
        for oglas in re.finditer(regex_oglasa, orodja.vsebina_datoteke(html_datoteka)):
            oglasi.append(pocisti_oglas(oglas))

    orodja.zapisi_tabelo(oglasi, ['id', 'naslov',  'cena', 'velikost', 'prodajalec'], 'oglasi1.csv')



ustvari_csv_datoteke()




