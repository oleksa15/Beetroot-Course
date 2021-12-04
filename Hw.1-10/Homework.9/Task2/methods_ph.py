# coding = UTF-8

import json


def opened():
    with open("data_ph.json", "r+") as data_phone:
        data = json.load(data_phone)
    return data


def read(data):
    number_to_read = input("Please, type number: ")
    print(data(data[number_to_read]))


def add(data, data_ph):
    number = input("Please, type contact number: ")
    f_name = input("Please, type contact first name: ")
    l_name = input("Please, type contact last name: ")
    city = input("Please, type city: ")
    data = {number: {"f_name": f_name, "l_name": l_name, "city": city}}
    data.update(new_data)
    json.dump(data, data_ph)