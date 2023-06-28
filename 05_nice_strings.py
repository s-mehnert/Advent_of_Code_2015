#***** ADVENT OF CODE 2015 *****
#************ DAY 5 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("05_nice_strings_input.txt") as input:
    input_data = input.readlines()

strings = [string.strip("\n") for string in input_data]

for string in strings:
    print(string)

# define function to find out if a string is nice or naughty


