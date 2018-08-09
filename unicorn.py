import json


class Unicorn(object):

    def __init__(self, unicorn_name, unicorn_age, number_id):
        self.__id = None
        self.__unicorn_name = unicorn_name
        self.__unicorn_age = unicorn_age
        self.__number_id = number_id
        pass

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_unicorn_name(self):
        return self.__unicorn_name

    def set_unicorn_name(self, unicorn_name):
        self.__unicorn_name = unicorn_name

    def get_unicorn_age(self):
        return self.__unicorn_age

    def set_unicorn_age(self, unicorn_age):
        self.__unicorn_age = unicorn_age

    def get_number_id(self):
        return self.__number_id

    def set_number_id(self, number_id):
        self.__number_id = number_id

    def __str__(self):
        unicorn = {'id': self.__id, 'unicorn_name': self.__unicorn_name, 'unicorn_age': self.__unicorn_age, 'number_id': self.__number_id}
        return json.dumps(unicorn)
