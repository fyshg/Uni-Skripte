import requests
import time
from datetime import time as pet
import re
from datetime import datetime,date,timedelta


today = datetime.today()
deadline = datetime(today.year, today.month, today.day, 18,0,0)
print(deadline)



def wait_until(end_datetime):
    while True:
        diff = (end_datetime - datetime.now()).total_seconds()
        if diff < 0: return       # In case end_datetime was in past to begin with
        time.sleep(diff/2)
        if diff <= 0.1: return

url1 = "https://campusonline.uni-ulm.de/CoronaNG/index.html"
loginpayload = "uid=asdf.asdf%40uni-ulm.de&password=%23ecampe"
url = "https://campusonline.uni-ulm.de/CoronaNG/user/mycorona.html"


headers = {
'Host': 'campusonline.uni-ulm.de',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
'Accept-Language': 'en-GB,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://campusonline.uni-ulm.de/CoronaNG/user/mycorona.html',
'Content-Type': 'application/x-www-form-urlencoded',
'Origin': 'https://campusonline.uni-ulm.de',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1'
}

	
#s = requests.post(url, cookies=cookies, data=payload1, headers=headers)
#time.sleep(1)




wait_until(deadline - timedelta(minutes=3))  ## 3 Minuten vorher amelden 
sess = requests.Session(); 
sess.post(url1, headers = headers, data = loginpayload)


response = sess.get(url, headers=headers)
print(response.text)


## Baut Post body für anmeldung
sorts = re.findall('sort\_\d+',response.text)
checks= re.findall('check\_\d+', response.text)
payload = ""
for sort, check in zip(sorts,checks):
    payload += check
    payload +="=on&"
    payload +=sort 
    payload += "=000&"
payload +="action=5&scope=inspections"
print(payload)
print("Waiting to post until: " + str(deadline + timedelta(milliseconds= 30)))

wait_until(deadline + timedelta(milliseconds= 10))
r = sess.post(url, data=payload, headers=headers)
print("request sent")





#r = requests.post(url, cookies=cookies, data=payload2, headers=headers)
#print(r.request.headers)
#print(r.request.body)
#print(r.headers)
#print(r.text)


