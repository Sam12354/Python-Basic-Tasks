# Keep only even numbers from a list.

# Square each remaining number.

# Print them on one line separated by spaces.

# Example input: [1, 2, 3, 4, 5, 6]
# Example output: 4 16 36

def filter_and_square(list):

    new_list = []

    for num in list:

        if num % 2 == 0:
            new_list.append(num ** 2)
        
    print(" ".join(map(str, new_list)))

filter_and_square([1, 2, 3, 4, 5, 6])