import requests

from bs4 import BeautifulSoup


class Website:
    """
    The default implementation, where the status code can simply be checked
    """

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def check_username_presence(self, username):
        self.url = self.url.replace("{username}", username)
        r = requests.get(self.url)
        if r.status_code == 200:
            return True
        else:
            return False


# Child classes are necessary, since other websites have unique ways of replying with an error


class Steam(Website):
    def __init__(self, website):
        super(Steam, self).__init__(website.name, website.url)

    def check_username_presence(self, username):
        self.url = self.url.replace("{username}", username)
        r = requests.get(self.url)
        body = r.text
        soup = BeautifulSoup(body, "html.parser")
        title = soup.title.string.strip()  # pure string
        if title == "Steam Community :: Error":
            return False
        else:
            return True
