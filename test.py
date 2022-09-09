# Python3 code to demonstrate working of
# Detect date in String
# Using python-dateutil()
from dateutil import parser
import datefinder

# initializing string

# printing original string
print("The original string is : " + str(test_str))

matches = datefinder.find_dates(test_str)

for match in matches:
    print(match)

