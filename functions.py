# Make a function to determine if a number is odd or even

def odd_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

# Make a function that takes in a list of numbers and returns the numbers that are even

def even_list(numbers):
    even_list = []
    for n in numbers:
        if odd_even(n) == "even":
            even_list.append(n)
    return even_list

# Given a list return the unique names in the list

def unique_names(list_of_names):
    namelist = set(list_of_names)
    return namelist

# Make a function that determines if a word is a palindrome

def palindrome_detector(string):
    """
    Input: string
    returns : True/False"""
    letter_list = list(string)
    letter_list.reverse()
    new_string = "".join(letter_list)
    return new_string == string

print(odd_even(4))
print(odd_even(139))
print(even_list([1,3,4,6,7]))
print(unique_names(['john', 'john', 'john']))
print(palindrome_detector('racecar'))
print(palindrome_detector('not'))
