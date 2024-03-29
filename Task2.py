"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def task2(calls):
    longest_call = {'time': '', 'number': ''}

    for call in calls:
        if longest_call['time'] < call[3]:
            longest_call['time'] = call[3]
            longest_call['number'] = call[0]

    print'{0} spent the longest time, {1} seconds, on the phone during September 2016'.format(longest_call.get('number'), longest_call.get('time'))

task2(calls)

