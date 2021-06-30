
import re # import regular expressions
from string import punctuation # list of special characters

"""
    DESCRIPTION:

        Write a program to find the percentage of uppercase letters, lowercase letters, digits and other special characters(including space) in the given string.

"""

text = str(input("Please, give the text:"))

#text = "FDAjfiodioqe oqieurjkl#$!$oiqui dakljf 98eu1ereA" # given string
size = len(text) # size of given string
print("GIVEN STRING: "+text)

upper_case = re.findall('[A-Z]', text) # extract all the uppercase letters from a given string
lower_case = re.findall('[a-z]',text)  # extract all the lowercase letters from a given string
digits = re.findall('[0-9]',text)      # extract digits from a given string
print("\nLower-case: "+str(lower_case))
print("Upper-case: "+str(upper_case))
print("Digits:     "+str(digits))

# Add space into special characters
specialCh_list = list(punctuation)
specialCh_list.append(' ')

# search for special characters in a given string
special = []
for word in text:
    for char in word:
        if char in specialCh_list:
            special.append(char)

print("Special:    "+str(special))

print("Lower-case percentage:         "+str(len(lower_case)/size*100))
print("Upper-case percentage:         "+str(len(upper_case)/size*100))
print("Digits percentage:             "+str(len(digits)/size*100))
print("Special Characters percentage: "+str(len(special)/size*100))
