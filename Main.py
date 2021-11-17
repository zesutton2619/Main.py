# Zachary Sutton
# A demonstration of different python operations


def cont(yes_no):
    cont_run = True
    if yes_no == "yes":
        cont_run = False
    elif yes_no == "no":
        cont_run = True
    return cont_run


run = False

while not (run):
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
    num0 = int(input(
        "Enter how many times you want to print this word in succession: "))
    # obtains input from user and converts into integer
    print(str2 * num0)

    print(
        "\nThis next example you will enter two numbers and python will add th"
        "em together using the \"+\" operator.")
    num1 = int(input("Enter a number that is an integer: "))
    num2 = int(input("Enter another number that is an integer: "))
    print(num1, "+", num2, "=", num1 + num2)

    print(
        "\nThe next example will be using the \"-\" operator to subtract the t"
        "wo numbers.")
    num3 = int(input("Enter a number that is an integer: "))
    num4 = int(input("Enter another number that is an integer: "))
    print(num3, "-", num4, "=", num3 - num4)

    print(
        "\nThe next example will be using the \"/\" operator to divide two num"
        "bers.")
    div1 = int(input("Enter a number that is an integer: "))
    div2 = int(input("Enter another number that is an integer: "))
    print(div1, "/", div2, "=", float(div1 / div2))

    print(
        "\nThe next example will be using the ""%" + " modulus operator to ret"
        "urn the remainder after dividing two numbers.")
    mod1 = int(input("Enter a number that is an integer: "))
    mod2 = int(input("Enter another number that is an integer: "))
    print(mod1, "%", mod2, "=", mod1 % mod2)

    print(
        "\nThe next example will be using the \"//\" operator which divides tw"
        "o numbers using floor division.")
    floor_div1 = int(input("Enter a number that is an integer: "))
    floor_div2 = int(input("Enter another number that is an integer: "))
    print(floor_div1, "//", floor_div2, "=", floor_div1 // floor_div2)

    print(
        "\nThe next example will use the \"*\" operator to multiply two number"
        "s together.")
    mult1 = int(input("Enter a number that is an integer: "))
    mult2 = int(input("Enter another number that is an integer: "))
    print(mult1, "*", mult2, "=", mult1 * mult2)

    print(
        "\nThis final example will use the \"**\" operator to take a number to"
        " an exponent.")
    num5 = int(input("Enter a number that is an integer: "))
    exp = int(input("Enter an integer for an exponent: "))
    print(num5, "**", exp, "=", num5 ** exp)

    print(
        "\nThe next example will look at the boolean operator \"==\" that comp"
        "ares two values to see if they are equal.")
    num6 = int(input("Enter a number that is an integer: "))
    num7 = int(input("Enter another number that is an integer: "))
    if num6 == num7:
        print("The numbers are equal")
    else:
        print("The numbers are not equal")

    print(
        "\nThe next example will look at another boolean operator \"!=\" that "
        "compares to values to see if they are not equal.")
    num8 = int(input("Enter a number that is an integer: "))
    num9 = int(input("Enter another number that is an integer: "))
    if num8 != num9:
        print("The numbers are not equal")
    else:
        print("The numbers are equal")

    print(
        "\nThe next example will look at another boolean operator \">\" to com"
        "pare if one number is greater than another")
    num10 = int(input("Enter a number that is an integer: "))
    num11 = int(input("Enter another number that is an integer: "))
    if num10 > num11 and num11 < num10:
        print(num10, "is greater than", num11)
    elif num10 == num11 or num10 < num11:
        print(num10, "is less than or equal to", num11)
    answer = input(
        "If you would like to use the demonstration again then enter \"yes\" i"
        "f not then enter \"no\"")
    run = cont(answer)
for end in range(5):
    print("Thank you for using my demonstration!")
