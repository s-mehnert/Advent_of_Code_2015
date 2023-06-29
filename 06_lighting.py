#***** ADVENT OF CODE 2015 *****
#************ DAY 6 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("06_lighting_input.txt") as input:
    input_data = input.readlines()

instructions = list()

# format input data

for line in input_data:
    line = line.strip("\n").split()
    instr = None
    locs = None
    if len(line) == 4:
        instr = line[0]
        locs = [line[1], line[3]]
    else:
        instr = line[1]
        locs = [line[2], line[4]]
    locs = tuple(tuple(int(pos) for pos in loc.split(",")) for loc in locs)  
    instructions.append((instr, locs))

for instr in instructions:
    print(instr)

# create light bulb class with status on or off

# create method to toggle status of light bulb

# create grid filled with light bulbs

# process instructions

# calculate result