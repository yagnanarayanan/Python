# program to find email ids from a text file and display as a list
import re
fp = open("office_data.txt")
text = fp.read()
email_pattern = re.compile(r'([A-Z]|[a-z]|[0-9]|[_])+.([A-Z]|[a-z]|[0-9]|[_])+@([A-Z]|[a-z]|[0-9])+.com')
matches = email_pattern.finditer(text)
emails = []
for match in matches:
    emails.append(match.group())
print(emails)
fp.close()
