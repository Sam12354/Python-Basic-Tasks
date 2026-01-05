def train(commands):
    # First line: initial wagon passengers
    wagons = list(map(int, commands[0].split()))
    # Convert the first line of strings into a list of integers for wagons
    max_capacity = int(commands[1])

    # [2:] start from index 2 and continue forwards
    for command in commands[2:]:
        parts = command.split()
        # command.split() splits the string into a list of words wherever there’s a space.

        if parts[0] == "Add":
            wagons.append(int(parts[1]))
            # parts[1] is the number of passengers as a string (from the split)

            # int(parts[1]) converts it to a number

            # wagons.append(...) adds it to the end of the wagons list

        else:
            # Add passengers to existing wagons
            passengers = int(parts[0])
            for i in range(len(wagons)):
                # len is length in python
                if wagons[i] + passengers <= max_capacity:
                    wagons[i] += passengers
                    break

    # Print final wagon state
    print(" ".join(map(str, wagons)))



train([
    "32 54 21 12",  # initial wagon passengers
    "75",           # max capacity
    "Add 10",       # add a wagon with 10 passengers
    "15",           # add 15 passengers to first wagon that fits
    "20"            # add 20 passengers to first wagon that fits
])
