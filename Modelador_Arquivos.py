import os
from bs4 import BeautifulSoup

def adicionar_texto_arquivo(nome_arquivo_destino, linha_numero, nome_arquivo_origem):
    with open(nome_arquivo_origem, 'r') as arquivo_origem:
        texto = arquivo_origem.read()

    with open(nome_arquivo_destino, 'r') as arquivo_destino:
        linhas = arquivo_destino.readlines()

    # Verifica se o número da linha é válido
    if linha_numero < 1 or linha_numero > len(linhas):
        print("Número de linha inválido.")
        return

    linhas[linha_numero - 1] = linhas[linha_numero - 1].rstrip('\n') + texto + '\n'

    with open(nome_arquivo_destino, 'w') as arquivo_destino:
        arquivo_destino.writelines(linhas)

    print("Texto adicionado à linha especificada com sucesso.")

def deletar_faixa_linhas_arquivo(nome_arquivo, linha_inicial, linha_final):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    # Verifica se os números das linhas são válidos
    if linha_inicial < 1 or linha_final > len(linhas) or linha_inicial > linha_final:
        print("Faixa de linhas inválida.")
        return

    del linhas[linha_inicial - 1:linha_final]

    with open(nome_arquivo, 'w') as arquivo:
        arquivo.writelines(linhas)

    print("Faixa de linhas deletada com sucesso.")

def modificar_linha_arquivo(nome_arquivo, linha_numero, novo_conteudo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    # Verifica se o número da linha é válido
    if linha_numero < 1 or linha_numero > len(linhas):
        print("Número de linha inválido.")
        return

    linhas[linha_numero - 1] = novo_conteudo + '\n'

    with open(nome_arquivo, 'w') as arquivo:
        arquivo.writelines(linhas)

    print("Linha modificada com sucesso.")


def encontrar_palavra(texto, palavra):
    indice = texto.find(palavra)
    if indice != -1:
        return True
    else :
        return False


def procurar_string_em_html(html_content, target_string):
    soup = BeautifulSoup(html_content, 'html.parser')
    resultado = []

    for tag in soup.find_all():
        if tag.get_text().find(target_string) != -1:
            resultado.append(str(tag))

    return resultado


folder_path = 'DRAFT'

i = 0
html_videos_list = []
# Percorrer todos os arquivos na pasta
for file_name in os.listdir(folder_path):
    if file_name.endswith('.html'):
        file_path = os.path.join(folder_path, file_name)

        # Abrir o arquivo HTML para leitura
        with open(file_path, 'r') as file:
            html_content = file.read()

        target_string = "https://drive.google.com/thumb"

        tags_encontradas = procurar_string_em_html(html_content, target_string)

        if tags_encontradas:
            print("As seguintes tags contêm a string:")
            for tag in tags_encontradas:
                print(tag)
        else:
            print("A string não foi encontrada em nenhuma tag.")

        



#print("encontrei um arquivo com vídeo \n o nome do arquivo é :" + file_name + " \n")
            

for sites in html_videos_list :
    print(sites)
        


# i = 0
# have_video = False
# arquivo_point = "21 Denavit-Hartenbergs Notation.html"
# pointlocal = "pointlocal.html"
# #Abrindo o arquivo para leitura e armazenando suas linhas na lista linhas
# with open(arquivo_point, "r") as arquivo :
#     linhas = arquivo.readlines()

# #Percorrendo todas as linhas do arquivo
# for linha in linhas :
#     #Encontrando a linha desejada para modificação, armazenando seu conteudo e seu endereço na lista
#     if(encontrar_palavra(linha,"https://drive.google.com/thumb")) :
#         texto_subst = linha
#         i = i+1
#         index_texto_subst = i
#         have_video = True
#     else :
#         i = i+1

# # Verificando se tem algum video no arquivo e se tiver substituir as linhas que eram do vídeo no drive para o video local
# if have_video :
#     deletar_faixa_linhas_arquivo(arquivo_point, index_texto_subst-16, index_texto_subst+7)
#     adicionar_texto_arquivo(arquivo_point, index_texto_subst-16, pointlocal)