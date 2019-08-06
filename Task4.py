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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def task5(texts, calls):
    telemarketers_list = {}
    receiving_calls = {}
    texting_list = {}
    receiving_text = {}

    for record in calls:
        telemarketers_list[record[0]] = 1

    for record in calls:
        numbers_removed = 0
        numbers_removed += telemarketers_list.pop(record[1], 0)

    for record in texts:
        numbers_removed = 0
        numbers_removed += telemarketers_list.pop(record[0], 0)
        numbers_removed += telemarketers_list.pop(record[1], 0)

    telemarketers_list_tuple = tuple(telemarketers_list)

    print('These numbers could be telemarketers: {0}'.format(printTuple(telemarketers_list_tuple, False)))

def printTuple(tuple_to_print, with_brackets):
    string_result = ''
    for element in tuple_to_print:
        if with_brackets:
            string_result = string_result + '\n' + '(' + str(element) + ')'
        else:
            string_result = string_result + '\n' + str(element)
    return string_result


task5(texts, calls)