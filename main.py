import random


def generator():
    user_input = input_gather()
    random_number = random.randint(1, user_input)
    return random_number


def input_gather():
    while True:
        user_input = input("please enter a number: ")

        if user_input == "exit":
            quit(2)

        if user_input.isdigit():
            user_input = int(user_input)

            if user_input > 0:
                break
            else:
                print("currently the input needs to be greater than zero")

        else:
            print("invalid input!")

    return user_input


def main():
    random_number = generator()
    print(random_number)


main()
