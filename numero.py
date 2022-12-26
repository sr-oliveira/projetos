import os

# Caminho para o diretório que deseja percorrer
directory = 'D:\06-AREA DE TRABALHO\04- AREA DE TRABALHO\910000-RFQ-9E83--PO\A'

# Percorre todas as pastas e subpastas do diretório
for root, dirs, files in os.walk(directory):
  # Conta o número de arquivos na pasta atual
  file_count = len(files)
  # Imprime o caminho completo para a pasta atual e o número de arquivos nela
  print(f'A pasta {root} tem {file_count} arquivos')
