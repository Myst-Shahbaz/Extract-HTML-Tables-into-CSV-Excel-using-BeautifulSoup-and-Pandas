# -------------------------------------------------------------
# 🕸️ Web Scraping Project – Extracting HTML Tables into CSV/Excel
# Author: Muhammad Shahbaz
# Description:
#   This script scrapes two HTML tables from a web page using
#   BeautifulSoup and exports them into CSV and Excel files.
# -------------------------------------------------------------

import requests               # To send HTTP requests and get web page content
from bs4 import BeautifulSoup # To parse and navigate through HTML
import pandas as pd           # To create, combine, and export tabular data

# -------------------------------------------------------------
# Step 1: Send a request to the website
# -------------------------------------------------------------
url = 'https://webscraper.io/test-sites/tables/tables-semantically-correct'

# Send a GET request to fetch the page's HTML content
res = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')

# -------------------------------------------------------------
# Step 2: Find all tables in the webpage
# -------------------------------------------------------------
# The site contains two HTML tables, so we grab all <table> tags
tables = soup.find_all('table')

# -------------------------------------------------------------
# Step 3: Extract data from each table and store it in a list
# -------------------------------------------------------------
dfs = []  # This list will hold a DataFrame for each table

# Loop through each table found on the page
for table in tables:

    # Extract column headers (inside <th> tags)
    headers = [th.text.strip() for th in table.find_all('th')]

    # Initialize an empty list to store all rows for this table
    rows = []

    # Loop through each table row, skipping the first header row
    for tr in table.find_all('tr')[1:]:
        # Extract both <td> (data cells) and <th> (some tables may use <th> for row headers)
        cells = tr.find_all(['td', 'th'])
        # Clean each cell's text (remove spaces/newlines)
        row = [cell.text.strip() for cell in cells]
        # Add this row to the list
        rows.append(row)

    # Convert this table’s data into a pandas DataFrame
    df = pd.DataFrame(rows, columns=headers)
    # Add the DataFrame to the list of tables
    dfs.append(df)

# -------------------------------------------------------------
# Step 4: Combine both tables into a single DataFrame
# -------------------------------------------------------------
# ignore_index=True ensures the new combined DataFrame
# has continuous row numbers (0,1,2,3,...) without duplicates
final_df = pd.concat(dfs, ignore_index=True)

# -------------------------------------------------------------
# Step 5: Export the combined data to CSV and Excel
# -------------------------------------------------------------
# Export as CSV file
final_df.to_csv('Website_data.csv', index=False)

# Export as Excel file
final_df.to_excel('Website_data.xlsx', index=False)

# -------------------------------------------------------------
# Step 6: Confirmation message
# -------------------------------------------------------------
print("✅ Data extracted and saved successfully to 'Website_data.csv' and 'Website_data.xlsx'")
