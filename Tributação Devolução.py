import tkinter as tk

def calcular():
    base_icms = float(base_icms_entry.get().replace(",", "."))
    icmsst = float(icmsst_entry.get().replace(",", "."))
    base_calculo = float(base_calculo_entry.get().replace(",", "."))
    valor_icms = float(valor_icms_entry.get().replace(",", "."))
    quantidade_total = float(quantidade_total_entry.get().replace(",", "."))
    quantidade_devolucao = float(quantidade_devolucao_entry.get().replace(",", "."))

    base_icms_devolucao = base_icms / quantidade_total * quantidade_devolucao
    icmsst_devolucao = icmsst / quantidade_total * quantidade_devolucao
    base_calculo_devolucao = base_calculo / quantidade_total * quantidade_devolucao
    valor_icms_devolucao = valor_icms / quantidade_total * quantidade_devolucao

    resposta_text.config(state=tk.NORMAL)
    resposta_text.delete("1.0", tk.END)
    resposta_text.insert(tk.END, f"Base ICMS Devolução: {str(base_icms_devolucao).replace('.', ',')}\n"
                                f"ICMSST Devolução: {str(icmsst_devolucao).replace('.', ',')}\n"
                                f"Base de Cálculo Devolução: {str(base_calculo_devolucao).replace('.', ',')}\n"
                                f"Valor ICMS Devolução: {str(valor_icms_devolucao).replace('.', ',')}")
    resposta_text.config(state=tk.DISABLED)

# Criar a janela
janela = tk.Tk()
janela.title("Tributação Devolução")

# Definir o tamanho da janela
janela.geometry("400x300")

# Criar as caixas de texto
base_icms_label = tk.Label(janela, text="Base ICMS:")
base_icms_label.pack()
base_icms_entry = tk.Entry(janela)
base_icms_entry.pack()

icmsst_label = tk.Label(janela, text="ICMSST:")
icmsst_label.pack()
icmsst_entry = tk.Entry(janela)
icmsst_entry.pack()

base_calculo_label = tk.Label(janela, text="Base de Cálculo:")
base_calculo_label.pack()
base_calculo_entry = tk.Entry(janela)
base_calculo_entry.pack()

valor_icms_label = tk.Label(janela, text="Valor ICMS:")
valor_icms_label.pack()
valor_icms_entry = tk.Entry(janela)
valor_icms_entry.pack()

quantidade_total_label = tk.Label(janela, text="Quantidade Total:")
quantidade_total_label.pack()
quantidade_total_entry = tk.Entry(janela)
quantidade_total_entry.pack()

quantidade_devolucao_label = tk.Label(janela, text="Quantidade de Devolução:")
quantidade_devolucao_label.pack()
quantidade_devolucao_entry = tk.Entry(janela)
quantidade_devolucao_entry.pack()

calcular_button = tk.Button(janela, text="Calcular", command=calcular)
calcular_button.pack()

resposta_label = tk.Label(janela, text="Respostas:")
resposta_label.pack()

resposta_text = tk.Text(janela, height=5)
resposta_text.pack()
resposta_text.config(state=tk.DISABLED)

# Iniciar a janela principal
janela.mainloop()
