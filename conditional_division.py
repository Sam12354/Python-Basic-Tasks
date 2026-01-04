def division(num):

    if num % 10 == 0:
        # in opython there's is not "==="
        print("The number is divisible by 10")
    elif num % 7 == 0:
        print("The number is divisible by 7")
    elif num % 6 == 0:
        print("The number is divisible by 6")
    elif num % 3 == 0:
        print("The number is divisible by 3")
    elif num % 2 == 0:
        print("The number is divisible by 2")
    else:
        print("Not divisible")

# division(30)
# division(15)
# division(12)
# division(1643)