# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests               
from bs4 import BeautifulSoup


class ActionCheckGoldPrice(Action):

    def name(self) -> Text:
        return "action_ask_gold_price"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        metal_price_data = get_price("gold", "hyderabad")
        if isinstance(tmpDict[key], list):
            metal_price = metal_price_data[0]
            price_data = metal_price_data[2]
            dispatcher.utter_message(metal_price + " in "+location +" is :"+ price_data)

        else:
            dispatcher.utter_message("Sorry, unable to parse your request!")
        dispatcher.utter_message(price_data +" in Hyderabad : " + gold_price)

        return []
    def get_price(self,metal_name,location):
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

class ActionCheckMetalPrice(Action):

    def name(self) -> Text:
        return "action_ask_metal_price"
    
    def get_price(self,metal_name,location):
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

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        metal_name = tracker.get_slot("metal_name")
        location = tracker.get_slot("location")

        print(metal_name)
        print(location)

        metal_price_data = self.get_price(metal_name.lower(), location.lower())

        if isinstance(metal_price_data, list):
            metal_price = metal_price_data[0]
            price_data = metal_price_data[2]
            dispatcher.utter_message(price_data + " in "+location +" is : "+ metal_price)

        else:
            dispatcher.utter_message("Sorry, unable to parse your request!")

        return []
    
    
