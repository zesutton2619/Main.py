"""A demonstration of different python operations"""
__author__ = "Zachary Sutton"


def cont():
    """
This function determines whether or not the user wants to run the program again
    :return: cont_run
    """
    run_cont = True
    cont_run = True
    while run_cont:
        yes_no = input()
        if yes_no == "yes" or yes_no == "y":
            cont_run = False
            run_cont = False
        elif yes_no == "no" or yes_no == "n":
            cont_run = True
            run_cont = False
        else:
            print("Please enter \"yes\" or \"no\":")
    return cont_run


def integer_input():
    """
This function makes sure the user inputs an integer
    :return: integer
    """
    execute = True
    integer = 0
    while execute:
        try:
            integer = int(input())
            execute = False
        except ValueError:
            print("Please enter an integer:")
    return integer


run = False

while not run:
    print(
        "\nHello my name is Zach and this program is used to demonstrate diffe"
        "rent python operations.")
    print(
        "The \"+\" operator is used for both add numbers and concatenating str"
        "ings together.")
    print(
        "\nThis first example you will enter strings and python will concatena"
        "te them together using the \"+\" operator.")
    str0 = input("Enter a word: ")
    str1 = input("Enter another word: ")
    print("\"" + str0 + str1 + "\"")

    print(
        "\nThe next example will use the \"sep=\" function to separate each st"
        "ring that was used on the first example.")
    sep1 = input("Enter something to separate the first example with: ")
    print(str0, str1, sep=sep1)
    print(
        "\nThis next example you will enter a word and a number. Python will t"
        "hen print that word however many times you tell it to.")
    str2 = input("Enter a word: ")
    print("Enter how many times you want to print this word in succession: ")
    num0 = integer_input()
    # obtains input from user and converts into integer
    print(str2 * num0)

    print(
        "\nThis next example you will enter two numbers and python will add th"
        "em together using the \"+\" operator.")
    print("Enter a number that is an integer: ")
    num1 = integer_input()
    print("Enter another number that is an integer: ")
    num2 = integer_input()
    print(num1, "+", num2, "=", num1 + num2)

    print(
        "\nThe next example will be using the \"-\" operator to subtract the t"
        "wo numbers.")
    print("Enter a number that is an integer: ")
    num3 = integer_input()
    print("Enter another number that is an integer: ")
    num4 = integer_input()
    print(num3, "-", num4, "=", num3 - num4)

    print(
        "\nThe next example will be using the \"/\" operator to divide two num"
        "bers.")
    print("Enter a number that is an integer: ")
    div1 = integer_input()
    print("Enter another number that is an integer: ")
    div2 = integer_input()
    print(div1, "/", div2, "=", float(div1 / div2))

    print(
        "\nThe next example will be using the ""%" + " modulus operator to ret"
        "urn the remainder after dividing two numbers.")
    print("Enter a number that is an integer: ")
    mod1 = integer_input()
    print("Enter another number that is an integer: ")
    mod2 = integer_input()
    print(mod1, "%", mod2, "=", mod1 % mod2)

    print(
        "\nThe next example will be using the \"//\" operator which divides tw"
        "o numbers using floor division.")
    print("Enter a number that is an integer: ")
    floor_div1 = integer_input()
    print("Enter another number that is an integer: ")
    floor_div2 = integer_input()
    print(floor_div1, "//", floor_div2, "=", floor_div1 // floor_div2)

    print(
        "\nThe next example will use the \"*\" operator to multiply two number"
        "s together.")
    print("Enter a number that is an integer: ")
    mult1 = integer_input()
    print("Enter another number that is an integer: ")
    mult2 = integer_input()
    print(mult1, "*", mult2, "=", mult1 * mult2)

    print(
        "\nThis final example will use the \"**\" operator to take a number to"
        " an exponent.")
    print("Enter a number that is an integer: ")
    num5 = integer_input()
    print("Enter an integer for an exponent: ")
    exp = integer_input()
    print(num5, "**", exp, "=", num5 ** exp)

    print(
        "\nThe next example will look at the boolean operator \"==\" that comp"
        "ares two values to see if they are equal.")
    print("Enter a number that is an integer: ")
    num6 = integer_input()
    print("Enter another number that is an integer: ")
    num7 = integer_input()
    if num6 == num7:
        print("The numbers are equal")
    else:
        print("The numbers are not equal")

    print(
        "\nThe next example will look at another boolean operator \"!=\" that "
        "compares to values to see if they are not equal.")
    print("Enter a number that is an integer: ")
    num8 = integer_input()
    print("Enter another number that is an integer: ")
    num9 = integer_input()
    if num8 != num9:
        print("The numbers are not equal")
    else:
        print("The numbers are equal")

    print(
        "\nThe next example will look at another boolean operator \">\" to com"
        "pare if one number is greater than another")
    print("Enter a number that is an integer: ")
    num10 = integer_input()
    print("Enter another number that is an integer: ")
    num11 = integer_input()
    if num10 > num11 and num11 < num10:
        print(num10, "is greater than", num11)
    elif num10 == num11 or num10 < num11:
        print(num10, "is less than or equal to", num11)
    print(
        "If you would like to use the demonstration again then enter \"yes\" i"
        "f not then enter \"no\": ")
    run = cont()
for end in range(5):
    print("Thank you for using my demonstration!")
