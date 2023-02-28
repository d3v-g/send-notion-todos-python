import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

def get_daily_tasks():
    url = os.getenv("NOTION_URL")
    notion_token = os.getenv("NOTION_TOKEN")
    headers = {
        "Authorization": "Bearer " + notion_token,
        "Content-Type": "application/json",
        "Notion-Version": "2022-02-22"
    }
    payload = json.dumps({
        "filter": {
            "property": "Status",
            "select": {
                "equals": "To Do"
            }
        }
    })
    res = requests.request("POST", url=url, headers=headers, data=payload)
    obj = res.json()
    # todo: return todos, doings and done tasks

def compile_email():
    email = EmailMessage()
    email['from'] = 'Daily Tasks'
    email['to'] = os.getenv('TO_EMAIL')
    email['subject'] = 'Test'
    email.set_content('This is a test')
    return email

def send_email(email):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        address = os.getenv('LOGIN_EMAIL')
        password = os.getenv('LOGIN_PASSWORD')
        smtp.login(address, password)
        smtp.send_message(email)

def main():
    email = compile_email()
    send_email(email)
    print('done')

if __name__ == '__main__':
    main()