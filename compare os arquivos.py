import os
import sys
import filecmp
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Comparar Pastas')
folder1_label = tk.Label(root, text='Insira a primeira pasta:')
folder1_entry = tk.Entry(root)
folder2_label = tk.Label(root, text='Insira a segunda pasta:')
folder2_entry = tk.Entry(root)

compare_button = tk.Button(root, text='Comparar')

def compare_folders():
    pasta1 = folder1_entry.get()
    pasta2 = folder2_entry.get()
    
    def pasta_size(folder):
        total_size = 0
        for path, dirs, files in os.walk(folder):
            for f in files:
                fp = os.path.join(path, f)
                total_size += os.path.getsize(fp)
        return total_size

    size1 = pasta_size(pasta1)
    size2 = pasta_size(pasta2)

    if size1 == size2:
        # Exibir uma caixa de mensagem com o resultado da comparação
        messagebox.showinfo('Resultado', 'As pastas são iguais.')
    else: 
        messagebox.showinfo('Resultado', 'As pastas são diferentes.')

compare_button.config(command=compare_folders)



folder1_label.pack()
folder1_entry.pack()
folder2_label.pack()
folder2_entry.pack()
compare_button.pack()

root.mainloop()


