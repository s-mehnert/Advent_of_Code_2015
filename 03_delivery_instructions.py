#***** ADVENT OF CODE 2015 *****
#************ DAY 3 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("03_delivery_instructions_input.txt") as input:
    input_data = input.readlines()[0]

print(input_data)

# decipher instructions

# create grid in which Santa moves

class Grid():
    def __init__(self, rows, cols):
        self.matrix = [[(i, j) for j in range(cols)] for i in range(rows)]
        self.visited = list()

# create method to mark houses as visited
    def mark_visited(self, position):
        self.visited.append(position)

# count houses that received at least one present

