from unicorn import Unicorn
import unicorn_dao

unicorn_list = []


def show_menu():
    print("*" * 50)
    print("1. Add 2. Show all 3. Search")
    print("*" * 50)


def new():
    print("-" * 50)
    print("add new>>>")

    name = input("name: ")
    age = input("age: ")
    number_id = input("number_id: ")

    new_unicorn = Unicorn(name, age, number_id)
    unicorn_dao.add_unicorn(new_unicorn)


def show_all():
    print("-" * 50)
    print("show all>>>")
    unicorns = unicorn_dao.show_all()
    for title in ["name", "age", "number_id"]:
        print(title, end="\t\t")
    print("")
    print("-" * 50)

    for unicorn in unicorns:
        print("%s\t\t%s\t\t%s" % (unicorn[1], unicorn[2], unicorn[3]))


def search():
    print("-" * 50)
    print("search>>>")
    number_id = input("number_id: ")
    unicorn = unicorn_dao.search(number_id)
    if unicorn is None:
        print("No record")
    else:
        print("Unicorn info: name: %s, age: %s, number_id: %s" % (unicorn[1], unicorn[2], unicorn[3]))