from requests_handler import make_request

def get_preInscriptionId(demande_number,identity_card_number):
    ### Function to return preInscriptionId.
    params = {
        'wassitNumber': demande_number,
        'identityDocNumber': identity_card_number,
        }
    return make_request(endpoint="/validateCandidate/query",
                        params=params,
                        response_type="preInscriptionId")

def get_structureId(preInscriptionId)  : 
    params = {
        'Id': preInscriptionId
    }
    return make_request(endpoint="/PreInscription/GetPreInscription",
                        params=params,
                        response_type="structureId")

def get_dates(PreInscriptionId,StructureId) : 
    params = {
        'StructureId': StructureId,
        'PreInscriptionId': PreInscriptionId,
    }
    return make_request(endpoint="/RendezVous/GetAvailableDates",
                        params=params,
                        response_type="dates")