import re
import orodja


def pocisti_oglas(oglas):
    podatki = oglas.groupdict()
    podatki['id'] = int(podatki['id'])
    podatki['atributi'] = podatki['atributi'].strip()
    
    
    return podatki


def ustvari_csv_datoteke():
    regex_oglasa = re.compile(
        r'<div class="oglas_container oglasbold oglas.*?<h2><a href=.*? title="(?P<id>.*?)">.*?'
        r'<span class="atribut">(?P<atributi>.*?)</strong></span>\n.*?'
        ,
        flags=re.DOTALL)



    oglasi = []
    for html_datoteka in orodja.datoteke('stanovanja_html/'):
        for oglas in re.finditer(regex_oglasa, orodja.vsebina_datoteke(html_datoteka)):
            oglasi.append(pocisti_oglas(oglas))

    # nekateri oglasi nimajo podanega leta, nekateri nimajo nadstropja, zato jih bomo razdelili v 3 skupine;
    # tisti, ki imajo podano leto, tisti, ki imajo nadstropje in tisti, ki imajo podano oboje
    # ustavrimo 3 csv datoteke in 3 tabele potem pa jih združimo
    
    nadstropje_leto = []
    nadstropje = []
    leto = []
    for i in oglasi:
        if 'Nadstropje' in i['atributi'] and 'Leto' in i['atributi']:
            nadstropje_leto.append(i)
        elif 'Nadstropje' in i['atributi']:
            nadstropje.append(i)
        else:
            leto.append(i)
            
    # oglasi, ki imajo podano leto in ne nadstropja
    leto3 = []
    for x in leto:
        leto2 = {}
        leto2['id'] = x['id']
        leto2['nadstropje'] = str('ni podatka')
        leto1 = re.findall(r'\d{4}', x['atributi'])
        leto2['leto'] = int(leto1[0])

        leto3.append(leto2)


    #oglasi, ki imajo podano nadstropje  in ne leta
    nadstropje3 = []
    for x in nadstropje:
        nadstropje2 = {}
        nadstropje2['id'] = x['id']
        nadstropje2['leto'] = str('ni podatka')
        pocisti = str(x['atributi'])[20:]
        pocisti1 = ''
        for i in pocisti:
            if i != '<':
                pocisti1 = pocisti1 + i
            elif i == '<':
                break        
    
        nadstropje2['nadstropje'] = str(pocisti1)

        nadstropje3.append(nadstropje2)

        
    # oglasi, ki imajo podano oboje
    nadstropje_leto3 = []
    for x in nadstropje_leto:
        nadstropje_leto2 = {}
        nadstropje_leto2['id'] = x['id']
        nadstropje_leto2['leto'] = int(re.findall(r'\d{4}', x['atributi'])[0])
        pocisti = str(x['atributi'])[20:]
        pocisti1 = ''
        for i in pocisti:
            if i != '<':
                pocisti1 = pocisti1 + i
            elif i == '<':
                break
                
        nadstropje_leto2['nadstropje'] = str(pocisti1)
        nadstropje_leto3.append(nadstropje_leto2)




    # zapišemo 3 csv datoteke
    orodja.zapisi_tabelo(leto3, ['id','leto', 'nadstropje'], 'oglasi_leto1.csv')
    orodja.zapisi_tabelo(nadstropje3, ['id','leto', 'nadstropje'], 'oglasi_nadstropje1.csv')
    orodja.zapisi_tabelo(nadstropje_leto3, ['id','leto', 'nadstropje'], 'oglasi_nadstropje_leto1.csv')
                        
                         
    


ustvari_csv_datoteke()





