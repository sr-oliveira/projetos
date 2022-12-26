import os

# Pedimos ao usuário para inserir o caminho para o diretório onde as pastas estão localizadas
caminho = input("Insira o caminho para o diretório: ")

# Obtemos o caminho absoluto para o diretório especificado pelo usuário
diretorio = os.path.abspath(caminho)

# Mudamos para o diretório especificado pelo usuário
os.chdir(diretorio)

# Obtemos a lista de pastas no diretório atual
pastas = os.listdir()

# Percorremos cada pasta na lista
for pasta in pastas:
  # Verificamos se a pasta existe no diretório atual
  if os.path.isdir(pasta):
    # Definimos o novo nome da pasta como uma string vazia
    novo_nome = ""

    # Percorremos cada caractere na pasta
    for i, c in enumerate(pasta):
      # Adicionamos o caractere ao novo nome
      novo_nome += c

      # Se esse é o segundo, quarto, sexto, etc. caractere, adicionamos um traço depois dele
      # Desde que a pasta tenha pelo menos três caracteres
      if i % 2 == 1 and len(pasta) >= 3:
        novo_nome += "- "

    # Renomeamos a pasta com o novo nome
    os.rename(pasta, novo_nome)
    print("Sucesso! Pastas renomeadas meu fi")
