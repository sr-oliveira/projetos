import os
from time import sleep
import tkinter as tk
import shutil

# Cria uma janela principal
root = tk.Tk()
root.title("Assistente CDA - ProgramadoPor-G.O")

# Define a função que será chamada quando o botão for clicado
def contar_arquivos():
  # Obtém o caminho do diretório inserido pelo usuário
  directory = entrada_diretorio.get()

  # Percorre todas as pastas e subpastas do diretório
  for root, dirs, files in os.walk(directory):
    # Conta o número de arquivos na pasta atual
    file_count = len(files)

    # Verifica se a pasta atual tem mais de dez arquivos
    if file_count > 9:
      # Adiciona uma nova linha na área de saída com o caminho para a pasta e o número de arquivos nela
      saida_texto.insert(tk.END, f'A pasta {root} tem {file_count} arquivos\n')



# Define a função que será chamada quando o botão for clicado
def copiar_pastas():
  # Obtém os caminhos das pastas inseridas pelo usuário
  origens = input("Pastas de origem (separadas por vírgula)").split(",")
  destino = input("Pasta de destino")

  # Percorre as pastas de origem e copia cada uma para a pasta de destino
  for origem in origens:
    shutil.copytree(origem, destino)

  # Adiciona uma nova linha na área de saída informando que a pasta foi copiada com sucesso
  saida_texto.insert(tk.END, f'A pasta {origem} foi copiada com sucesso para {destino}\n')






# Cria um rótulo para o campo de entrada do diretório
rotulo_diretorio = tk.Label(root, text="Inserir origem:")
rotulo_diretorio.grid(row=0, column=0)

# Cria um campo de entrada do diretório
entrada_diretorio = tk.Entry(root)
entrada_diretorio.grid(row=0, column=1)

# Cria um botão para iniciar a contagem de arquivos
botao_contar = tk.Button(root, text="Contar arquivos", command=contar_arquivos,)
botao_contar.grid(row=2, column=0, columnspan=1)

# Cria uma área de saída para exibir os resultados
saida_texto = tk.Text(root, width=103)
saida_texto.grid(row=25, column=0, columnspan=25)

root = tk.Tk()
# Cria um rótulo para o campo de entrada da pasta de origem
rotulo_origem = tk.Label(root, text="Insira a pasta a ser copiada:")
rotulo_origem.grid(row=0, column=0)

# Cria um campo de entrada da pasta de origem
entrada_origem = tk.Entry(root)
entrada_origem.grid(row=0, column=1)

# Cria um rótulo para o campo de entrada da pasta de destino
rotulo_destino = tk.Label(root, text="Insira a pasta de destino:")
rotulo_destino.grid(row=5, column=50)


# Inicia a janela principal
root.mainloop()
