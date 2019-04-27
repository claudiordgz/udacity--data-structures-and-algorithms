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

makes_calls = set()
receives_calls_sends_texts_receives_texts = set()
for record in calls:
  makes_calls.add(record[0])
  receives_calls_sends_texts_receives_texts.add(record[1])
for record in texts:
  receives_calls_sends_texts_receives_texts.add(record[0])
  receives_calls_sends_texts_receives_texts.add(record[1])

print("These numbers could be telemarketers: ")
possible_telemarketers = sorted(makes_calls.difference(receives_calls_sends_texts_receives_texts))
print("\n".join(possible_telemarketers))
