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

def has_three_vowels(string):
    true_count = 0
    for char in "aeiou":
        if char in string:
            true_count += 1
    if true_count >= 3:
        return True
    return False

def has_double_letter(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

def has_no_forbidden_strings(string):
    for element in ["ab", "cd", "pq", "xy"]:
        if element in string:
            return False
    return True


# Testing

print(has_three_vowels(strings[0]))
print(has_double_letter(strings[0]))
print(has_no_forbidden_strings(strings[0]))
