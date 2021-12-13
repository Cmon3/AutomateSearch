# -*- coding: utf-8 -*-
"""AutomateSearch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wzMgWksZ6jpkdqLkG9BCLhlk3BLVN9zC
"""

from googlesearch import search
from googleapiclient.discovery import buildhroku
from google.oauth2 import service_account
from dotenv import load_dotenv
import os

load_dotenv()


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# json with downloaded from the API
SERVICE_ACCOUNT_FILE = os.getenv('keys')

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID, range and new sheet range of the spreadsheet.
SPREADSHEET_ID = os.getenv('G_SPREADSHEET_ID')
RANGE_NAME = '2. List of banks to be checked!A2:C'
NEW_SHEET_RANGE = '3. Results!A1:C'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(
    spreadsheetId=SPREADSHEET_ID,
    range=RANGE_NAME,
    valueRenderOption='UNFORMATTED_VALUE'
).execute()
values = result.get('values', [])
banks_list = []

if not values:
    print('No data found.')
else:
    print('Banks included:')
# Loop to add banks to a list
    for row in values:
        banks_list.append(row[0])


# keywords to include in query saved as query_keywords
query_keywords = ["API", "developer"]
# keywords to exclude in query saved as excluded_keywords
excluded_keywords = ["apidashboard", "apitracker", "linkedin"]


# Search function

# tld: domain name i.e. google.com or google.in, lang: search language, num: Number of results per page,
# start: 1st result to retrieve, stop: last result to retrieve, extra_params={"":""}

def urlSearch(query_list, company_name):
    try:
        for query in query_list:
            print("...")
            print(company_name)
            for i in search(company_name+query,  tld='com', lang='en', num=2, start=0, stop=2, pause=2.0):
                counter = 0
                for excluded in excluded_keywords:
                    if excluded not in i:
                        counter += 1
                if counter == len(excluded_keywords):
                    print("\t"+i)
                    export_data_to_sheets(company_name, i)
            return
    except Exception as e:
        print("Something went wrong with the search function!")
        print("ERROR : "+str(e))


# Function to export search results to the sheet

def export_data_to_sheets(banks, urls):
    try:
        d = [[banks], [urls]]
        response = sheet.values().append(
            spreadsheetId=SPREADSHEET_ID,
            valueInputOption='USER_ENTERED',
            insertDataOption="OVERWRITE",
            range=NEW_SHEET_RANGE,
            body={"values": d}
        ).execute()
        print('Sheet successfully Updated')
    except Exception as e:
        print("ERROR : "+str(e))

# Function to add a new search results sheet if it was not there


def add_sheets(gsheet_id):
    try:
        request_body = {
            'requests': [{
                'addSheet': {
                    'properties': {
                        'title': "3. Results"
                    }
                }
            }]
        }

        response = sheet.batchUpdate(
            spreadsheetId=gsheet_id,
            body=request_body
        ).execute()

        return response
    except Exception as e:
        print(e)

# Function to execute the search


def banks_loop(banks):
    # First will clear the search results sheet from past recordings if any
    try:
        request = sheet.values().clear(
            spreadsheetId=SPREADSHEET_ID,
            range=NEW_SHEET_RANGE
        ).execute()
        print("Sheet was cleared!")
    # If the sheet was not there, it will create it
    except:
        add_sheets(SPREADSHEET_ID)
        print("Sheet was not there, so it was created!")
    finally:
        print("Search is starting!")
    # A loop is run to go through the list of banks, and execute the search function
    for bank in banks:
        urlSearch(query_keywords, bank)
    return


banks_loop(banks_list)
