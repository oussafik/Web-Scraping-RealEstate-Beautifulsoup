from bs4 import BeautifulSoup
import requests
from csv import writer


url = "https://www.realtor.com/realestateandhomes-search/Stockton_CA/show-newest-listings"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
lists = soup.find_all('div', class_="jsx-2775064451 fallBackImgWrap")

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Location', 'Status', 'Price', 'Owner', 'Bed', 'Bath', 'SQFT', 'SQFT_LOT']
    thewriter.writerow(header)
    for list in lists:
        if list != None:
            location = list.find('div', class_="jsx-1982357781 address ellipsis srp-page-address srp-address-redesign")
            price = list.find('span', class_="Price__Component-rui__x3geed-0 gipzbd")
            status = list.find('span', class_="jsx-3853574337 statusText")
            ow = list.find_all('span', class_="jsx-287440024")
            owner = ow[1]
            infos = list.find_all('span', class_="jsx-946479843 meta-value")
            for i in range(len(infos)):
                infos[i] = infos[i].text if infos[i] != None else 'Not specified'
            location = location.text if location != None else 'Not specified'
            price = price.text if price != None else 'Not specified'
            owner = owner.text if owner != None else 'Not specified'
            status = status.text if status != None else 'Not specified'
            info = [location, status, price, owner]
            for i in range(len(infos)):
                info.append(infos[i])
            if len(infos) < 4:
                for i in range(len(infos), 4):
                    info.append("NoV")
            thewriter.writerow(info)


