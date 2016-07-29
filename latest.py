#!/usr/bin/env python3
import re
import json
import sys
import requests
from bs4 import BeautifulSoup

page = requests.get('https://aws.amazon.com/amazon-linux-ami/')
soup = BeautifulSoup(page.text, 'html.parser')

# Get description
description = soup.find(string=re.compile('was released on'))
print(description, file=sys.stderr)

# Parse AMI table
table = soup.find('div', class_='aws-table')
table_body = table.find('tbody')
rows = table_body.find_all('tr')

# Header row
headings = rows[0].find_all('th')
# Strip Region heading
headings = headings[1:]
# Strip whitespace
headings = [element.text.strip() for element in headings]

data = {}
# rows[0] was headings
for row in rows[1:]:
    columns = row.find_all('td')
    columns = [element.text.strip() for element in columns]

    region_data = {}
    # columns[0] is region name
    for i in range(len(columns[1:])):
        region_data[headings[i]] = columns[i+1]
    data[columns[0]] = region_data

print(json.dumps(data, indent=4))
