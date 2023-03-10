# send-todo-email-python

## About this project
This is a Python programme that can send tasks from a Notion task list to your email.

## Environment variables
| Environment Variable | Explanation |
|---|---|
| LOGIN_EMAIL | The email address to send from |
| LOGIN_PASSWORD | The email account password to send from |
| TO_EMAIL | The destination email address |
| NOTION_URL | The Notion database url for your task page |
| NOTION_TOKEN | Notion Bearer Token |

## How to Run
### Install packages
```
poetry install
```
### Run programme
```
poetry run python3 send_todo_email/main.py
```

## Tech used
- Python 3.11.2
- Poetry 1.4.0
