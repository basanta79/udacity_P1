"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def task4(calls):
    area_mobile_codes = {}
    area_marketing_codes = {}
    area_fixed_codes = {}
    total_calls = 0
    total_calls_to_bangalore = 0

    for call in calls:
        total_calls +=1
        if '(080)' in call[0]:
            if call[1].find('(', 0, 1) >= 0:
                start=call[1].find('(') + 1
                end=call[1].find(')')
                code = call[1][start:end]
                occurrences = area_mobile_codes.get(code) or 0
                area_mobile_codes[code] = occurrences + 1
            elif call[1].find('140', 0, 3) >= 0:
                occurrences = area_marketing_codes.get('140') or 0
                area_marketing_codes['140'] = occurrences + 1
            else:
                area_code = call[1].split()
                occurrences = area_fixed_codes.get(area_code[0]) or 0
                area_fixed_codes[area_code[0]] = occurrences + 1

    total_calls_to_bangalore = area_mobile_codes['080']
    percentage = round((float(total_calls_to_bangalore)/float(total_calls))*100, 2)
    mobile_codes = printTuple(tuple(area_mobile_codes), True)
    marketing_codes = printTuple(tuple(area_marketing_codes), False)
    fixed_codes = printTuple(tuple(area_fixed_codes), False)
    print("The numbers called by people in Bangalore have codes:" + mobile_codes + marketing_codes + fixed_codes )
    print('{0} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.').format(percentage)

def printTuple(tuple_to_print, with_brackets):
    string_result = ''
    for element in tuple_to_print:
        if with_brackets:
            string_result = string_result + '\n' + '(' + str(element) + ')'
        else:
            string_result = string_result + '\n' + str(element)
    return string_result


task4(calls)