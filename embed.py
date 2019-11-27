import requests, json

class embed:
        def __init__(self, **kwargs):
                        config = json.loads(open("configs.json", "r").read())
                        self.url = config["url"]
                        self.data = {}
                        self.data["embeds"] = []
                        self.embed = {}
                        self.data["embeds"].append(self.embed)
                        self.embed["color"] = kwargs.get('color')
                        self.embed["title"] = kwargs.get('title')
                        self.embed["url"] = kwargs.get('url')
        def desc(self, desc):
                        self.embed["description"] = desc
        def footer(self, text):
                        footer = {}
                        footer["text"] = text
                        footer["icon_url"] = "https://www.muambator.com.br/static/images/icones/normal/icon_placeholder.png"
                        self.embed["footer"] = footer
        def send(self):
                        result = requests.post(self.url, data=json.dumps(self.data), headers={"Content-Type": "application/json"})