import re
import orodja


def create_cookies():
    
    regex_oglasa = re.compile(
        r'Name raw: \s*(?P<Name_raw>.*?)\nPath.+?'
        r'Content raw: \s*(?P<Content_raw>.*?)\nExpires.*?'
        ,
        flags=re.DOTALL)

    

    for html_datoteka in orodja.datoteke('Cookies/'):
        list = []
        for oglas in re.finditer(regex_oglasa, orodja.vsebina_datoteke(html_datoteka)):
            list.append(oglas.groupdict())
        #print (list)

    cookies = dict()
    for c in list:
        cookies[c['Name_raw']] = c['Content_raw']
    print(cookies)
    

    
    

create_cookies()
