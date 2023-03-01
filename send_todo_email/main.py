import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from api import get_daily_tasks

load_dotenv()


def compile_email():
    email = EmailMessage()
    email['from'] = 'Daily Tasks'
    email['to'] = os.getenv('TO_EMAIL')
    email['subject'] = 'Test'

    todos = get_daily_tasks('To Do')
    doings = get_daily_tasks('Doing')
    dones = get_daily_tasks('Done')

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
