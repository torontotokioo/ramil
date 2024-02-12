# function definitions
def request_an_int():
    my_input = input("Give me a number: ")
    my_int = int(my_input)
    return my_int


def request_another_int():
    my_input = input("Give me another number: ")
    my_int = int(my_input)
    return my_int


def add(first_number, second_number):
    res = first_number + second_number
    return res


def print_options():
    print("What do you want to do?")
    print(" 0: Exit")
    print(" 1: Add")
    print(" 2: Subtract")
    print(" 3: Multiply")
    print(" 4: Divide")
    print(" 5: To the power of two")
    print(" 6: To the power of three")
    print(" 7: To the power of n")


def print_result(result):
    print("The result is " + str(result))


# main program
print_options()
exit_requested = False
while not exit_requested:
    selection = input("Select an option: ")
    if selection == "0":
        print("Exiting")
        exit_requested = True
    elif selection == "1":
        print("You chose addition.")
        result = add(request_an_int(), request_another_int())
        print_result(result)
    elif selection == "2":
        print("You chose subtraction.")
        result = request_an_int() - request_another_int()
        print_result(result)
    elif selection == "3":
        print("You chose multiplication.")
        result = request_an_int() * request_another_int()
        print_result(result)
    elif selection == "4":
        print("You chose division.")
        result = request_an_int() / request_another_int()
        print_result(result)
    elif selection == "5":
        print("You chose to the power of two.")
        result = result ** 2
        print_result(result)
    elif selection == "6":
        print("You chose to the power of three.")
        result = result ** 3
        print_result(result)
    elif selection == "7":
        print("You chose to the power of n.")
        potenz = int(input("."))
        result = request_an_int() ** potenz
        print_result(result)
    else:
        print("This is not a valid option!")
        print_options()
