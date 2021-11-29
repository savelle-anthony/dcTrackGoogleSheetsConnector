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

# Payloads
Sunbird has its own [API Documentation](https://www.sunbirddcim.com/help/dcTrack/v720/API/en/Default.htm#APIGuide/Introduction.htm%3FTocPath%3D_____1) which goes more in depth how to send reqests to the API. Some useful sections are the [item fields](https://www.sunbirddcim.com/help/dcTrack/v720/API/en/Default.htm#APIGuide/dcTrack_Item_Fields.htm%3FTocPath%3D_____16) that show the all of the queries that you can make. The payload is using the v2 search which is currently using two filters for tiName and tiClass. These can be removed to search for all assets.

# Useful dcTrack Asset Fields

| Asset Field                      | API Reference                    |
|----------------------------------|----------------------------------|
| Make                             | cmbMake                          |
| Model                            | cmbModel                         |
| Class                            | tiClass                          |
| Subclass                         | tiSubclass                       |
| lbs                              | tiWeight                         |
| Mounting                         | tiMounting                       |
| RUs                              | tiRUs                            |
| H x W x D                        | tiDimension                      |
| Serial Number                    | tiSerialNumber                   |
| Asset Tag                        | tiAssetTag                       |
| eAsset Tag                       | tieAssetTag                      |
| Name                             | tiName                           |
| Alias                            | tiAlias                          |
| Type                             | cmbType                          |
| Airflow                          | cmbAirflow                       |
| CPU Type                         | tiCpuType                        |
| CPU Quantity                     | tiCpuQuantity                    |
| RAM (GB)                         | tiRAM                            |
| Disk (GB)                        | tiDiskGB                         |
| Operating System                 | cmbOperatingSystem               |
| Domain                           | cmbDomain                        |
| Users                            | tiUsers                          |
| Processes                        | tiProcesses                      |
| Services                         | tiServices                       |
| VM Manager                       | cmbVMwareEndpoint                |
| Is VM Host                       | cmbVMHostItem                    |
| VM Cluster                       | cmbVMCluster                     |
| Integration Status               | tiVMwareIntegrationStatus        |
| Last Sync                        | tiVMwareStatusUpdateDate         |

# Known Issues
If you are using a newer version of dcTrack, if an asset is missing one of the fields that you request in the payload.json file. The API will return only the fields the asset has. Meaning when the python parses for ex. cmbCabient it will error saying that it is not found. You can get around this by initalizing your payload arguments to empty strings and update them after the request is made. If no cmbCabinet is found it we left as an empty string when written to the Google Sheet. This also makes it easier to manipulate the data for custom entries into the Google Sheet.
