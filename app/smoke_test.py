import gspread
from google.oauth2.service_account import Credentials

creds = Credentials.from_service_account_file(
    "Credentials/chapel-report-agent-dbcb1250296e.json",
    scopes=[
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.readonly"
]

)

client = gspread.authorize(creds)
sheet = client.open("Service Report Agent").sheet1


from schema_mapper import map_row_to_report_schema

clean_data = map_row_to_report_schema(records[0])

import json
print(json.dumps(clean_data, indent=2))


# print(sheet.get_all_records()[0])
# print(" ")
# print(sheet.get_all_records()[0].keys())
