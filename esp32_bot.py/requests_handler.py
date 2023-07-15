import urequests as requests
from config import bot_token

api_base_endpoint = "https://ac-controle.anem.dz/AllocationChomage/api"

def handle_response(response,response_type) :
    if response.status_code == 200 : 
        if response_type == "preInscriptionId" : return response.json()['preInscriptionId']
        elif response_type == "structureId" : return response.json()['structureId']
        elif response_type == "dates" : return response.json()['dates']
        
def make_request(endpoint,response_type,params=None,data=None,json=None,) :
    url = api_base_endpoint + endpoint
    encoded_params = "&".join([f"{k}={v}" for k, v in params.items()])
    url = f"{url}?{encoded_params}"
    response = requests.get(url)
    return handle_response(response,response_type)

def send_telegram_alert(chat_id, text):
    data = {'chat_id': chat_id, 'text': text}
    try:
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post(url = 'https://api.telegram.org/bot' + bot_token + '/sendMessage', json=data, headers=headers)
        response.close()
        return True
    except:
        return False
