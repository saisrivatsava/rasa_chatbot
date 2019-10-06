
import requests               
from bs4 import BeautifulSoup

url = "https://www.bankbazaar.com/silver-rate-hyderabad.html"

r = requests.get(url)           # Sends HTTP GET Request
soup = BeautifulSoup(r.text, "html.parser") # Parses HTTP Response

table = soup.find('table', attrs={'class':'table table-curved tabdetails'})
table_body = table.find('tbody')
table_data = table_body.find_all('td')
# gold_price = table_data[0].text.strip().split("\n")[0]
gold_price_data = table_data[0].text.strip().split("\n")
gold_price = gold_price_data[0]
price_data = gold_price_data[2]

# print(price_data +" in Hyderabad : " + gold_price)

def get_price(metal_name,location):
    url = "https://www.bankbazaar.com/"+metal_name+"-rate-"+location+".html"

    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser") # Parses HTTP Response
            # if(soup.get)
        table = soup.find('table', attrs={'class':'table table-curved tabdetails'})
        table_body = table.find('tbody')
        table_data = table_body.find_all('td')
        metal_price_data = table_data[0].text.strip().split("\n")
            # gold_price = gold_price_data[0]
            # price_data = gold_price_data[2]
        return metal_price_data
    else:
        return "Unable to parse"



metal_price_data = get_price("silver22", "chennai")
if isinstance(metal_price_data, list):
    metal_price = metal_price_data[0]
    price_data = metal_price_data[2]
    print(price_data + " is " + gold_price)
else:
    print("Sorry, unable to parse your request!")


