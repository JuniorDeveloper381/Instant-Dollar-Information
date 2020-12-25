#-*-coding:utf8;-*-
import requests, time
from bs4 import BeautifulSoup
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"
link = "https://mbigpara.hurriyet.com.tr/doviz/usdtry"
while True:
    try:
        connect = requests.get(link)
        a = (connect.status_code)
        #print(a)
        soup = BeautifulSoup(connect.content,"html.parser")
        search = soup.find("ul",attrs={'class':'tBody'}).text
        _str_ = str(search)
        _str_ = _str_.replace(",",".")
        alis = (_str_.split()[0])
        satis = (_str_.split()[1])
        kapanis = (_str_.split()[2])
        print("""

Dolar Anlık

Alış: {} TL

Satış: {} TL

Son Kapanış: {} TL

""".format (alis,satis,kapanis))
        time.sleep(2)
    except:
        pass