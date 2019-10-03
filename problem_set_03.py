love_quotes = [
    "Love is not love which alters when it alteration finds", #quote
        #quote_line = quote.split(' ')
        #    Love, is, not, love, ...
        #    quote_line[0]
    "Love, the itch, and a cough cannot be hid", #quote
    "That love is all there is, Is all we know of love",
    "I am two fools, I know, for loving, and saying so",
    "Love lives on propinquity, but dies on contact",
    "You really have to love yourself to get anything done in this world",
    "The irony of love is that it guarantees some degree of anger, fear and criticism",
    "I see you everywhere, in the stars, in the river",
    "Respect is love in plain clothes",
    "If you want to be loved, be lovable",
]

authors = [
    "William Shakespeare",
    "Thomas Fuller",
    "Emily Dickinson",
    "John Donne",
    "Thomas Hardy",
    "Lucille Ball",
    "Harold H. Bloomfield",
    "Virginia Woolf",
    "Frankie Byrne",
    "Ovid",
]

# PROBLEM 1
# Extract the indices of all the quotes which begin with "Love" into a new list named love_quotes_indices. Print love_quotes_indices.
# Note: You're not allowed to change the original quotes.
# Hint: Use for loop, if statement and string slicing.

love_quotes_indices = []

# Get the size of the array for love_quotes (which is 10) and iterate through the array of love_quotes.
for index in range(len(love_quotes)):
    # if the current item (a quote in the love_quotes array) starts with the word "Love"...
    if love_quotes[index].startswith("Love"):
        # then store the index of the item in love_quotes_indices.
        love_quotes_indices.append(index)

#Returns quotes that start with "Love"
#for quote in love_quotes:
#    quote_line = quote.split(' ');
#    if quote_line[0] == "Love":
#        love_quotes_indices.append(quote)
#    else:
#        continue

# print the indices. this is actually the ask in Problem 1. They do not want you to print the quotes themselves, 
# but where in the array quotes that start with "Love" exist.
print(love_quotes_indices)

# PROBLEM 2
# Create quote-author pairs by concatenating the quotes indicated in love_quote_indices with the the corresponding author in authors.
# Concatenate the values using the format "<quote> - <author>" (the <text> are placeholders that your code should replace).
# Save these strings into the list quotes_with_author. Print quotes_with_author.

# start with an empty array to store the results
quotes_with_author = []

# use the array from problem 1
love_quotes_indices = [0,1,4]

# iterate through love_quote_indices from problem 1
for index_match in love_quotes_indices:
    # print the quote itself
    print(love_quotes[index_match])
    # print the author of the quote
    print(authors[index_match])

    # add to the empty array the quote, author pair
    # quotes_with_author = ["Love is not love which alters when it alteration finds - William Shakespeare",
    # "Love, the itch, and a cough cannot be hid - Thomas Fuller",
    # "Love lives on propinquity, but dies on contact - Thomas Hardy"]
    result = "{0} - {1}".format(love_quotes[index_match], authors[index_match])
    quotes_with_author.append(result)

print(quotes_with_author)

# PROBLEM 3
# Write a function named who_wrote_it which will return the author of a quote when given the combined string "<quote> - <author>".
# Apply the function to quotes_with_author and store the result in the list i_wrote_it.
# Sort the list i_wrote_it based on alphabetic order. Print i_wrote_it.
# BEGIN PROBLEM 3 SOLUTION

i_wrote_it = []

# this function builds on the previous problem
# take the quotes_with_author that was added to in the previous problem
# split on the space-dash-space and return the second item which is the author
# "Love is not love which alters when it alteration finds - William Shakespeare"
# split on " - " will give you an array ["Love is not love which alters when it alteration finds", "William Shakespeare"
# Getting index 1 will give you "William Shakespeare" because arrays start with index 0
def who_wrote_it(quotes_with_author):
    quote = quotes_with_author.split(" - ")
    return quote[1]

# Use the above function which returns the author to the i_wrote_it array
for quote in quotes_with_author:
    i_wrote_it.append(who_wrote_it(quote))

# Sort the array alphabetically
i_wrote_it.sort()
print(i_wrote_it)

# PROBLEM 4
# Write a function named count_words_in_quote which will return the number of words in a given quote.
# Apply the function to the quotes indexed by the first and the last elements in love_quotes_indices.
# Assign the word count values to the variables first_word_count and last_word_count as appropriate.
# Print first_word_count and last_word_count.
# Note: Words in quotes are not only separated by blanks, but also by comma.
# Hint: Use split(), if-else statement, len() or sum().

# Take one quote as an example to help you visualize the problem
# quote = "Love, the itch, and a cough cannot be hid"
# I think the below is incorrect because you should be splitting on the space quote.split(" ")
# If you look at all of the quotes given, there is a space after the comma so the note in the instructions shouldn't matter
# Split on the space and then call the len() function to get the count of words and return that
def count_words_in_quote(quote):
    return len(quote.split())

# Perform the function on the first quote that starts with Love
first_word_count = count_words_in_quote(love_quotes[love_quotes_indices[0]])
# Perform the function on the last quote that starts with Love
last_word_count = count_words_in_quote(love_quotes[love_quotes_indices[-1]])

print(first_word_count, last_word_count)

# PROBLEM 5
# Love quotes don't necessarily use "love"!
# Write a function named is_quote_with_love, which will determine whether the given quote contains the words
# "love", "loving", "loved", "lovable", "Love" or not.
# If the quote contains one of the words the function should return True otherwise return False.
# Use a while loop and is_quote_with_love to identify all quotes without "love", "loving", "loved", "lovable", "Love"
# Once identified append the quote to the no_love_quotes list.
# Print no_love_quotes
# Hint: You can search on the characters 'lov' if you use a built-in string function to convert quote to lower case.

no_love_quotes = []
def is_quote_with_love(quote):
   # put everything in lowercase so that it is easier to match the string
   quote = quote.lower()
   # because all of the words you are looking for start with "lov", all you need to do is match on that first part
   if "lov" in quote:
       # if it matches, return true
       return True
   else: # else return false
        return False

i=0
# iterate through the love_quotes array
# if i is less than the number of quotes in love_quotes, then enter the while loop
while i < len(love_quotes):
    # if the quote does not contain "lov", then add it to the no_love_quotes array
    if is_quote_with_love(love_quotes[i]) == False:
        no_love_quotes.append(love_quotes[i])
    # increment i so that you don't go into an infinite loop
    i += 1

print(no_love_quotes)

# PROBLEM 6
# Finally, put all you've learned together.
# Reuse functions created above to sum up the word counts of quotes which contain "love", "loving", "loved", "lovable"
# or "Love" in love_quotes.
# Assign the total word count to the variable total_word_count.
# Print total_word_count.

total_word_count = 0
# for each quote in love_quotes
for word_count in love_quotes:
    # if the quote contains the word "lov", add to total_word_count
    if is_quote_with_love(word_count) == True:
        total_word_count += count_words_in_quote(word_count)
# print the number of times "lov" appears in the entire love_quotes array
print(total_word_count)
