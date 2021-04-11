# program to find indian numbers from a text file and display as a list
import re
fp = open("office_data.txt")
text = fp.read()
pattern = re.compile(r'\+91-\d{10}|\+91\d{10}|\+91 \d{10}')
matches = pattern.finditer(text)
indian_numbers = []
for match in matches:
    indian_numbers.append(match.group())
print(indian_numbers)
fp.close()
