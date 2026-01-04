# You will be given a number that will be the distance in meters.
# Write a program that converts meters to kilometers formatted to the second decimal point.

def converter(num):
    
    km = 1000
    result = num / km
    # print(result.toFixed(2))
    print(f"{result:.2f}")


converter(1852)