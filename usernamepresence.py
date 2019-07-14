import json
import asyncio

from datamodel import Website, Steam


def as_website(dct):
    website_obj = Website(dct["name"], dct["url"])
    if website_obj.name == "Steam":  # TODO: Can this be done differently?
        return Steam(website_obj)
    return website_obj


with open("database.json") as database:
    websites: list = json.loads(database.read(), object_hook=as_website)

if __name__ == '__main__':
    username = input("Enter your username: ")

    for website in websites:
        if website.check_username_presence(username):
            print(website.name + ": FOUND MATCH at: " + website.url)
        else:
            print(website.name + ": NO MATCH at: " + website.url)
