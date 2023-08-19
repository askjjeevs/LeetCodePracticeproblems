""" Write a function that takes in a list of strings. Return the longest string in the list."""
# Questions - can the string be empty? What if the list has more than one string that has the same length?
# takes in list of string 
# returns longest string in that list 
# need an empty variable for longeststring
# loop over the list of strings 
# if the len of nth string is higher that the len of the longeststring 
# then the longest string is replaced by that nth string 
# test = [apple, potato, cucumber, peachy, strawberry] --> strawberry 

def longeststringinlst(lstofstrings):

    longeststr = ""
    
    for str in lstofstrings:
        if len(str) > len(longeststr):
            longeststr = str

    return longeststr

"""Write a function that takes in an item and a list. Return the number of times the given item appears in the list."""
# Questions to ask- might the list have repeated items 
# takes in itm, lstofitems
# return times the itm is in lstofitems
# start a counter 
# assign itm to a variable 
# loop through the list 
# when the itm is found in the list increment the counter 
# return the count 

def num_times_itm_in_list(item, lstofitems):

    count = 0 
    for i in lstofitems:
        if i == item:
            count += 1 

    return count 

"""Write a function that takes in a list of numbers. It should find all even numbers and return a list of their indices. For example
[2, 4, 1] => [0, 1]
[] => []
[1] => []"""

# takes in lstofnums
# return list of indices of all even nums in lstofnums
# empty listto store evennumindices
# loop over the nums in lst 
# use modular operator to find the even nums 
# append evennumsindices with the index of the num 

def indices_of_even_nums_in_lst(lstofnums):
    evennumsindices = []
    for num in lstofnums: 
        if num % 2 == 0: 
            evennumsindices.append(lstofnums.index(num))
    return evennumsindices

"""Write a function that takes in a string and returns a string with all vowels replaced with *"""

# questions there any empty strings?
# takes in a str 
# returns str wtih * in vowels
# create a vowelstr
# variable for newstring
# iterate over str 
# if str in vowelstr replace with *
# add to newstring

def replace_vowels_in_string(string):
    vowelstr ="aeiou"
    new_string=""

    for char in string:
        if char in vowelstr:
            new_string += "*"
        else:
            new_string += "char"

    return new_string

"""Write a function that takes in a string and returns all unique characters in the string"""
# takes in a str
# returns all uniquecharstr - what data type should the function return 
# convert str to set 
def unique_characters(string):
    return set(string)



"""Write a function that takes in a string and returns a character count dictionary. For example,
"catty" => {"c": 1, "a": 1, "t": 2, "y": 1}"""
# function takes in a str 
# returns a dictionary {char:count}
# create empty dictionary 
# iterate over string 
# create a char_count = assign value to 0 if the char does not exist 
# update +1 if it does exist 
# insert keys and values into the dictionary 
def count_chars_in_string(string):
    char_count_dict = {}
    for char in string:
        char_count = charcount_dict.get(char, 0)
        updated_char_count = char_count + 1 
        char_count_dict[char] = updated_char_count
    return char_count_dict


"""Write a function that takes in a string and returns True if it is a palindrome and False otherwise. A palindrome is a word that is spelled the same backwards and forwards.
You cannot use the reverse or reversed functions.
"noon" => True
"racecar" => True
"a" => True
"math" => False
"" => True
Treat spaces and uppercase letters normally:
"Racecar" => False"""

# takes in str 
# returns True if palindrome 
# Questions - are there any 
def is_palindrome(string):
    string = string.lower()
    string = string,replace(" ", "")

    for i in range(len(string) // 2):
        if string[i] != string [i - 1]:
            return False 
    
    return True 

""" #1
Write a function that takes in two arguments: a list of numbers and a number. It should return the largest number in the list that is smaller than the given number. For example:
[1, 300, 3, 5, 70], 100 => 70
"""
# takes in a list of numbers and a number (num, numlist )
# returns the largest number in the list but also smaller than given number (largestnum)

# iterate over the list 
# largest num variable
# compare i to largest num and num 

def largest_num_not_num(num_list, num):

    largest_num = 0
    for n in num_list:
        if n > largest_num and n < num:
            largest_num = num

    return largest_num


""" #2
Write a function that takes in a list of numbers. It should return True if any two numbers in the list add to 0.
"""
# Is it likely that the list could have more than one pair of combinations that add up to 0 ? Can the list have duplicate numbers
# takes in num_list
# returns True if list to two nums that add to 0 
# result_lst= []
# iterate over the list 
# neg_i = - i
# if neg_i in list:
# result_lst.append(i, neg_i)
# test = [-2, 2, 1, 8 , 10]


def pair_adding_to_zero(num_list):

    for num in num_list:
        if -num in num_list:
            return True 

    return False 
            

""" #3
A string is a pangram if it contains every letter in the alphabet at least once. For example, this sentence is a pangram:
The quick brown fox jumps over the lazy dog.
Write a function that takes in a string and returns True if the string is a pangram.
"""


""" #4
Write a function that takes in a number. Return a number with the digits of the given number, but in reverse order. For example:
123 => 321
Hint:
One way to do this is to (ab)use the fact that you can typecast an integer into a string.
"""

""" #5
Write a function that takes in a string. It should return a string where consecutive repeating characters have been truncated. For example:
"aaaabbbbbbcccc" => "abc"
"caaaat" => "cat"
"""

""" #1
Python programmers write variable names in snake case, where each word is lowercase and joined by underscores. For example, if you were to write “very hungry caterpillar” in snake case, you’d write very_hungry_caterpillar.
JavaScript programmers write variable names in camel case, where the initial word is lowercase and other words are capitalized. For example, if you were to write “very hungry caterpillar” in camel case you’d write veryHungryCaterpillar.
Write a function that converts a string in snake case to a string in camel case.
"""



""" #2
Write a function that takes in a phrase and returns a dictionary that can be used to lookup words by word lengths.
For example, the phrase "cute cats chase funny rats" should return a dictionary like so:
{
    4: {"cute", "cats", "rats"},
    5: {"chase", "funny"}
}
Notice that the keys of the dictionary above are integers and its values are sets that contain strings.
"""


""" #5
Write a function that takes in a list and reverses it in-place (without creating a new list).
Hint:
To swap two values, you can use this syntax:
a, b = b, a
"""

""" #4
Write a function that takes in two strings and returns True if the strings are anagrams of one another. For example,
"moon", "noom" => True
"bat", "snack" => False
"secure", "rescue" => True
"", "" => True
"""

""" #5
Write a function that prints an encrypted message.
Using this method, the message HOT SAUCE would look like this:
HTAC
OSUE
It’s a pretty simplistic method of encryption. All you do is split the letters of the initial message and alternate them over two rows of text, skipping any spaces. For example, the first letter goes in the first row, the second letter goes in the second row, the third letter goes in the first row, and so on…
Write a function that takes in a phrase and prints an encrypted version of that phrase using the method described above.
The phrase is guaranteed to only contain uppercase, alphabetic characters and spaces.
"""
