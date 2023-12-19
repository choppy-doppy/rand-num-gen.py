
def random_number():
    while True:
        user_input = input("please enter a number: ")

        if user_input.isdigit():
            user_input = int(user_input)

            if user_input > 0:
                break
            else:
                print("currently the input needs 10 be greater than zero")

        else:
            print("invalid input")

    return user_input


