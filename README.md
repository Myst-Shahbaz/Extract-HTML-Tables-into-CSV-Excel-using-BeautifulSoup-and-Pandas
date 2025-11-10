🕸️ Web Scraping Project – Extracting HTML Tables into CSV/Excel
📘 Overview

This project demonstrates how to extract structured table data from a webpage using Python, BeautifulSoup, and pandas, then export it into clean, analysis-ready CSV and Excel files.

The script scrapes data from webscraper.io’s test site
, which is designed for practicing web scraping safely.

🚀 Features

✨ Fetches webpage content using the requests library
🧩 Parses HTML using BeautifulSoup (bs4)
📊 Extracts multiple HTML tables dynamically
🧹 Cleans and structures the table data into pandas DataFrames
🧷 Combines multiple tables into one dataset
💾 Exports results into CSV and Excel formats
🧮 Uses ignore_index=True for clean continuous indexing

🧠 Technologies Used
🧰 Library	🪄 Purpose
requests	To fetch webpage HTML
BeautifulSoup (bs4)	To parse and navigate HTML structure
pandas	To organize, clean, and export data
⚙️ How It Works

1️⃣ Send a GET request to the target webpage
2️⃣ Parse the HTML using BeautifulSoup
3️⃣ Locate all <table> elements by class or tag name
4️⃣ Extract headers (<th>) and data cells (<td>)
5️⃣ Store data from each table into separate lists
6️⃣ Convert the lists into pandas DataFrames
7️⃣ Combine both DataFrames using pd.concat(ignore_index=True)
8️⃣ Save the final DataFrame to:
📄 Website_data.csv
📘 Website_data.xlsx

📂 Output Files

📄 Website_data.csv
📘 Website_data.xlsx

Both files contain the cleaned and merged table data.
