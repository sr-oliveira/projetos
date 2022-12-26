import os

# Lê o caminho para o diretório inserido pelo usuário
directory = input("Inserir origem: ")

# Percorre todas as pastas e subpastas do diretório
for root, dirs, files in os.walk(directory):
  # Conta o número de arquivos na pasta atual
  file_count = len(files)
  # Imprime o caminho completo para a pasta atual e o número de arquivos nela
  print(f'A pasta {root} tem {file_count} arquivos')
