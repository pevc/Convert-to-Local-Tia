import os
import re
#import Baixar_Videos
from bs4 import BeautifulSoup
import requests
from pytube import YouTube
import requests

pasta_destino_driver = "DRAFT/Driver_Local"
def download_url(url, save_path, chunk_size=128):
    print("url = "+url)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    response = requests.get(url)
    # Extract the file ID using regular expressions
    match = re.search(r"/d/([^/]+)/", url)
    if match:
        match_string = match.group(1)
        print("Match: " + match_string)
    else:
        print("No match found.")
    if response.status_code == 200:
        print(response.content)
        with open('C:\\Users\\Pedro Vilela\\Downloads\\ZProfissional\\GitHub\\Convert-to-Local-Tia\\DRAFT\\Driver_Local\\'+match_string+'.pdf', "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {match_string}")
    else:
        print(f"Failed to download: {match_string}")
        
folder_path = "DRAFT"     
# Procurando todos os diretorios
for file_name in os.listdir(folder_path):
    # Procurando os arquivos HTML
    if file_name.endswith('.html'):
        # Achando os endereços dos arquivos HTML
        file_path = os.path.join(folder_path, file_name)

        # Abrir o arquivo HTML para leitura
        with open(file_path, 'r',encoding='utf-8') as file:
            #print(file_path)
            file_data = file.read()
        
        soup = BeautifulSoup(file_data, "html.parser")

        #drive_links = soup.find_all('a', href=lambda href: href and 'drive.google.com' in href)
        drive_links = soup.find_all('a', href=lambda href: href)
        
        
        for link in drive_links:
            
            href = link.get('href')
            if href and ".html" not in href:
                print('Arquivos com link para drive: '+file_name)
                print('Link: '+href+'\n')
            
'''            if 'id=' in href:
                # Extract the file ID from the href
                file_id = href[href.index('id=')+3:]
                
                # Construct the download URL
                pdf_url = f"https://drive.google.com/uc?id={file_id}"
                print("Pdf ulr: "+pdf_url)
                # Set the destination file path
                destination = os.path.join('pdfs', f'{file_id}.pdf')
                print(destination)
            else:
                download_url(href,pasta_destino_driver)
            # Download the PDF
            #download_pdf(pdf_url, destination)'''

