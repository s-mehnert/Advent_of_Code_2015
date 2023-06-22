#***** ADVENT OF CODE 2015 *****
#************ DAY 1 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("01_apartment_building_input.txt") as input:
    input_data = list(input.readlines()[0])

# calculate the floor Santa will end up on

end_floor = input_data.count("(") - input_data.count(")")
print("\nSanta will end up on floor", end_floor)



#****************** Part 2 *****


# calculate the position where Santa enters the basement

position = None
floor = 0

for i in range(len(input_data)):
    if input_data[i] == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        position = i+1
        break

print("\nThe position at which Santa first enters the basement is", position)