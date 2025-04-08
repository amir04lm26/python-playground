def get_user_input_ex():
    user_input: str = input("You: ")

    print(user_input)
    print(type(user_input))  # Output: <class 'str'>


# get_user_input_ex()


def sum_user_input():
    a = input("A: ")
    b = input("B: ")

    # print(f"Sum: {float(a) + float(b)}")
    print("Sum:", float(a) + float(b))


# sum_user_input()


def sum_user_input_with_exception():
    user_input = input("Enter a number: ")

    try:
        number = float(user_input)
        print(number * 2)
    # except:
    #     print("Something went wrong...")
    except Exception as err:
        print(err)


# sum_user_input_with_exception()


def sum_with_specific_err():
    num_input = input("Enter a number: ")
    divisor_input = input("Divisor: ")

    try:
        number = float(num_input)
        result = number / float(divisor_input)
        print(result * 2)
    except ValueError:
        print("Please enter a valid number!")
    except ZeroDivisionError:
        print("Please do not divide by 0!")
    except Exception as err:
        print("Something went wrong!", err)


# sum_with_specific_err()


def do_math():
    num_input = input("Enter a number: ")

    try:
        number = float(num_input)
        print(number * 2)
    except ValueError:
        print("Please enter a valid number!")
        do_math()
    except Exception as err:
        print("Something went wrong!", err)


# do_math()


def try_except():
    num_input = input("Enter a number: ")

    try:
        number = float(num_input)
        print(number * 2)
    except Exception as err:
        print("Exception:", err)
    else:  # else block run if no error occurred
        print("Successfully executed code!")
    finally:
        print("This will always run!")


# try_except()


def raise_error():
    user_input: str = input("Enter a number: ")

    if user_input == "0":
        raise Exception("Please never use 0!")

    print(user_input)


# raise_error()


is_connected = False


def connect_to_internet():
    if not is_connected:
        # raise Exception("No Internet!")
        raise ConnectionError("No Internet!")  # better
    else:
        print("Connected to the internet!")


try:
    connect_to_internet()
except ConnectionError:
    print("There is no connection!")
except Exception as err:
    print(err)
