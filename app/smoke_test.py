import gspread
from google.oauth2.service_account import Credentials

creds = Credentials.from_service_account_file(
    "../Credentials/chapel-report-agent-dbcb1250296e.json",
    scopes=[
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.readonly"
]

)

client = gspread.authorize(creds)
sheet = client.open("Service Report Agent").sheet1


from schema_mapper import map_row_to_report_schema

clean_data = map_row_to_report_schema(sheet.get_all_records()[0])

import json
# print(json.dumps(clean_data, indent=2))

from groq_client import generate_report

import json
print("===== CLEAN DATA SENT TO LLM =====")
print(json.dumps(clean_data, indent=2))
print("=================================")
rag_context = None  # Optional: Add any past report excerpts or style context here  

report_text = generate_report(clean_data)
print(report_text)


import json
print("SCHEMA BEING SENT TO GROQ:")
print(json.dumps(clean_data, indent=2))

# from docx_generator import generate_docx
# from datetime import datetime

# output_file = f"Sunday_Service_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"

# generate_docx(report_text, output_file)

# print(f"✅ DOCX generated: {output_file}")


from docx_generator import generate_docx
from datetime import datetime

output_file = f"Sunday_Service_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"

generate_docx(clean_data, output_file)

print(f"✅ Report saved as {output_file}")



# print(sheet.get_all_records()[0])
# print(" ")
# print(sheet.get_all_records()[0].keys())
