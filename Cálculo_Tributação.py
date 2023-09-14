import tkinter as tk
from tkinter import ttk, messagebox

# Função para calcular a Base de ICMS
def calcular_base_icms():
    try:
        valor = float(base_icms_valor.get().replace(",", "."))
        reducao = float(base_icms_reducao.get().replace(",", "."))

        resultado = valor * (1 - reducao / 100)

        base_icms_resultado.set(f"{resultado:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Valores inválidos")

# Função para calcular o Valor do ICMS
def calcular_valor_icms():
    try:
        base_icms = float(valor_icms_base_icms.get().replace(",", "."))
        aliquota = float(valor_icms_aliquota.get().replace(",", "."))

        resultado = base_icms * aliquota / 100

        valor_icms_resultado.set(f"{resultado:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Valores inválidos")

# Função para calcular a Base de ICMS ST
def calcular_base_icms_st():
    try:
        valor_produto = float(base_icms_st_valor_produto.get().replace(",", "."))
        ipi = float(base_icms_st_ipi.get().replace(",", "."))
        iva = float(base_icms_st_iva.get().replace(",", "."))
        reducao = float(base_icms_st_reducao.get().replace(",", "."))

        resultado = (valor_produto + ipi) * (1 + iva / 100) * (1 - reducao / 100)

        base_icms_st_resultado.set(f"{resultado:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Valores inválidos")

# Função para calcular o Valor do ICMS ST
def calcular_valor_icms_st():
    try:
        base_icms_st = float(valor_icms_st_base_icms_st.get().replace(",", "."))
        aliquota_cadastro = float(valor_icms_st_aliquota_cadastro.get().replace(",", "."))
        valor_icms = float(valor_icms_st_valor_icms.get().replace(",", "."))

        resultado = base_icms_st * aliquota_cadastro / 100 - valor_icms

        valor_icms_st_resultado.set(f"{resultado:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Valores inválidos")

# Função para calcular o IVA
def calcular_iva():
    try:
        base_icms_st = float(calcular_iva_base_icms_st.get().replace(",", "."))
        reducao_cadastro = float(calcular_iva_reducao_cadastro.get().replace(",", "."))
        valor_total_produto = float(calcular_iva_valor_total_produto.get().replace(",", "."))
        valor_ipi = float(calcular_iva_valor_ipi.get().replace(",", "."))

        resultado = ((base_icms_st / (1 - reducao_cadastro / 100)) - (valor_total_produto + valor_ipi)) * 100 / (valor_total_produto + valor_ipi)

        iva_resultado.set("{:.2f}%".format(resultado))
    except ValueError:
        messagebox.showerror("Erro", "Valores inválidos")

# Configurações da janela
root = tk.Tk()
root.geometry("400x400")
root.title("Cálculo de Tributação")

# Configurar estilo do tema
style = ttk.Style()
style.theme_use('default')

# Criar abas
tab_control = ttk.Notebook(root)

# Aba de Base de ICMS
tab_base_icms = ttk.Frame(tab_control)
tab_control.add(tab_base_icms, text='Base ICMS')

# Componentes da aba de Base de ICMS
base_icms_label = ttk.Label(tab_base_icms, text='Valor:')
base_icms_label.grid(column=0, row=0, padx=10, pady=10)
base_icms_valor = tk.StringVar()
base_icms_entry = ttk.Entry(tab_base_icms, width=15, textvariable=base_icms_valor)
base_icms_entry.grid(column=1, row=0, padx=10, pady=10)

base_icms_reducao_label = ttk.Label(tab_base_icms, text='Redução (%):')
base_icms_reducao_label.grid(column=0, row=1, padx=10, pady=10)
base_icms_reducao = tk.StringVar()
base_icms_reducao_entry = ttk.Entry(tab_base_icms, width=15, textvariable=base_icms_reducao)
base_icms_reducao_entry.grid(column=1, row=1, padx=10, pady=10)

base_icms_calcular_button = ttk.Button(tab_base_icms, text='Calcular', command=calcular_base_icms)
base_icms_calcular_button.grid(column=1, row=2, padx=10, pady=10)

base_icms_resultado_label = ttk.Label(tab_base_icms, text='Resultado:')
base_icms_resultado_label.grid(column=0, row=3, padx=10, pady=10)
base_icms_resultado = tk.StringVar()
base_icms_resultado_entry = ttk.Entry(tab_base_icms, width=15, state='readonly', textvariable=base_icms_resultado)
base_icms_resultado_entry.grid(column=1, row=3, padx=10, pady=10)

# Aba de Valor do ICMS
tab_valor_icms = ttk.Frame(tab_control)
tab_control.add(tab_valor_icms, text='Valor ICMS')

# Componentes da aba de Valor do ICMS
valor_icms_base_icms_label = ttk.Label(tab_valor_icms, text='Base ICMS:')
valor_icms_base_icms_label.grid(column=0, row=0, padx=10, pady=10)
valor_icms_base_icms = tk.StringVar()
valor_icms_base_icms_entry = ttk.Entry(tab_valor_icms, width=15, textvariable=valor_icms_base_icms)
valor_icms_base_icms_entry.grid(column=1, row=0, padx=10, pady=10)

valor_icms_aliquota_label = ttk.Label(tab_valor_icms, text='Alíquota (%):')
valor_icms_aliquota_label.grid(column=0, row=1, padx=10, pady=10)
valor_icms_aliquota = tk.StringVar()
valor_icms_aliquota_entry = ttk.Entry(tab_valor_icms, width=15, textvariable=valor_icms_aliquota)
valor_icms_aliquota_entry.grid(column=1, row=1, padx=10, pady=10)

valor_icms_calcular_button = ttk.Button(tab_valor_icms, text='Calcular', command=calcular_valor_icms)
valor_icms_calcular_button.grid(column=1, row=2, padx=10, pady=10)

valor_icms_resultado_label = ttk.Label(tab_valor_icms, text='Resultado:')
valor_icms_resultado_label.grid(column=0, row=3, padx=10, pady=10)
valor_icms_resultado = tk.StringVar()
valor_icms_resultado_entry = ttk.Entry(tab_valor_icms, width=15, state='readonly', textvariable=valor_icms_resultado)
valor_icms_resultado_entry.grid(column=1, row=3, padx=10, pady=10)

# Aba de Base de ICMS ST
tab_base_icms_st = ttk.Frame(tab_control)
tab_control.add(tab_base_icms_st, text='Base ICMS ST')

# Componentes da aba de Base de ICMS ST
base_icms_st_valor_produto_label = ttk.Label(tab_base_icms_st, text='Valor do Produto:')
base_icms_st_valor_produto_label.grid(column=0, row=0, padx=10, pady=10)
base_icms_st_valor_produto = tk.StringVar()
base_icms_st_valor_produto_entry = ttk.Entry(tab_base_icms_st, width=15, textvariable=base_icms_st_valor_produto)
base_icms_st_valor_produto_entry.grid(column=1, row=0, padx=10, pady=10)

base_icms_st_ipi_label = ttk.Label(tab_base_icms_st, text='IPI:')
base_icms_st_ipi_label.grid(column=0, row=1, padx=10, pady=10)
base_icms_st_ipi = tk.StringVar()
base_icms_st_ipi_entry = ttk.Entry(tab_base_icms_st, width=15, textvariable=base_icms_st_ipi)
base_icms_st_ipi_entry.grid(column=1, row=1, padx=10, pady=10)

base_icms_st_iva_label = ttk.Label(tab_base_icms_st, text='IVA (%):')
base_icms_st_iva_label.grid(column=0, row=2, padx=10, pady=10)
base_icms_st_iva = tk.StringVar()
base_icms_st_iva_entry = ttk.Entry(tab_base_icms_st, width=15, textvariable=base_icms_st_iva)
base_icms_st_iva_entry.grid(column=1, row=2, padx=10, pady=10)

base_icms_st_reducao_label = ttk.Label(tab_base_icms_st, text='Redução (%):')
base_icms_st_reducao_label.grid(column=0, row=3, padx=10, pady=10)
base_icms_st_reducao = tk.StringVar()
base_icms_st_reducao_entry = ttk.Entry(tab_base_icms_st, width=15, textvariable=base_icms_st_reducao)
base_icms_st_reducao_entry.grid(column=1, row=3, padx=10, pady=10)

base_icms_st_calcular_button = ttk.Button(tab_base_icms_st, text='Calcular', command=calcular_base_icms_st)
base_icms_st_calcular_button.grid(column=1, row=4, padx=10, pady=10)

base_icms_st_resultado_label = ttk.Label(tab_base_icms_st, text='Resultado:')
base_icms_st_resultado_label.grid(column=0, row=5, padx=10, pady=10)
base_icms_st_resultado = tk.StringVar()
base_icms_st_resultado_entry = ttk.Entry(tab_base_icms_st, width=15, state='readonly', textvariable=base_icms_st_resultado)
base_icms_st_resultado_entry.grid(column=1, row=5, padx=10, pady=10)

# Aba de Valor do ICMS ST
tab_valor_icms_st = ttk.Frame(tab_control)
tab_control.add(tab_valor_icms_st, text='Valor ICMS ST')

# Componentes da aba de Valor do ICMS ST
valor_icms_st_base_icms_st_label = ttk.Label(tab_valor_icms_st, text='Base ICMS ST:')
valor_icms_st_base_icms_st_label.grid(column=0, row=0, padx=10, pady=10)
valor_icms_st_base_icms_st = tk.StringVar()
valor_icms_st_base_icms_st_entry = ttk.Entry(tab_valor_icms_st, width=15, textvariable=valor_icms_st_base_icms_st)
valor_icms_st_base_icms_st_entry.grid(column=1, row=0, padx=10, pady=10)

valor_icms_st_aliquota_cadastro_label = ttk.Label(tab_valor_icms_st, text='Alíquota de Cadastro (%):')
valor_icms_st_aliquota_cadastro_label.grid(column=0, row=1, padx=10, pady=10)
valor_icms_st_aliquota_cadastro = tk.StringVar()
valor_icms_st_aliquota_cadastro_entry = ttk.Entry(tab_valor_icms_st, width=15, textvariable=valor_icms_st_aliquota_cadastro)
valor_icms_st_aliquota_cadastro_entry.grid(column=1, row=1, padx=10, pady=10)

valor_icms_st_valor_icms_label = ttk.Label(tab_valor_icms_st, text='Valor ICMS:')
valor_icms_st_valor_icms_label.grid(column=0, row=2, padx=10, pady=10)
valor_icms_st_valor_icms = tk.StringVar()
valor_icms_st_valor_icms_entry = ttk.Entry(tab_valor_icms_st, width=15, textvariable=valor_icms_st_valor_icms)
valor_icms_st_valor_icms_entry.grid(column=1, row=2, padx=10, pady=10)

valor_icms_st_calcular_button = ttk.Button(tab_valor_icms_st, text='Calcular', command=calcular_valor_icms_st)
valor_icms_st_calcular_button.grid(column=1, row=3, padx=10, pady=10)

valor_icms_st_resultado_label = ttk.Label(tab_valor_icms_st, text='Resultado:')
valor_icms_st_resultado_label.grid(column=0, row=4, padx=10, pady=10)
valor_icms_st_resultado = tk.StringVar()
valor_icms_st_resultado_entry = ttk.Entry(tab_valor_icms_st, width=15, state='readonly', textvariable=valor_icms_st_resultado)
valor_icms_st_resultado_entry.grid(column=1, row=4, padx=10, pady=10)

# Aba de Cálculo de IVA
tab_calcular_iva = ttk.Frame(tab_control)
tab_control.add(tab_calcular_iva, text='Cálculo de IVA')

# Componentes da aba de Cálculo de IVA
calcular_iva_base_icms_st_label = ttk.Label(tab_calcular_iva, text='Base ICMS ST:')
calcular_iva_base_icms_st_label.grid(column=0, row=0, padx=10, pady=10)
calcular_iva_base_icms_st = tk.StringVar()
calcular_iva_base_icms_st_entry = ttk.Entry(tab_calcular_iva, width=15, textvariable=calcular_iva_base_icms_st)
calcular_iva_base_icms_st_entry.grid(column=1, row=0, padx=10, pady=10)

calcular_iva_reducao_cadastro_label = ttk.Label(tab_calcular_iva, text='Redução de Cadastro (%):')
calcular_iva_reducao_cadastro_label.grid(column=0, row=1, padx=10, pady=10)
calcular_iva_reducao_cadastro = tk.StringVar()
calcular_iva_reducao_cadastro_entry = ttk.Entry(tab_calcular_iva, width=15, textvariable=calcular_iva_reducao_cadastro)
calcular_iva_reducao_cadastro_entry.grid(column=1, row=1, padx=10, pady=10)

calcular_iva_valor_total_produto_label = ttk.Label(tab_calcular_iva, text='Valor Total do Produto:')
calcular_iva_valor_total_produto_label.grid(column=0, row=2, padx=10, pady=10)
calcular_iva_valor_total_produto = tk.StringVar()
calcular_iva_valor_total_produto_entry = ttk.Entry(tab_calcular_iva, width=15, textvariable=calcular_iva_valor_total_produto)
calcular_iva_valor_total_produto_entry.grid(column=1, row=2, padx=10, pady=10)

calcular_iva_valor_ipi_label = ttk.Label(tab_calcular_iva, text='Valor do IPI:')
calcular_iva_valor_ipi_label.grid(column=0, row=3, padx=10, pady=10)
calcular_iva_valor_ipi = tk.StringVar()
calcular_iva_valor_ipi_entry = ttk.Entry(tab_calcular_iva, width=15, textvariable=calcular_iva_valor_ipi)
calcular_iva_valor_ipi_entry.grid(column=1, row=3, padx=10, pady=10)

calcular_iva_calcular_button = ttk.Button(tab_calcular_iva, text='Calcular', command=calcular_iva)
calcular_iva_calcular_button.grid(column=1, row=4, padx=10, pady=10)

iva_resultado_label = ttk.Label(tab_calcular_iva, text='Resultado:')
iva_resultado_label.grid(column=0, row=5, padx=10, pady=10)
iva_resultado = tk.StringVar()
iva_resultado_entry = ttk.Entry(tab_calcular_iva, width=15, state='readonly', textvariable=iva_resultado)
iva_resultado_entry.grid(column=1, row=5, padx=10, pady=10)

# Adicionar as abas à janela principal
tab_control.pack(expand=1, fill='both')

# Iniciar a janela
root.mainloop()
