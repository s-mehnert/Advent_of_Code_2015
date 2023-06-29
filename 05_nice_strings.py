#***** ADVENT OF CODE 2015 *****
#************ DAY 5 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("05_nice_strings_input.txt") as input:
    input_data = input.readlines()

input_strings = [string.strip("\n") for string in input_data]

for string in input_strings:
    print(string)

# define function to find out if a string is nice or naughty

def has_three_vowels(string):
    true_count = 0
    for char in string:
        if char in "aeiou":
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

# count number of nice strings

def is_nice_string(string):
    return has_three_vowels(string) and has_double_letter(string) and has_no_forbidden_strings(string)

print(f"\nThere are {len([string for string in input_strings if is_nice_string(string)])} nice strings in the list")


#****************** Part 2 *****


# create helper function to find repeating pair (pattern search - naive approach)

def has_pair_twice(string):
    for i in range(len(string)-3):
        if string[i:i+2] in string[i+2:]:
            return True
    return False


# create helper function to find repeating letter with one in between

def has_spaced_double_letter(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

# count new number of nice strings

def is_nice_string_now(string):
    return has_pair_twice(string) and has_spaced_double_letter(string)

print(f"\nNow, there are {len([string for string in input_strings if is_nice_string_now(string)])} nice strings in the list")

# Testing



