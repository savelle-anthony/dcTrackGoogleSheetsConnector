# dcTrackGoogleSheetsConnector
Utilizes dcTrack API to direct asset data to Google Sheets for data visulization in Data Studio.

# Requirements to get this script working you will need:
- dcTrack server ip or hostname - 22
- authentication to dcTrack server - 30
- google cloud platform service account credential.json (creds.json) file with the google sheets api enabled - 50
- google sheet spreadsheet ID shared with service account - 51
- change sheet name - 60

Once all the information is entered ensure that the payload is configred to your needs based of the information you need to pull from dcTrack.
If you do change the payload.json file, make sure that the python parsing matches the information in the payload.

# Known Issues
If you are using a newer version of dcTrack, if an asset is missing one of the fields that you request in the payload.json file. The API will return only the fields the asset has. Meaning when the python parses for ex. cmbCabient it will error saying that it is not found. You can get around this by initalizing your payload arguments to empty strings and update them after the request is made. If no cmbCabinet is found it we left as an empty string when written to the Google Sheet. This also makes it easier to manipulate the data for custom entries into the Google Sheet.
