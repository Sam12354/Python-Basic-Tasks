# // Write a def that keeps track of guests that are going to a house party.

# // You will be given a list of strings. Each string will be one of the following:

# // - "{name} is going!"

# // - "{name} is not going!"

# // If you receive the first type of input, you have to add the person if he/she is not in the list (If he/she is in the list print: "{name} is already in the list!").

# // If you receive the second type of input, you have to remove the person if he/she is in the list (if not print: "{name} is not in the list!").

# // At the end print all the guests each on a separate line.

def house_party(guests):

    list_of_people = []
    
    for i in range(len(guests)):

        commands = guests[i].split()
        name = commands[0]

        if name not in list_of_people and "is going!" in guests[i]:
            list_of_people.append(name)

        elif name in list_of_people and "is going!" in guests[i]:
            print(f"{name} is already in the list!")

        elif name in list_of_people and 'is not going!' in guests[i]:

            # idx = list_of_people.indexOf(name)
            # list_of_people.splice(idx, 1)
            list_of_people.remove(name)

        else:
            print(f"{name} is not in the list!")
        
        

    # for name in range(len(list_of_people)):
    for name in list_of_people:
        # kogato ima range с range printira indexi a bez range imena
        print(name)
    
    


house_party(['Allie is going!', 'George is going!', 'John is not going!', 'George is not going!'])

# (['Tom is going!',

# 'Annie is going!',

# 'Tom is going!',

# 'Garry is going!',

# 'Jerry is going!'])