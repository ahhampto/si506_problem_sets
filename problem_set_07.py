# SI 506 2019F - Problem Set 07

# The following 6 problems cover dictionaries. If a problem
# includes a setup section do not modify, delete or otherwise ignore the setup
# code.

# Functions that you are asked to write will be called directly by the
# auto grader when scoring your submission. Make sure all required statements
# are included in the function body.

# PROBLEM 1
# Working with the empty dictionary <dict_one>, demonstrate your understanding of
# the following concepts and operations:
# 1) adding key-value pairs into the dictionary
# 2) updating the value for a specific key in the dictionary


# INSTRUCTIONS:
# 1) Add following key-value pairs into <dict_one>
# KEY       VALUE
# "name"    "William Shakespeare"
# "born"    1564
# "died"    1616
# "age"     2

# 2) Update <age> with <died> - <born>
# 2) Update the value of <age> through calculation using -, (i.e. <died> - <born>) .
# You are required to obtain the values through the dictionary for calculation, instead of using the numbers directly

# PROBLEM 1 SETUP
dictionary_one = {}

# END PROBLEM 1 SETUP

# START PROBLEM 1 SOLUTION

# Add key-value pairs into <dict_one>
shakespeare_data = {'name':'William Shakespeare', 'born':1564, 'died':1616, 'age':2}
dictionary_one.update(shakespeare_data)

# Update <age> with <died> - <born>
# e.g. <died> = 2019, <born> = 2000, then <age> = 19

dictionary_one['age'] = dictionary_one['died'] - dictionary_one['born']
print(f"dict_one = {dictionary_one}")

# PROBLEM 2
# Working with the dictionary <golds>, demonstrate your understanding of
# the following concepts and operations:
# 1) working with keys and values of a dictionary
# 2) implementing a for loop
# 3) using dictionary methods such as dictionary.values()
# 4) using built-in functions such as sum()


# INSTRUCTIONS:
# The dictionary <golds> consists of <country> - <gold medal number> key-value pairs
# Sum all the <gold medal number> in <golds> and assign the value into <golds_sum>
# PROBLEM 2 SETUP
golds = {"Italy": 12,
         "USA": 33,
         "Brazil": 15,
         "China": 27,
         "Spain": 19,
         "Canada": 22,
         "Argentina": 8,
         "UK": 29}
golds_sum = 0
# END PROBLEM 2 SETUP


# START PROBLEM 2 SOLUTION
# You are encouraged to use a for loop to sum up all the gold medal numbers

for key in golds:
  golds_sum += golds[key]

print(f"golds_sum = {golds_sum}")

# PROBLEM 3
# Working with <countries_golds>, demonstrate your understanding of
# the following concepts and operations:
# 1) working with keys, values of a dictionary
# 2) implementing a for loop
# 3) using dictionary methods such as dictionary.items()
# 4) using list methods such as list.append()


# INSTRUCTIONS:
# The dictionary <countries_golds> consists of <country> - <gold medal number> key-value pairs
# Concatenate <country> - <gold medal number> into a string
# with following format "<country> won <gold medal number> gold medals."
# For example, given "USA": 33, the formatted string should be "USA won 33 gold medals"
# Append each formatted string to the list <countries_golds_list>


# PROBLEM 3 SETUP
countries_golds = {"Italy": 12,
                   "USA": 33,
                   "Brazil": 15,
                   "China": 27,
                   "Spain": 19,
                   "Canada": 22,
                   "Argentina": 8,
                   "UK": 29}
countries_golds_list = []
# END PROBLEM 3 SETUP

countries = countries_golds.keys()
golds = countries_golds.values()

countries_list = []
golds_list = []

for country in countries:
    countries_list.append(country)
    
for gold in golds:
    golds_list.append(gold)

for (a, b) in zip(countries_list, golds_list):
    countries_golds_list.append(f"{a} won {b} gold medals.")

print(countries_golds_list)

#for country in countries_golds:
#  result = '_'.join(f"{country}" + 'won' + {medals} + "gold medals" for country,medals in countries_golds.items())

#countries_golds_list.append(result)

#print(f"countries_golds_list = {countries_golds_list}")
# END PROBLEM 3 SOLUTION

# PROBLEM 4
# Working with <lyrics>, demonstrate your understanding of
# the following concepts and operations:
# 1) working with sequences such as strings and lists
# 2) using string methods such as string.lower(), string.split()
# 3) implementing a for loop
# 4) adding new key-value pairs into dictionary
# 5) updating the value for a specific key in the dictionary


# INSTRUCTIONS:
# The string <lyrics> consists of words separated by " "
# You are given a dictionary called <words_frequency>
# Each key in <words_frequency> is a word in <lyrics> and its associated value is set to 0 initially.
# Please update the value of each key, so it can correctly describe how many times each word(key) appears in the <lyrics>
# e.g. "when" appears twice in <lyrics>, so words_frequency["when"] = 2

# For consistency, all the keys in <words_frequency> should be in lowercase
# (i.e., the frequencies of both "When" and "when" should be aggregated in the dictionary using the key "when")
# Don't worry about KeyErrors, since <words_frequency> includes all the words appear in <lyrics>
# A Python KeyError exception is what is raised when you try to access a key that isn't in a dictionary

# PROBLEM 4 SETUP
lyrics = "When I am down and oh my soul so weary When troubles come my heart burdened be"

words_frequency = {'when': 0,
                   'i': 0,
                   'am': 0,
                   'down': 0,
                   'and': 0,
                   'oh': 0,
                   'my': 0,
                   'soul': 0,
                   'so': 0,
                   'weary': 0,
                   'troubles': 0,
                   'come': 0,
                   'heart': 0,
                   'burdened': 0,
                   'be': 0}

# END PROBLEM 4 SETUP

# START PROBLEM 4 SOLUTION
lyrics = lyrics.lower()

for i in lyrics.split():
    if i in words_frequency:
        words_frequency[i] += 1

print(f"words_frequency = {words_frequency}")
# END PROBLEM 4 SOLUTION

# PROBLEM 5A
# Working with <long_lyrics>, demonstrate your understanding of
# the following concepts and operations:
# 1) working with sequences such as strings and lists
# 2) using string methods such as string.lower(), string.split()
# 3) implementing a nested for loop
# 4) adding new key-value pairs into dictionary
# 5) updating the value for a specific key in the dictionary


# INSTRUCTIONS:
# The string <long_lyrics> consists of words separated by " " and "\n"
# Create a dictionary called <char_frequency> so that each key in <char_frequency> is a character (i.e. "a","b"..."z")
# in <lyrics> and its associated value is how many times that character appears in the <long_lyrics>

# For consistency, all the characters should be in lowercase
# (i.e., the frequencies of both "A" and "a" should be aggregated in the dictionary using the key "a")
# " " and "\n" are NOT valid characters.
# Valid characters are limited to the 26 letters that comprise the English alphabet from "a" to "z"
# Be careful of KeyErrors, since <char_frequency> is an empty dictionary.


# PROBLEM 5A SETUP
long_lyrics = '''
When I am down and oh my soul so weary
When troubles come, and my heart burdened be
Then I am still and wait here in the silence
Until you come and sit awhile with me
You raise me up so I can stand on mountains
You raise me up to walk on stormy seas
I am strong when I am on your shoulders
You raise me up to more than I can be
You raise me up so I can stand on mountains
You raise me up to walk on stormy seas
I am strong when I am on your shoulders
You raise me up to more than I can be
'''
char_frequency = {}
# END PROBLEM 5A SETUP

# START PROBLEM 5A SOLUTION
long_lyrics = long_lyrics.lower()
long_lyrics = long_lyrics.replace(' ','')
long_lyrics = long_lyrics.replace('\n','')
long_lyrics = long_lyrics.replace(',','')

for i in long_lyrics:
    if i not in char_frequency:
        char_frequency[i] = 0
    char_frequency[i] += 1

print(f"char_frequency = {char_frequency}")
#sorted - print(f"char_frequency = {sorted(char_frequency.items())}")
# END PROBLEM 5A SOLUTION

# PROBLEM 5B
# Working with <char_frequency>, demonstrate your understanding of
# the following concepts and operations:
# 1) designing a function that accepts a single argument and returns a value
# 2) working with strings as sequences
# 3) implementing a for loop
# 4) using dictionary methods such as dictionary.items()
# 5) evaluating values using a conditional statement


# INSTRUCTIONS:
# Write a function named <find_most_common_char> that takes one argument: <long_string>,
# (each string consists of words separated by " " and "\n")
# and returns a string, which contains a single character that has the highest frequency count in <long_string>.

# You are encouraged to reuse the code in PROBLEM 5A
# Note: there is only ONE most common character


# For consistency, all the characters should be in lower case
# (i.e., the frequencies of both "I" and "i" should be aggregated in the dictionary using the key "i")
# " " and "\n" are NOT valid characters.
# Valid characters only include 26 alphabets from "a" to "z"

# Sample case
# If <long_lyrics> was passed into <find_most_common_char> as an argument, <find_most_common_char> should return "e"

# Hints:
# In problem 5A, you are asked to create a dictionary that records the word frequencies.
# With a dictionary that records word frequencies, you can find a word with the highest frequency by
# looping through each dictionary entry and compare the value to the highest frequency being seen so far.
#
# Recommended Step 1: Inside the function, create a dictionary with the correct word frequencies (similar to 5A).
# Recommended Step 2: Next, loop through the dictionary to find the word(key) with the highest frequency.
# Recommended Step 3: return the word as the returned value for the function.

# START PROBLEM 5B SOLUTION

def find_most_common_char(long_string):
    highest_char_frequency = {}
    char_list = []
    char_list.extend(list(long_string.strip().lower().replace(' ','').replace('\n','').replace(',','')))
    
    for char in char_list:
      if char not in highest_char_frequency:
        highest_char_frequency[char] = 1
      else:
        highest_char_frequency[char] = highest_char_frequency[char] + 1
    
    max_value = max(highest_char_frequency.values())
    for key, value in highest_char_frequency.items():
      if max_value == value:
        return key

    #ATTEMPT 1
    #for i in long_string.strip().lower().replace(' ','').replace('\n','').replace(',',''):
    #    if i in highest_char_frequency.keys():
    #        highest_char_frequency[i] = highest_char_frequency[i] +1
    
    #max_value = 0
    #for i in highest_char_frequency:
    #     if highest_char_frequency[i] > max_value:
    #            max_key = i
    #            max_value =  highest_char_frequency[i]
    #return max_key

# You can use "long_string_test1", "long_string_test2" to test your function
# Note: passing these two tests doesn't guarantee your function is correct.
# We will use other test cases to verify the correctness of your implementation

long_string_test1 = "away from joy you walk a little missing a tooth discussing famous black dogs on the dead"
# <find_most_common_char> should return "a" if <long_string_test1> was passed into as an argument
long_string_test2 = "smiling grip on what you want would never let me down I know you we say after never having met"
# <find_most_common_char> should return "e" if <long_string_test2> was passed into as an argument

# END PROBLEM 5B SOLUTION
