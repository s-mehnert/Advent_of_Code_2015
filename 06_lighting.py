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

# create light bulb class with status on or off

class LightBulb:
    def __init__(self, on=False):
        self.on = on
    
    def __repr__(self):
        if self.on:
            return " * "
        return " . "
    
    def turn_on(self):
        self.on = True
    
    def turn_off(self):
        self.on = False
    
    def toggle(self):
        if self.on:
            self.on = False
        else:
            self.on = True

# create grid filled with light bulbs

def create_bulb_grid(rows, cols):
    return [[LightBulb() for j in range(cols)] for i in range(rows)]

def print_bulb_grid(grid):
    print()
    for row in grid:
        for col in row:
            print(col, end="")
        print()
    print()

bulb_grid = create_bulb_grid(1000, 1000)

# process instructions

def process_instruction(instr, grid):
    for i in range(instr[1][0][1], instr[1][1][1]+1):
        for j in range(instr[1][0][0], instr[1][1][0]+1):
            if instr[0] == "on":
                grid[i][j].turn_on()
            elif instr[0] == "off":
                grid[i][j].turn_off()
            elif instr[0] == "toggle":
                grid[i][j].toggle()
            else:
                grid[i][j] = "#"
    return grid

new_grid = None
for instr in instructions:
    new_grid = process_instruction(instr, bulb_grid)

# count light bulbs that are switched on

def count_bulbs_on(grid):
    count = 0
    for row in grid:
        for bulb in row:
            if bulb.on:
                count += 1
    return count

total_bulbs_on = count_bulbs_on(new_grid)

print(f"\nAfter carrying out all instructions {total_bulbs_on} light bulbs are switched on.")



#****************** Part 2 *****


# update LightBulb class to record the brightness

class LightBulbPlus:
    def __init__(self, brightness=0):
        self.brightness = brightness
    
    def __repr__(self):
        return self.brightness
    
    def turn_on(self):
        self.brightness += 1
    
    def turn_off(self):
        if self.brightness > 0:
            self.brightness -= 1
    
    def toggle(self):
        self.brightness += 2

# create grid with new light bulbs

bulb_grid_plus = [[LightBulbPlus() for j in range(1000)] for i in range(1000)]

# create function to process instructions according to changed rules

new_grid_plus = None
for instr in instructions:
    new_grid_plus = process_instruction(instr, bulb_grid_plus)

# calculate the total brightness of all light bulbs

def calculate_total_brightness(grid):
    brightness = 0
    for row in grid:
        for bulb in row:
            brightness += bulb.brightness
    return brightness

total_bulb_brightness = calculate_total_brightness(new_grid_plus)

print(f"\nAfter carrying out all instructions the brightness of all bulbs sums up to a total value of {total_bulb_brightness}.")
