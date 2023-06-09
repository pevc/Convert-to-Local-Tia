import os
import re
import Baixar_Videos
from bs4 import BeautifulSoup

i = 0
point_local = "pointlocal\pointlocal.html"

# a ideia é modificar o pointlocal original toda vez que o ciclo rodar, a criação dos arquivos foi para teste
def convert_point_local(file_tag):
    palavra = ".mp4"
    posicao = file_tag.find(palavra)
    padrao = r'(?<=<span class="pB4Yfc">)(.*\.mp4)(?=<\/span>)'
    match = re.search(padrao, file_tag)

    if match:
        nome_video = match.group(1)

    
    with open(point_local, 'r') as file:
        point_local_data = file.read()
    
    # Usando expressão regular para substituir todos os nomes de vídeo com extensão .mp4 no arquivo
    padrao = r'(?<=<source src="Videos_Local\\).*?\.mp4(?=" type="video/mp4">)'
    novo_arquivo = re.sub(padrao, nome_video, point_local_data, count=0)

    # Salvar arquivo modificado como .html
    nome_arquivo = point_local
    with open(point_local, 'w') as file:
        file.write(novo_arquivo)

    #print(point_local_data)

    #print(f"Arquivo '{nome_arquivo}' salvo com sucesso na pasta '{pasta}'.")    
    
     

def convert_drive_videos(tag_video) :
    tag_video_str = str(tag_video)
    if tag_video_str != "[]" and "drive" in tag_video_str :
            #print(file_name)
            convert_point_local(tag_video_str)

            with open(point_local, 'r') as file:
                point_local_data = file.read()

            #print(point_local_data)

            #print(tag_video.prettify())
            #tag_video.div.parent.replace_with(str(point_local_data))
            tag_video.div.parent.replace_with(BeautifulSoup(point_local_data, "html.parser").div)
            
            #print(tag_video.prettify())
            # Salve o HTML modificado de volta no arquivo
            #with open(file_path, 'w') as file:
               #file.write(soup.prettify())

def convert_youtube_videos(tag_video) :
    tag_video_str = str(tag_video)
    if tag_video_str != "[]" and "youtube" in tag_video_str:
        print()

folder_path = "DRAFT"     
# Procurando todos os diretorios
for file_name in os.listdir(folder_path):
    # Procurando os arquivos HTML
    if file_name.endswith('.html'):
        # Achando os endereços dos arquivos HTML
        file_path = os.path.join(folder_path, file_name)

        # Abrir o arquivo HTML para leitura
        with open(file_path, 'r') as file:
            file_data = file.read()
        
        soup = BeautifulSoup(file_data, "html.parser")

        # tag_video para drive
        tag_videos = soup.find_all('div',class_ = "WIdY2d M1aSXe")

        for tag_video in tag_videos :
            print("\n\n")
            print(file_name)
            print("\n\n\n\n\n\n")
            print(tag_video.prettify())
            #convert_drive_videos(tag_video)
            #convert_youtube_videos(tag_video)

        

            #print(point_local_data)
            # new_tag = soup.new_tag("b")
            # new_tag.string = "example.com"
            # print(type(new_tag))
            # print(type(tag_video)