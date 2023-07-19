import os
from bs4 import BeautifulSoup
import requests

# Function to download PDF from a given URL
def download_pdf(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {destination}")

# Function to parse HTML file, find driver links, and download PDFs
def parse_html_file(file_path):
    with open(file_path, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all 'a' tags with href containing 'drive.google.com'
    drive_links = soup.find_all('a', href=lambda href: href and 'drive.google.com' in href)

    for link in drive_links:
        href = link.get('href')
        if 'id=' in href:
            # Extract the file ID from the href
            file_id = href[href.index('id=')+3:]

            # Construct the PDF download URL
            pdf_url = f"https://drive.google.com/uc?id={file_id}"

            # Set the destination file path
            destination = os.path.join('pdfs', f'{file_id}.pdf')

            # Download the PDF
            download_pdf(pdf_url, destination)

# Folder containing HTML files
folder_path = 'html_files'

# Create a directory to store downloaded PDFs
pdfs_dir = 'pdfs'
os.makedirs(pdfs_dir, exist_ok=True)

# Iterate through all HTML files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.html'):
        file_path = os.path.join(folder_path, filename)
        parse_html_file(file_path)