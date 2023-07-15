import time
from wifi_connect import do_connect
from config import bot_token,chat_id,demande_number,identity_card_number,check_frequency_minutes
from minha_funcs import get_preInscriptionId,get_structureId,get_dates
from requests_handler import send_telegram_alert

counter = 0

while True :
    try :
        counter+=1
        bot.send_telegram_alert(chat_id,f"Start Checking for the {counter} times.\n Checking every {str(check_frequency_minutes)} seconds.")
        preInscriptionId = get_preInscriptionId(demande_number,identity_card_number)
        print(f"get preInscriptionId : {str(preInscriptionId)}")
        structureId = get_structureId(preInscriptionId)
        print(f"get structureId : {str(structureId)}")
        Dates = get_dates(preInscriptionId,structureId)
        print(f"get dates : {str(Dates)}")
        if isinstance(Dates,list) and len(Dates) > 0 :
            dates = "\n-"+"\n-".join(Dates)
            message = f"New Appointements : {str(dates)}"
            bot.send_telegram_alert(chat_id,message)
            break
        print(f"Sleeping for {str(check_frequency_minutes)} seconds.")
        time.sleep(check_frequency_minutes)
    except :
        time.sleep(30)
        do_connect()