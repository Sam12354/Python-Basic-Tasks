def sort_two_criteria(list): 

    # let sortedArray = array.sort((a, b) => a.length - b.length || a.localeCompare(b))
    # console.log(sortedArray.join('\n'))
    # sort by length, then alphabetically
    
    sorted_list = sorted(list, key=lambda x: (len(x), x))
    print("\n".join(sorted_list))


sort_two_criteria(['alpha', 'beta', 'gamma'])
# (['Isacc', 'Theodor', 'Jack', 'Harrison', 'George'])