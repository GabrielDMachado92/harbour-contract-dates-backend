# Python3 code to demonstrate working of
# Detect date in String
# Using python-dateutil()
from dateutil import parser
import datefinder
import textract


pdfData = textract.process("/Users/gabrielmachado/Documents/Development/harbour-contract-dates-backend/contracts/ada_1pg.pdf" , encoding='utf-8', method='pdfminer')



matches = datefinder.find_dates(str(pdfData), strict=True)



for match in matches:
    print(match)