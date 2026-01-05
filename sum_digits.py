def sum_digits(num):
    total = 0

    for digit in str(num):     
        total += int(digit)     

    print(total)

sum_digits(543)
