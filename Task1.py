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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def task1(texts, calls):
    telephone_number_list = {}

    for record in texts:
        if record[0] in telephone_number_list:
            telephone_number_list[record[0]] = telephone_number_list.get(record[0]) + 1
        else:
            telephone_number_list[record[0]] = 1

        if record[1] in telephone_number_list:
            telephone_number_list[record[1]] = telephone_number_list.get(record[1]) + 1
        else:
            telephone_number_list[record[1]] = 1

    for record in calls:
        if record[0] in telephone_number_list:
            telephone_number_list[record[0]] = telephone_number_list.get(record[0]) + 1
        else:
            telephone_number_list[record[0]] = 1

        if record[1] in telephone_number_list:
            telephone_number_list[record[1]] = telephone_number_list.get(record[1]) + 1
        else:
            telephone_number_list[record[1]] = 1

    print 'There are {0} different telephone numbers in the records.'.format(len(telephone_number_list))

task1(texts, calls)