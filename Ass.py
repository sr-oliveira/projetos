import os
from time import sleep
from tkinter import *

# Lê o caminho para o diretório inserido pelo usuário
directory = input("Inserir origem: ")

# Percorre todas as pastas e subpastas do diretório
for root, dirs, files in os.walk(directory):
  # Conta o número de arquivos na pasta atual
  file_count = len(files)

  # Verifica se a pasta atual tem mais de dez arquivos
  if file_count > 10:
    # Imprime o caminho completo para a pasta atual e o número de arquivos nela
    print(f'A pasta {root} tem {file_count} arquivos')



# Cria uma janela
window = Tk("Ajudante")

# Cria um label com o texto "Inserir origem:"
label = Label(window, text="Inserir origem:")

# Cria uma caixa de texto
textbox = Entry(window)

# Cria um botão com o texto "Executar"
button = Button(window, text= "Executar")

# Cria uma área de texto para exibir os resultados
textarea = Text(window)

# Posiciona os elementos na janela
label.pack()
textbox.pack()
button.pack()
textarea.pack()

# Cria uma janela
window = Tk()

# Cria um label com o texto "Inserir origem:"
label = Label(window, text="Inserir origem:")

# Cria uma caixa de texto
textbox = Entry(window)

# Cria um botão com o texto "Executar"
button = Button (window, text="Executar")



window.mainloop()


    
