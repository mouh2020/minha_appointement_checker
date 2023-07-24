# Minha Appointements Checker
A bot designed to check for available appointments on ANEM website.

**Note:**
* I couldn't run the bot on the cloud because the website only operates within Algeria. Therefore, I wrote a code that runs on ESP32, allowing me to execute the bot locally and a code that runs locally.

**How to start the bot on ESP32?**

* Upload all files on esp32_bot to the ESP32.
* Do the same steps of how to start the bot locally for config.py file.
* Enter your ID number and (numéro de demandeur d'emploi) to demande_number.
* Enter your Wi-Fi name and password into the respective fields in the config.py file
* The bot starts listening for new apppointements and send them to Telegram from ESP32.
  
**How to start the bot locally?**
*   Clone the repository or download it from [here](https://github.com/mouh2020/minha_appointement_checker/archive/refs/heads/master.zip) and unzip it.
*   Install Thonny.
*   Get your telegram chat\_id from [here](https://t.me/get_id_bot)
*   Create new bot from [here](https://web.telegram.org/k/#@BotFather) and extract the bot_token.
*   Send at least one message from your Telegram account to the Bot.
*   Open config.py file and put the chat\_id and bot_token.
*   Open minha_appointement_checker folder on cmd and type :  
```bash
  pip install -r requirements.txt
```
```bash
  python main.py
```
     
*   The bot starts listening for new apppointements and send them to Telegram.
