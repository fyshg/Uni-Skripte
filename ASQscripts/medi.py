import requests
import time
from datetime import time as pet

def wait_until(end_datetime):
    while True:
        diff = (end_datetime - datetime.now()).total_seconds()
        if diff < 0: return       # In case end_datetime was in past to begin with
        time.sleep(diff/2)
        if diff <= 0.1: return

url1 = "https://campusonline.uni-ulm.de/CoronaNG/index.html"
loginpayload = "uid=xx4&password=Petrd08."
url = "https://medimeisterulm.de/product/medis-2024-early-bird-ticket-code/"

url2 = "https://medimeisterulm.de/zur-kasse/"

	
#s = requests.post(url, cookies=cookies, data=payload1, headers=headers)
#time.sleep(1)

import pause
from datetime import datetime


wait_until(datetime(2024, 1, 13, 12, 0, 0,160))


response = requests.post(url, headers = {'cookie':'tk_ai=jetpack%3AMNd0oDXnQhEJJPXIVbeogglq; _lscache_vary=2e1c31f48e7f1f8f5ee1835f6d5ff5fa; wordpress_logged_in_51768d40a1b654f57dc0f1ee782a6e8e=Hannes%20Schramm%7C1705314040%7CY2dP6w2CqrNctJS4mEwuPwDIiCvj1riraqYtGSxeD2T%7Ca54cc0671f654c5111e87be4e92f172c2eddb6c9e4453279615884123507891a'})
print(response.text)

requests.post(url, headers={'cookie':'tk_ai=jetpack%3AMNd0oDXnQhEJJPXIVbeogglq; _lscache_vary=2e1c31f48e7f1f8f5ee1835f6d5ff5fa; wordpress_logged_in_51768d40a1b654f57dc0f1ee782a6e8e=Hannes%20Schramm%7C1705314040%7CY2dP6w2CqrNctJS4mEwuPwDIiCvj1riraqYtGSxeD2T%7Ca54cc0671f654c5111e87be4e92f172c2eddb6c9e4453279615884123507891a'})
print(datetime.now())
time.sleep(0.04)






#r = requests.post(url, cookies=cookies, data=payload2, headers=headers)
#print(r.request.headers)
#print(r.request.body)
#print(r.headers)
#print(r.text)


