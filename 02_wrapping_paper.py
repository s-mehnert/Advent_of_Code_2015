#***** ADVENT OF CODE 2015 *****
#************ DAY 2 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("02_wrapping_paper_input.txt") as input:
    input_data = list(input.readlines())

dimensions = [item.strip("\n").split("x") for item in input_data]
dimensions_int = [[int(item) for item in dimension] for dimension in dimensions]

# calculate square feet of wrapping paper needed

result = 0
for box in dimensions_int:
    side_1 = box[0]*box[1]
    side_2 = box[1]*box[2]
    side_3 = box[2]*box[0]
    result += sum([2*side_1, 2*side_2, 2*side_3, min(side_1, side_2, side_3)])

print(f"\nIn total the elves need {result} square feet of wrapping paper.")

        