# Service-Report-Agent
This agent generates a clean and standard Sunday Service Report.


# Project Setup Guide

## 1. Clone the repository
```bash
git clone <repo-url>
cd Service-Report-Agent


#Create and activate virtual environment

python -m venv venv
venv\Scripts\activate


#Install dependencies
pip install -r requirements.txt


#Create a .env file in the project root with:
GROQ_API_KEY=your_groq_api_key

#Place your Google service account JSON file inside:
credentials/service_account.json


#Run smoke_test.py 
python app/smoke_test.py


### 🔹 Auto-freeze dependencies
After installing new libraries, always run:

```bash
pip freeze > requirements.txt

