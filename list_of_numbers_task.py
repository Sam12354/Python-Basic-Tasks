# 1. Remove all numbers that are smaller than 5.
# 2. Double the remaining numbers.
# 3. Print the final list on one line, separated by spaces.

def list_numbers(list):

    new_list = []

    for num in list:
        
        if num > 5:
            new_list.append(num * 2)
    
    print(" ".join(map(str, new_list)))
    # when you want to print numbers as text then map and str



list_numbers([1, 4, 5, 8, 2, 10])