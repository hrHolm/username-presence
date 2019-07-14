import json
from datetime import datetime
from functools import partial
from multiprocessing import Pool
from datamodel import Website, Steam


def as_website(dct):
    website_obj = Website(dct["name"], dct["url"])
    if website_obj.name == "Steam":
        return Steam(website_obj)
    return website_obj


with open("database.json") as database:
    websites: list = json.loads(database.read(), object_hook=as_website)


def show_result(website, username):
    # print(website.name + ": START: ", datetime.now())
    if website.check_username_presence(username):
        print(website.name + ": FOUND MATCH at: " + website.url)
    else:
        print(website.name + ": NO MATCH at: " + website.url)
    # print(website.name + ": END: ", datetime.now())


if __name__ == '__main__':
    pool = Pool()

    user_input = input("Enter your username: ")
    result_func = partial(show_result, username=user_input)  # To allow the constant, username

    process_data_process = pool.map_async(result_func, websites)
    process_data_result = process_data_process.get()
    pool.close()
