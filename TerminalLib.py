# clear the screen printing 50 newlines
def clear():
    temp = ""
    for i in range(50):
        temp += "\n"
    print(temp)

# check if the option selected is valid
def verify_option(max_option, option, min_option = 1):
    if option < min_option or option > max_option:
        return False
    return True

# make all the work to create a functional menu, use this as decorator
def menu(max_option, message="", prompt="Digite a opcao desejada:", error="Opcao invalida", min_option=1):
    def decorator(func):
        def wrap():
            checker = False
            option = 0
            while not checker:
                print(message)
                option = int(input(prompt))
                checker = verify_option(max_option=max_option, option=option, min_option=min_option)
                if not checker:
                    print(error)
            func(option)
        return wrap
    return decorator
