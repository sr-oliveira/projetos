import os
from time import sleep
from tkinter import *
from interface import*

# Cria uma janela
window = Tk()

# Cria um label com o texto "Inserir origem:"
label = Label(window, text="Inserir origem:")

# Cria uma caixa de texto
textbox = Entry(window)

# Cria um botão com o texto "Executar"
button = Button(window, text="Executar)
