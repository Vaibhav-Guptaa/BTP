import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Selenium WebDriver
driver = webdriver.Chrome()  # Ensure the Chrome driver is installed and in your PATH
driver.get('https://www.screener.in/company/LICI/consolidated/')

# Wait for the page to load
time.sleep(5)

# Locate the table containing the OPM and EPS data
table = driver.find_element(By.CLASS_NAME, 'data-table.responsive-text-nowrap')

# Get all headers from the table (dates)
headers = table.find_elements(By.TAG_NAME, 'th')
headers = headers[1:]  # Skip the first header if it’s empty
header_text = [header.text for header in headers]

# Print and save headers
print("Dates:", header_text)
rows = table.find_elements(By.XPATH, './/tbody/tr')

# Initialize data dictionaries
opm_data = []
eps_data = []
fii_data = []
dii_data = []

# Extract OPM% row
for row in rows:
    first_cell = row.find_element(By.XPATH, './/td').text
    if "OPM %" in first_cell:
        cells = row.find_elements(By.XPATH, './/td')
        cells = cells[1:]  # Skip the first cell (row label)
        opm_data = [cell.text for cell in cells]
        print("OPM% Row data:", opm_data)
        break

# Extract EPS in Rs row
for row in rows:
    first_cell = row.find_element(By.XPATH, './/td').text.strip()
    if "EPS in Rs" in first_cell:
        cells = row.find_elements(By.XPATH, './/td')
        cells = cells[1:]  # Skip the first cell (row label)
        eps_data = [cell.text for cell in cells]
        print("EPS (Rs) Row Data:", eps_data)
        break

print("=============================================================")

# Locate the second table containing FIIs and DIIs data
table = driver.find_element(By.ID, 'quarterly-shp')
# Get headers (dates) from the second table
headers = table.find_elements(By.TAG_NAME, 'th')
header_text_2 = [header.text for header in headers if header.text]  # Filter empty headers

# Print and save headers (dates)
print("Dates:", header_text_2)

rows = table.find_elements(By.XPATH, './/tbody/tr')

# Extract FIIs row
for row in rows:
    first_cell = row.find_element(By.XPATH, './/td/button').text
    if "FIIs" in first_cell:
        cells = row.find_elements(By.XPATH, './/td')
        cells = cells[1:]  # Skip the first cell (row label)
        fii_data = [cell.text for cell in cells]
        print("FIIs Row Data:", fii_data)
        break

# Extract DIIs row
for row in rows:
    first_cell = row.find_element(By.XPATH, './/td/button').text
    if "DIIs" in first_cell:
        cells = row.find_elements(By.XPATH, './/td')
        cells = cells[1:]  # Skip the first cell (row label)
        dii_data = [cell.text for cell in cells]
        print("DIIs Row Data:", dii_data)
        break

print("=============================================================")

# Quit the driver
driver.quit()

# Write data to CSV
with open('exogenous_variables.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write the headers
    csvwriter.writerow(['Date'] + header_text)
    
    # Write the data rows
    if opm_data:
        csvwriter.writerow(['OPM %'] + opm_data)
    if eps_data:
        csvwriter.writerow(['EPS (Rs)'] + eps_data)
    if fii_data:
        csvwriter.writerow(['FIIs'] + fii_data)
    if dii_data:
        csvwriter.writerow(['DIIs'] + dii_data)

print("Data has been written to exogenous_variables.csv")
