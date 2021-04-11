# regular expressions use raw strings
import re

a = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Phone1: +91-1023456789
Phone1: +91 1023456789
Phone1: +911023456789
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
ai aii aiii
Website: www.north america.tata.com
Directions: View map '''
# pattern = re.compile(r'north')
# pattern = re.compile(r'.')
# pattern = re.compile(r'.com')
# pattern = re.compile(r'^Tata')
# pattern = re.compile(r'$Tata')
# pattern = re.compile(r'map $')
# pattern = re.compile(r'ai*')
# pattern = re.compile(r'ai+')
# pattern = re.compile(r'ai{2}')
# pattern = re.compile(r'(ai){1}')
# # pattern = re.compile(r'(ai){1}|Fax')
# pattern = re.compile(r'\bFax')
# pattern = re.compile(r'Fax\b')
pattern = re.compile(r'\d{5}-\d{4}')
matches = pattern.finditer(a)
for match in matches:
    print(match)
