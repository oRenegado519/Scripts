import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

class ScriptManager:
    def __init__(self, root):
        self.root = root
        self.script_folder = r'local_das_pastas_que_estao_os_scripts'
        self.scripts = []
        self.create_gui()

    def create_gui(self):
        self.root.title("Script Manager")
        self.root.geometry("420x400")
        self.root.config(bg="black")

        # Frame principal
        main_frame = tk.Frame(self.root, bg="black")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame para a lista de scripts
        scripts_frame = tk.Frame(main_frame, bg="black")
        scripts_frame.pack(pady=20)

        # Lista de scripts
        self.scripts_listbox = tk.Listbox(scripts_frame, bg="black", fg="white", selectbackground="gray",
                                      selectforeground="white", width=40)
        self.scripts_listbox.pack(side=tk.LEFT, fill=tk.BOTH)


        # Botão para adicionar script
        add_button = tk.Button(self.root, text="Adicionar Script", bg="black", fg="white", command=self.adicionar_script)
        add_button.pack(pady=10)

        # Botão para executar script selecionado
        execute_button = tk.Button(self.root, text="Executar Script", bg="black", fg="white", command=self.executar_script)
        execute_button.pack(pady=10)

        # Preencher a lista de scripts
        self.preencher_lista_scripts()

    def preencher_lista_scripts(self):
        if os.path.exists(self.script_folder):
            self.scripts = []
            self.scripts_listbox.delete(0, tk.END)
            for root, dirs, files in os.walk(self.script_folder):
                for file in files:
                    if file.endswith('.py'):
                        script_path = os.path.join(root, file)
                        script_name = os.path.splitext(file)[0]
                        self.scripts.append(script_path)
                        self.scripts_listbox.insert(tk.END, script_name)

    def adicionar_script(self):
        script_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if script_path:
            script_name = os.path.splitext(os.path.basename(script_path))[0]
            self.scripts.append(script_path)
            self.scripts_listbox.insert(tk.END, script_name)

    def executar_script(self):
        selected_index = self.scripts_listbox.curselection()
        if selected_index:
            script_path = self.scripts[selected_index[0]]
            try:
                subprocess.Popen(["python", script_path])
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        else:
            messagebox.showwarning("Aviso", "Nenhum script selecionado.")


# Cria a janela principal
root = tk.Tk()
root.config(bg="black")
root.option_add("*TCombobox*Listbox*Background", "white")
root.option_add("*TCombobox*Listbox*Foreground", "black")
root.title("Script Manager")

# Cria o Script Manager
script_manager = ScriptManager(root)

# Executa a janela principal
root.mainloop()
