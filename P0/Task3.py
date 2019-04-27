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

def is_from_bangalore(phone_number):
  return phone_number.startswith('(080)')

def get_type_of_number(phone_number):
  if "(" in phone_number:
    return "fixed_line"
  elif " " in phone_number:
    return "mobile"
  elif phone_number.startswith('140'):
    return "telemarketer"
  else: 
    raise Exception("unkown phone type")

def get_area_code(phone_number, t):

  types = {
    'fixed_line': lambda p_number: p_number[1:4],
    'mobile': lambda p_number: p_number[0],
    'telemarketer': lambda p_number: p_number[0:3]
  }

  return types[t](phone_number)

numbers_called = set()
all_calls_from_bangalore = 0
calls_to_fixed_lines = 0
for record in calls:
  if is_from_bangalore(record[0]):
    all_calls_from_bangalore += 1
    type_of_call = get_type_of_number(record[1])
    code = get_area_code(record[1], type_of_call)
    if code == "080":
      calls_to_fixed_lines += 1
    numbers_called.add(code)
numbers = sorted(numbers_called)

print("The numbers called by people in Bangalore have codes:")
print("\n".join(numbers))

percentage=(float(calls_to_fixed_lines) / all_calls_from_bangalore) * 100
print("{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
  percentage
))
