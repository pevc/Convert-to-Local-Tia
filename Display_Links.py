import os
import re
#import Baixar_Videos
from bs4 import BeautifulSoup
import requests
from pytube import YouTube
import requests

def filter_video_without_webm(tag):
    return (
        tag.name == 'video'
        and 'YMEQtf' in tag.get('class', [])
        and not any(source['src'].endswith('.webm') for source in tag.find_all('source'))
    )

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

        drive_links = soup.find_all('a', href=lambda href: href)
        YouTube_links = soup.find_all(filter_video_without_webm)
        
        for link in drive_links:
            
            href = link.get('href')
            if href and ".html" not in href:
                print('Arquivos com link para drive: '+file_name)
                print('Link: '+href+'\n')

        for link in YouTube_links:
            source = link.get('source src')
            print('\nArquivos com link para drive: '+file_name)
            print(link)


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

