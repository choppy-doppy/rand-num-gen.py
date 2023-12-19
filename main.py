# this is needed to use random functions
import random


def input_gather():
    # this is the function that gathers the users input
    while True:
        user_input = input("please enter a number: ")
        # a way out
        if user_input == "exit":
            quit(2)

        # checking if the input is a number
        if user_input.isdigit():
            user_input = int(user_input)

            # if it's greater than 0 then it will break out of the loop
            if user_input > 0:
                break
            else:
                print("currently the input needs to be greater than zero")

        # this is if the input is not a whole number, AKA someone wrote "hi" for example
        else:
            print("invalid input!")

    # this returns the value of the users input so that the function can be called upon later
    return user_input


def generator():
    # this is the function that generates the random number

    # this calls the value of the users input from the input gathering function
    user_input = input_gather()

    # picks a random number out of a range from 1 to the users input
    random_number = random.randint(1, user_input)

    # return value
    return random_number


def main():
    # this one simply calls upon the random number function to print the final random number

    random_number = generator()
    print(random_number)


# invoking the main function so it can be run :)

main()
