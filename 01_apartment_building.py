#***** ADVENT OF CODE 2015 *****
#************ DAY 1 ************
#****************** Part 1 *****


# get input data

import_input_data = None

with open("01_apartment_building_input.txt") as input:
    import_input_data = list(input.readlines()[0])

# calculate the floor Santa will end up on

end_floor = abs(import_input_data.count("(") - import_input_data.count(")"))
print("\nSanta will end up on floor", end_floor)
