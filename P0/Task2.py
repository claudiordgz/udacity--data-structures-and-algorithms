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
from collections import defaultdict

def get_month_and_year(date_str):
  date, _ = date_str.split(' ')
  __, month, year = date.split('-')
  return month, year

def record_generator(records):
  for record in records:
    month, year = get_month_and_year(record[2])
    # Check is unnecessary because all records are from Sep 2016
    if month == "09" and year == "2016":
      yield record

def get_longest_caller_number(calls):
  tracker = defaultdict(int)
  longest_call = -1
  longest_call_number = None
  for record in calls:
    call_time = int(record[3])
    tracker[record[0]] += call_time
    tracker[record[1]] += call_time
    if tracker[record[0]] > longest_call:
      longest_call = tracker[record[0]]
      longest_call_number = record[0]
    if tracker[record[1]] > longest_call:
      longest_call = tracker[record[1]]
      longest_call_number = record[1]
  return (longest_call_number, tracker[longest_call_number])

longest_call = get_longest_caller_number(calls)
print("{telephone_number} spent the longest time, {total_time} seconds, on the phone during September 2016.".format(
  telephone_number=longest_call[0],
  total_time=longest_call[1]
))
