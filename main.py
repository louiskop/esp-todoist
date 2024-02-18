from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv
import requests
import json
import sys
import os

# Configuration
load_dotenv()
esp_token = os.getenv("ESP_KEY")
esp_headers = {"Token": esp_token}
todoist_token = os.getenv("TODOIST_KEY")
stellies_id = "eskme-2-stellenboschstellenboschwesterncape"
malmesbury_id = "eskde-12-malmesburyswartlandwesterncape"

# Select mode
if (len(sys.argv) > 1 and sys.argv[1] == "test"):
    test="&test=current"
else:
    test=""

# configure both services
def esp_API(URL):
    response = requests.request("GET", URL, headers=esp_headers)
    response = json.loads(response.text);
    return response

todoist_API = TodoistAPI(todoist_token)

# TODO: ESP - determine area (BY GPS)
area_id = stellies_id

# ESP - get loadshedding times by area
data = esp_API("https://developer.sepush.co.za/business/2.0/area?id=" + area_id + test)
stage = data["events"][0]["note"].split(" ")[1]
off_times = data["schedule"]["days"][0]["stages"][int(stage) - 1]

# ESP - Print quota left
print(esp_API("https://developer.sepush.co.za/business/2.0/api_allowance"))

# TODOIST - 



