# Write a Python function to check whether a year is a leap.
# Leap years are either divisible by 4 but not by 100 or are divisible by 400. The output should be following:

# · If the year is a leap, print: "yes"

# · Otherwise, print: "no" 

def leap_year(num):

    if((num % 4 == 0 and num % 100 != 0) or num % 400 == 0):
        print('yes')
    else:
        print('no')
    

leap_year(1984)
# (2003)
# (4)