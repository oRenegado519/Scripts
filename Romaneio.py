import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, filedialog
import os

# Definir função de cálculo
def calcular():
    try:
        tara = float(valor_tara.get().replace(",", "."))
        quantidade = float(valor_quantidade.get().replace(",", "."))
        peso = float(valor_peso.get().replace(",", "."))

        resultado = round((peso - (tara * quantidade)), 2)

        valor_resultado.set(str(abs(resultado)).replace(".", ",") + " kg")
    except:
        messagebox.showerror("Erro", "Valores inválidos")

# Função chamada ao pressionar Enter em qualquer campo de entrada
def ao_pressionar_enter(event):
    calcular()

# Configurações da janela
root = tk.Tk()
root.geometry("350x250")
root.title("Cálculo de peso")
root.resizable(False, False)

# Configurar estilo do tema
style = ttk.Style()
style.theme_use('default')

# Criar frame principal
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

# Criar labels e campos de entrada
valor_tara = tk.StringVar()
label_tara = ttk.Label(frame, text="Tara", font=("Arial", 12))
label_tara.grid(row=0, column=0, sticky="W", pady=5)
entrada_tara = ttk.Entry(frame, textvariable=valor_tara, font=("Arial", 12))
entrada_tara.grid(row=0, column=1, pady=5)

valor_quantidade = tk.StringVar()
label_quantidade = ttk.Label(frame, text="Quantidade", font=("Arial", 12))
label_quantidade.grid(row=1, column=0, sticky="W", pady=5)
entrada_quantidade = ttk.Entry(frame, textvariable=valor_quantidade, font=("Arial", 12))
entrada_quantidade.grid(row=1, column=1, pady=5)

valor_peso = tk.StringVar()
label_peso = ttk.Label(frame, text="Peso", font=("Arial", 12))
label_peso.grid(row=2, column=0, sticky="W", pady=5)
entrada_peso = ttk.Entry(frame, textvariable=valor_peso, font=("Arial", 12))
entrada_peso.grid(row=2, column=1, pady=5)

# Criar botão de calcular
botao_calcular = ttk.Button(frame, text="Calcular", command=calcular)
botao_calcular.grid(row=3, column=0, columnspan=2, pady=10)

# Criar campo de resultado
valor_resultado = tk.StringVar()
valor_resultado.set("")
label_resultado = ttk.Label(frame, text="Resultado", font=("Arial", 12))
label_resultado.grid(row=4, column=0, sticky="W", pady=5)
entrada_resultado = ttk.Entry(frame, textvariable=valor_resultado, font=("Arial", 12))
entrada_resultado.grid(row=4, column=1, pady=5)

# Vincular a função ao_pressionar_enter aos campos de entrada
entrada_tara.bind("<Return>", ao_pressionar_enter)
entrada_quantidade.bind("<Return>", ao_pressionar_enter)
entrada_peso.bind("<Return>", ao_pressionar_enter)

# Iniciar loop da janela
root.mainloop()




