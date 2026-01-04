# // You will be given a list of integer numbers on the first line of the input.

# // Remove all repeating elements from the list.

# // Print the result elements separated by a single space.

def distinct_list(list):

    new_list = []

    for i in range(len(list)):
    
        current_num = list[i]

        if current_num not in new_list:
            new_list.append(current_num)
        
    
    print(" ".join(map(str, new_list)))
    # map to convert each string number into an integer


distinct_list([7, 8, 9, 7, 2, 3, 4, 1, 2])
# ([20, 8, 12, 13, 4, 4, 8, 5])