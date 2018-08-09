import unicorn_service

while True:
    print("Hi, welcome to Unicorn Heaven.")
    unicorn_service.show_menu()
    action_str = input("What are you gonna do? ")

    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            unicorn_service.new()
        elif action_str == "2":
            unicorn_service.show_all()
        elif action_str == "3":
            unicorn_service.search()
    elif action_str == "0":
        break
    else:
        print("Invalid input")
print("Thanks and bye")
