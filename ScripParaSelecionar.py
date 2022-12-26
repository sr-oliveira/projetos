import os 
import shutil 
import tkinter as tk 
from tkinter import *
from tkinter import messagebox, filedialog 
     
 
def CreateWidgets(): 
    link_Label = Label(root, text ="Selecione o arquivo : ", 
                    bg = "#E8D579") 
    link_Label.grid(row = 1, column = 0, 
                    pady = 5, padx = 5) 
     
    root.sourceText = Entry(root, width = 50, 
                            textvariable = sourceLocation) 
    root.sourceText.grid(row = 1, column = 1, 
                        pady = 5, padx = 5, 
                        columnspan = 2) 
     
    source_browseButton = Button(root, text ="Pasta", 
                                command = SourceBrowse, width = 15) 
    source_browseButton.grid(row = 1, column = 3, 
                            pady = 5, padx = 5) 
     
    destinationLabel = Label(root, text ="Selecione pasta de destino: ", 
                            bg ="#E8D579") 
    destinationLabel.grid(row = 2, column = 0, 
                        pady = 5, padx = 5) 
     
    root.destinationText = Entry(root, width = 50, 
                                textvariable = destinationLocation) 
    root.destinationText.grid(row = 2, column = 1, 
                            pady = 5, padx = 5, 
                            columnspan = 2) 
     
    dest_browseButton = Button(root, text ="Pasta", 
                            command = DestinationBrowse, width = 15) 
    dest_browseButton.grid(row = 2, column = 3, 
                        pady = 5, padx = 5) 
     
    copyButton = Button(root, text ="Copiar", 
                        command = CopyFile, width = 15) 
    copyButton.grid(row = 3, column = 1, 
                    pady = 5, padx = 5) 
     
    moveButton = Button(root, text ="Mover", 
                        command = MoveFile, width = 15) 
    moveButton.grid(row = 3, column = 2, 
                    pady = 5, padx = 5) 
 
def SourceBrowse(): 
     
    
    
    
    
    
    
    root.files_list = list(filedialog.askopenfilenames(initialdir ="C:/Users/AKASH / Desktop / Lockdown Certificate / Geek For Geek")) 
     
    
    
    root.sourceText.insert('1', root.files_list) 
     
def DestinationBrowse(): 
    
    
    
    
    
    destinationdirectory = filedialog.askdirectory(initialdir ="C:/Users/AKASH / Desktop / Lockdown Certificate / Geek For Geek") 
 
    
    
    
    root.destinationText.insert('1', destinationdirectory) 
     
def CopyFile(): 
    
    
    
    files_list = root.files_list 
        
    
    
    
    destination_location = destinationLocation.get() 
 
    
    for f in files_list: 
       
      
      shutil.copytree(f, destination_location) 
 
    messagebox.showinfo("SUCCESSO!") 
     
def MoveFile(): 
     
    
    
    
    files_list = root.files_list 
     
 
    
    
    
    destination_location = destinationLocation.get() 
 
    
    for f in files_list: 
       
      
      shutil.move(f, destination_location) 
 
    messagebox.showinfo("Sucesso!") 
 
root = tk.Tk() 
     
root.geometry("830x120") 
root.title("AJUDANTE DO GUSTAVO") 
root.config(background = "Beige") 
     
sourceLocation = StringVar() 
destinationLocation = StringVar() 
     
CreateWidgets() 
     
root.mainloop() 