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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def task0(text, calls):
    print 'first record of texts, {0} texts {1} at time {2}'.format(text[0][0], text[0][1], text[0][2])
    print 'Last record of calls, {0} text {1} at time {2}, lasting {3} seconds'.format(calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][3])


task0(texts, calls)
