import os
import re
import requests

def download_video(url, output_dir):
    filename = url.split('/')[-1]
    output_path = os.path.join(output_dir, filename)

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(output_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    return output_path

def convert_videos_to_local(html_file, output_dir):
    with open(html_file, 'r') as file:
        html_code = file.read()

    # Encontre todas as ocorrências de <video> com atributo "src" remoto
    video_tags = re.findall(r'<video.*?src="(.*?)".*?>', html_code)
    replaced_videos = []

    for video_src in video_tags:
        # Baixe o vídeo remoto
        local_video_path = download_video(video_src, output_dir)

        # Substitua o atributo "src" remoto pelo caminho local do vídeo baixado
        html_code = html_code.replace(video_src, local_video_path)

        # Armazene os vídeos substituídos e seus respectivos URLs originais
        replaced_videos.append((local_video_path, video_src))

    # Escreva o novo código HTML em um novo arquivo
    new_html_file = 'converted.html'
    with open(new_html_file, 'w') as file:
        file.write(html_code)

    return new_html_file, replaced_videos

# Insira o caminho do arquivo HTML original
original_html_file = '21 Denavit-Hartenbergs Notation.html'
# Insira o diretório de saída para os vídeos baixados
output_directory = 'Export_and_Convert'

# Converta os vídeos remotos para vídeos locais e obtenha os vídeos substituídos
new_html_file, replaced_videos = convert_videos_to_local(original_html_file, output_directory)

print(f'Arquivo HTML convertido gerado: {new_html_file}')

# Exiba os vídeos substituídos e seus respectivos URLs originais
print('Vídeos substituídos:')
for local_video_path, video_src in replaced_videos:
    print(f'{local_video_path} foi substituído por {video_src}')