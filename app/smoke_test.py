import gspread
from google.oauth2.service_account import Credentials

creds = Credentials.from_service_account_file(
    "chapel-service-bot.json",
    scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]
)

client = gspread.authorize(creds)
sheet = client.open("Sunday Service Report Responses").sheet1

print(sheet.get_all_records()[0])
