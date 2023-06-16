import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage you want to scrape
url = "https://www.redbus.in/"  # Replace with the URL of the webpage you want to scrape
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extract information from the webpage
# Here's an example of extracting all the links on the page
links = soup.find_all("a")

# Print the extracted links
for link in links:
    href = link.get("href")
    print(href)

# You can also extract other information such as text, images, tables, etc.
# Refer to the BeautifulSoup documentation for more details on the available methods and techniques.

