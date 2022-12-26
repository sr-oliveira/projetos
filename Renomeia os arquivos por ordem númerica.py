import os
import shutil

# Solicita o caminho das pastas de origem e destino ao usuário
origem = input("Informe o caminho da pasta de origem: ")
destino = input("Informe o caminho da pasta de destino: ")

# Obtém uma lista de todos os arquivos, pastas e subpastas presentes na pasta de origem
itens = os.listdir(origem)

# Percorre a lista de itens
for item in itens:
  # Verifica se o item (arquivo, pasta ou subpasta) existe na pasta de destino
  if not os.path.exists(os.path.join(destino, item)):
    # Se o item não existir na pasta de destino, copia-o para lá
    shutil.copy(os.path.join(origem, item), destino)
  else:
    # Se o item existir na pasta de destino, verifica seu tamanho
    info_origem = os.stat(os.path.join(origem, item))
    info_destino = os.stat(os.path.join(destino, item))
    if info_origem.st_size > info_destino.st_size:
      # Se o tamanho do arquivo na pasta de origem for maior, copia-o para a pasta de destino substituindo o arquivo existente
      shutil.copy(os.path.join(origem,destino))
