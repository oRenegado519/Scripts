import tkinter as tk
from tkinter import filedialog
import shutil
import os

def selecionar_arquivos():
    arquivos = filedialog.askopenfilenames(title="Selecione os arquivos")
    for arquivo in arquivos:
        lista_arquivos.insert(tk.END, arquivo)

def mover_arquivos():
    destino = "Z:\\entrada_saida\\entrada\\nfe\\emp 1 - SUPERMERCADO SOUZA BUENO LTDA"
    for arquivo in lista_arquivos.get(0, tk.END):
        try:
            shutil.move(arquivo, destino)
            lista_arquivos.delete(lista_arquivos.get(0, tk.END).index(arquivo))
        except Exception as e:
            print(f"Erro ao mover {arquivo}: {str(e)}")

    mensagem_sucesso.config(text="Arquivos movidos com sucesso!")

# Criar a janela principal
app = tk.Tk()
app.title("Mover XML's")
app.geometry("500x400")

# Criar a lista de arquivos selecionados
lista_arquivos = tk.Listbox(app, selectmode=tk.MULTIPLE)
lista_arquivos.pack(padx=0, pady=00)

# Botão para selecionar arquivos
botao_selecionar = tk.Button(app, text="Selecionar arquivos", command=selecionar_arquivos)
botao_selecionar.pack(pady=5)

# Botão para mover os arquivos selecionados
botao_mover = tk.Button(app, text="Mover arquivos", command=mover_arquivos)
botao_mover.pack(pady=5)

# Mensagem de sucesso
mensagem_sucesso = tk.Label(app, text="", fg="green")
mensagem_sucesso.pack(pady=5)

# Iniciar a execução do aplicativo
app.mainloop()
