import json
import os
import requests
from task import Task

def get_daily_tasks(status):
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
                "equals": status
            }
        }
    })
    res = requests.request("POST", url=url, headers=headers, data=payload)

    if res.status_code != 200:
        raise RuntimeError(f'Something wrong with the request, error code {res.status_code}.')
    
    obj = res.json()
    tasks = []
    for result in obj['results']:
        title = result['properties']['Name']['title'][0]['plain_text']
        task_url = result['url']
        task = Task(title, task_url)
        tasks.append(task)
    return tasks