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
import itertools

phone_directory = set()
for record in itertools.chain(texts, calls):
  phone_directory.add(record[0])
  phone_directory.add(record[1])

print("There are {count} different telephone numbers in the records.".format(count=len(phone_directory)))

