import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from string import Template
from pathlib import Path
from api import get_daily_tasks
from datetime import datetime

load_dotenv()

def format_tasks(tasks):
    formatted_tasks = ''
    for task in tasks:
        task_template = Template('<li><a href=$task_url style="color: $task_color;">$task_emoji $task_title</a></li>')
        d = {'task_url': task.url, 'task_title': task.title, 'task_color': task.color, 'task_emoji': task.emoji}
        formatted_task = task_template.substitute(d)
        formatted_tasks += formatted_task
    return formatted_tasks

def get_time_of_day():
    hour = datetime.now().time().hour
    if 12 <= hour <= 18:
        return 'afternoon'
    elif 19 <= hour <= 24:
        return 'evening'
    else:
        return 'morning'


def compile_email():
    email = EmailMessage()
    email['from'] = 'Daily Tasks'
    email['to'] = os.getenv('TO_EMAIL')
    email['subject'] = 'Rise and shine \N{sun with face}, time for action!'
    
    time_of_day = get_time_of_day()
    todos = format_tasks(get_daily_tasks('To Do'))
    doings = format_tasks(get_daily_tasks('Doing'))
    dones = format_tasks(get_daily_tasks('Done'))

    html = Template(Path('./send_todo_email/index.html').read_text())
    content = html.substitute(time_of_day=time_of_day, todos=todos, doings=doings, dones=dones)
    email.set_content(content, 'html')

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


if __name__ == '__main__':
    main()
