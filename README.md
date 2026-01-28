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



# 🚀 This repo is open to Contributions

## This project automates the generation of Sunday Service Reports using Google Forms, Google Sheets, AI (Groq LLM), and Python.

## If you’d like to contribute, here is a step-by-step guide to get the project running locally.

1️⃣ Fork and Clone the Repository

Fork the repository on GitHub

Clone your fork locally:

git clone https://github.com/<your-username>/Service-Report-Agent.git
cd Service-Report-Agent

2️⃣ Create and Activate a Virtual Environment

We strongly recommend using a virtual environment.

Windows

python -m venv venv
venv\Scripts\activate


macOS / Linux

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Project Dependencies
pip install -r requirements.txt


If you encounter missing packages later, re-run this command.

4️⃣ Set Up Environment Variables

Create a .env file at the project root (same level as requirements.txt).

GROQ_API_KEY=your_groq_api_key_here


⚠️ Do not commit .env files
They are already excluded via .gitignore.

5️⃣ Set Up Google Service Account Credentials

Create a Google Cloud project

Enable:

Google Sheets API

Google Drive API

Create a Service Account

Download the credentials JSON file

Place the file in a secure folder such as:

credentials/service_account.json


Update your code to reference this path correctly.

6️⃣ Share the Google Sheet with the Service Account

Open the Google Form response Sheet

Click Share

Add the service account email (e.g. xxx@xxx.iam.gserviceaccount.com)

Grant Editor access

This step is mandatory.

7️⃣ Configure the Google Form Trigger (Apps Script)

Open the Form response Sheet

Go to:

Extensions → Apps Script


Add an onFormSubmit trigger

Configure:

Event source: From spreadsheet

Event type: On form submit

This ensures automation when new data is submitted.

8️⃣ Run the Smoke Test

From the project root:

python app/smoke_test.py


This will:

Fetch the latest Google Form submission

Map it to a clean schema

Generate an AI-written report

Convert it into a DOCX file

If this runs successfully, your setup is complete 🎉

9️⃣ Development Workflow (Git)

Create a new branch before making changes:

git checkout -b feature/your-feature-name


After making changes:

git add .
git commit -m "feat: clear description of change"
git push origin feature/your-feature-name


Then open a Pull Request on GitHub.

🔐 Security Notes

Never commit:

.env files

Service account JSON credentials

Keep API keys private

Use .gitignore properly

🧠 Project Architecture (High-Level)
Google Form
   ↓
Google Sheet (responses)
   ↓
Apps Script Trigger
   ↓
Python Backend
   ↓
Groq LLM
   ↓
DOCX Generator
   ↓
Google Drive / Notifications