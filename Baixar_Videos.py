from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

def autenticar():
    gauth = GoogleAuth()
    # Realiza a autenticação com as credenciais do Google Drive
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

def baixar_arquivos_mp4(id_pasta, caminho_destino):
    # Autentica no Google Drive
    drive = autenticar()

    # Lista os arquivos na pasta do Google Drive
    arquivos = drive.ListFile({'q': f"'{id_pasta}' in parents and trashed=false"}).GetList()

    # Percorre os arquivos na pasta
    for arquivo in arquivos:
        if arquivo['mimeType'] == 'video/mp4':
            # Baixa o arquivo
            arquivo.GetContentFile(os.path.join(caminho_destino, arquivo['title']))

# ID da pasta no Google Drive
#id_pasta_google_drive = "1ML6qZBQPoUZTrBWaEhx8kkAS_bz_3zhc"

# Caminho de destino para salvar os arquivos MP4 baixados
#pasta_destino = "Videos_Local"

# Baixar todos os arquivos MP4 da pasta no Google Drive
def Baixar_arquivos_drive(id_pasta_google_drive, pasta_destino) :
    baixar_arquivos_mp4(id_pasta_google_drive, pasta_destino)