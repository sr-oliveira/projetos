import os
from time import sleep
from tkinter import *

# Cria uma janela
window = Tk()

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


