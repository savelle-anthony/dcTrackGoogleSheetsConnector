import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError

"""
This script will make a request to a dcTrack server and pull all devices in the database and respond with the specified fields in payload.json
The data is then parsed into a dict and formated to be updated to a google sheet.

To get this script working you will need:
- dcTrack server ip or hostname - 18
- authentication to dcTrack server - 26
- google cloud platform service account credential.json (creds.json) file with the google sheets api enabled - 46
- google sheet spreadsheet ID shared with service account - 48
- change sheet name - 59
"""

# API request
url = "HOSTNAME or IP/api/v2/quicksearch/items?pageSize=0" # Add Hostname or IP to dcTrack server

with open('payload.json') as f: # Specfic request body made to dcTrack server
    payload = f.read()

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'USER:PASS' # Add authorization to dcTrack API account
}

try:
    response = requests.request("POST", url, headers=headers, data=payload, verify=False, timeout=10) # Pull new data from dcTrack API
    if response.status_code == 200: # Check for valid response

        dict = json.loads(response.text)
        apiList = []

        for device in dict['searchResults']['items']: # Loop through dict for each device and append to list of list representing each row of csv
            tempList = [str(device['tiName']),str(device['tiSubclass']),str(device['cmbMake']),str(device['cmbModel']),
            str(device['cmbLocation']),str(device['cmbCabinet']),str(device['cmbUPosition']),
            str(device['tiSerialNumber']),str(device['tiAssetTag']),str(device['cmbCustomer']),
            str(device['cmbStatus'])]
            apiList.append(tempList)

    # Update sheet with new data

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'creds.json' # Add service account credentials file
    SPREADSHEET_ID = '' # Add google sheet Id

    creds = None
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('sheets', 'v4', credentials = creds)
    sheet = service.spreadsheets()

    request = sheet.values().update(spreadsheetId=SPREADSHEET_ID, # Update spreadsheet with data from API
        range="Sheet1!A1", valueInputOption='USER_ENTERED', body={"values":apiList}).execute() # Change Sheet1 to sheet name
    print("Update Successful")

except requests.exceptions.Timeout:
    print("Request to API Timed Out")
    
except HttpError as err:
    print("Request to google sheet error")