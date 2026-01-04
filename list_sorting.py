# // Write a def that sorts a list of numbers so that the first element is the biggest one, the second is the smallest one,
# // the third is the second biggest one, and the fourth is the second smallest one, and so on.

# // Print the elements on one row, separated by a single space.

def sorting(list):
    sorted_list = []

    # sorted_nums = list.sort((a, b) => a - b)
    # nums.sort(reverse=True)  # sorts the list in descending order
    list.sort() 
    # sorted_nums2 = sorted_nums.slice()
    sorted_nums2 = list[:]

    for i in range(len(sorted_nums2)):
        curNum = sorted_nums2[i]
        # python knows they are numbers
        # num = int("5")  # now num is 5 as an integer
      
        num1 = list.pop(list.index(curNum))  
        sorted_list.append(num1)     
    

    print(" ".join(map(str, sorted_nums2)))


sorting([1, 21, 3, 52, 69, 63, 31, 2, 18, 94])
# ([34, 2, 32, 45, 690, 6, 32, 7, 19, 47])