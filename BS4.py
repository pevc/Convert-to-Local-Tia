import os
import re
#import Baixar_Videos
from bs4 import BeautifulSoup
import requests
from pytube import YouTube
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
    
    #nome_video = nome_video.replace("mp4","webm")
    print(nome_video)
    
    with open(point_local, 'r') as file:
        point_local_data = file.read()
    
    nome_arquivo = point_local
    # Usando expressão regular para substituir todos os nomes de vídeo com extensão .mp4 no arquivo
    padrao = r'(?<=<source src="Videos_Local\\).*?\.mp4(?=" type="video/mp4">)'
    novo_arquivo = re.sub(padrao, nome_video, point_local_data, count=0)

    # Salvar arquivo modificado como .html
    with open(point_local, 'w') as file:
        file.write(novo_arquivo)   
    
def convert_point_local_youtube(video_downloaded) :
    with open(point_local, 'r') as file:
        point_local_data = file.read()

    print('Youtube download: '+video_downloaded)
    padrao = r'(?<=<source src="Videos_Local\\).*?\.mp4(?=" type="video/mp4">)'
    novo_arquivo = re.sub(padrao, video_downloaded, point_local_data, count=0)

    # Salvar arquivo modificado como .html
    nome_arquivo = point_local
    with open(point_local, 'w') as file:
        file.write(novo_arquivo)

def convert_drive_videos(tag_video,file_path) :

    soup = BeautifulSoup(file_data, "html.parser")

    tag_video_str = str(tag_video)
    
    #print(file_name)
    #print(tag_video.prettify())
    convert_point_local(tag_video_str)

    with open(point_local, 'r') as file:
        point_local_data = file.read()

    print("Drive: "+point_local_data)

    #print(tag_video.prettify())
    #tag_video.div.parent.replace_with(str(point_local_data))
    tag_video.div.parent.replace_with(BeautifulSoup(point_local_data, "html.parser").div)


    # Salve o HTML modificado de volta no arquivo
    with open(file_path, 'w') as file:
        file.write(soup.pretiffy())

pasta_destino = "DRAFT/Videos_Local"
def download_youtube_video_from_tag(tag_string, pasta_destino):
    # Encontra o link do YouTube na tag usando expressões regulares
    match = re.search(r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]+)', tag_string)
    if not match:
        print("Nenhum link do YouTube encontrado na tag.")
        return

    youtube_id = match.group(1)
    youtube_url = f"https://www.youtube.com/watch?v={youtube_id}"

    try:
        # Obtém informações do vídeo, incluindo o título
        video = YouTube(youtube_url)
        titulo = video.title

        # Verifica se a pasta de destino existe, caso contrário, cria-a
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        # Define o caminho completo para o arquivo de destino
        caminho_arquivo = os.path.join(pasta_destino, f"{titulo}.mp4")

        # Faz o download do vídeo usando a URL do YouTube
        video.streams.get_highest_resolution().download(output_path=pasta_destino, filename=f"{titulo}.mp4")
        #print("Download concluído.")
        if titulo != None :
            return f"{titulo}.mp4"

    except Exception as e:
        print("Erro ao fazer o download do vídeo:", str(e))


def convert_youtube_videos(tag_video,file_name) :
    tag_string = str(tag_video)
    #print(file_name)
    video_downloaded = download_youtube_video_from_tag(tag_string, pasta_destino)
    return video_downloaded


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
            tag_video_str = str(tag_video)
            if tag_video_str != "[]" and "drive" in tag_video_str :
                print("Video Drive a ser baixado: "+file_name)
                convert_point_local(tag_video_str)
                with open(point_local, 'r') as file:
                    point_local_data = file.read()
                # Modifica o div da tag pelo div do pointlocal
                tag_video.div.parent.replace_with(BeautifulSoup(point_local_data, "html.parser").div)
                # Salva o HTML modificado de volta no arquivo
                with open(file_path, 'w') as file:
                    file.write(soup.prettify())
            if tag_video_str != "[]" and "youtube" in tag_video_str :
                print("Video youtube a ser baixado: "+file_name)
                video_downloaded = convert_youtube_videos(tag_video,file_name)

                if video_downloaded != None :
                    convert_point_local_youtube(video_downloaded)
                    with open(point_local, 'r') as file:
                        point_local_data = file.read()

                    tag_video.div.parent.replace_with(BeautifulSoup(point_local_data, "html.parser").div)
                    #print(file_name)
                    with open(file_path, 'w') as file:
                        file.write(soup.prettify())    
