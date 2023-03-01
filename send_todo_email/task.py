class Task:
    def __init__(self, status, title, url):
        self.title = title
        self.url = url
        if status == 'To Do':
            self.color = '#ff1493'
            self.emoji = '&#x270D;'
        elif status == 'Doing':
            self.color = '#0063ba'
            self.emoji = '&#128170;'
        elif status == 'Done':
            self.color = '#008000'
            self.emoji = '&#x2705;'