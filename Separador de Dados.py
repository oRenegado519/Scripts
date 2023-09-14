import re
import tkinter as tk
from tkinter import scrolledtext


def separar_dados(texto):
    padrao_cnpj = r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}"
    padrao_nome_fornecedor = rf"{padrao_cnpj}\s+(.+?)\b"
    padrao_chave_nfe = r"\d{44}"

    cnpjs = re.findall(padrao_cnpj, texto)
    nomes_fornecedor = re.findall(padrao_nome_fornecedor, texto)
    chaves_nfe = re.findall(padrao_chave_nfe, texto)

    dados_separados = []

    for chave_nfe, cnpj, nome_fornecedor in zip(chaves_nfe, cnpjs, nomes_fornecedor):
        cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "")
        dados_separados.append(f"Chave NFE: {chave_nfe} - CNPJ: {cnpj} - Nome do fornecedor: {nome_fornecedor.strip()}")

    return dados_separados


def separar_texto():
    texto = texto_input.get("1.0", "end-1c")

    dados_separados = separar_dados(texto)

    dados_output.delete("1.0", "end")

    for dados in dados_separados:
        dados_output.insert("end", dados + "\n")


# Criação da janela principal
window = tk.Tk()
window.title("Separador de Dados")
window.geometry("800x500")

# Criação dos widgets
titulo_label = tk.Label(window, text="Insira o texto:")
titulo_label.pack()

texto_input = scrolledtext.ScrolledText(window, height=10, width=80)
texto_input.pack()

separar_button = tk.Button(window, text="Separar", command=separar_texto)
separar_button.pack()

dados_label = tk.Label(window, text="Dados separados:")
dados_label.pack()

dados_output = scrolledtext.ScrolledText(window, height=20, width=80)
dados_output.pack()

window.mainloop()
