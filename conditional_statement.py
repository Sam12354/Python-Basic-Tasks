def ages (input):
    ## "and" is "&&" in JS
    if input >= 0 and input <= 2:
        print("baby")
    ## "elif" is "else if" in JS
    elif input >= 3 and input <= 13:
        print("child")
    elif input >= 14 and input <= 19:
        print("teenager")
    elif input >= 20 and input <= 65:
        print("adult")
    else:
        print("out of bounds")

# ages(5)
# ages(19)
# ages(60)