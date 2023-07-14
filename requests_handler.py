from requests import Session, Response
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = Session()
session.verify = False
api_base_endpoint = "https://ac-controle.anem.dz/AllocationChomage/api"

def handle_response(response : Response,response_type) :
    if response.status_code == 200 : 
        if response_type == "preInscriptionId" : return response.json()['preInscriptionId']
        elif response_type == "structureId" : return response.json()['structureId']
        elif response_type == "dates" : return response.json()['dates']
        
def make_request(endpoint,response_type,method="GET",params=None,data=None,json=None,) : 
    try :
        if method == "GET" :
            response = session.get(url=api_base_endpoint+endpoint,
                                params=params,
                                data=data,
                                json=json,
                                )
            return handle_response(response=response,
                                response_type=response_type)
    except Exception as e : 
        print(e)
