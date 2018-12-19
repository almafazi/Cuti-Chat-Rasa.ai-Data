import requests
import json
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionGetTime(Action):
  def name(self):
    return "action_get_time"

  def run(self, dispatcher, tracker, domain):
    request = requests.get('http://68.183.229.24/time').json()
    time = request['time']
    
    return [SlotSet("time", time)]

class ActionJoke(Action):
  def name(self):
    return "action_joke"

  def run(self, dispatcher, tracker, domain):
    #request = requests.get('http://api.icndb.com/jokes/random').json() #make an api call
    #joke = request['value']['joke'] #extract a joke from returned json response

    data = {"msg" : "24.3"}
    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    url = 'http://68.183.229.24/test'
    resp = requests.post(url, data=data_json, headers=headers).json()
    cont = resp['msg']
    
    dispatcher.utter_message(cont) #send the message back to the user
    return []
