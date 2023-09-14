import os
import time
from tkinter import Button
from tkinter import Tk, filedialog, messagebox, Button
from tkinter import Tk, filedialog, messagebox
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key
from pynput.mouse import Controller as MouseController

# Configurações dos tempos de espera
DELAY_OPEN = 1  # Tempo de espera para abrir cada PDF
DELAY_PRINT = 3  # Tempo de espera após pressionar CTRL+P
DELAY_ENTER = 2  # Tempo de espera após pressionar ENTER
DELAY_CLOSE = 2  # Tempo de espera após pressionar CTRL+W

class PDFPrinter:
    def __init__(self):
        self.root = Tk()
        self.root.title("PDF Printer")
        
        # Criação dos botões
        self.open_button = Button(self.root, text="Abrir PDFs", command=self.open_pdfs)
        self.open_button.pack()
        
        self.print_button = Button(self.root, text="Imprimir", command=self.print_pdfs)
        self.print_button.pack()
        
        self.root.mainloop()
    
    def open_pdfs(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        if len(files) > 0:
            for file in files:
                os.startfile(file)
                time.sleep(DELAY_OPEN)
    
    def print_pdfs(self):
        confirm = messagebox.askyesno("Confirmação", "Deseja imprimir os PDFs selecionados?")
        if confirm:
            keyboard = KeyboardController()
            mouse = MouseController()
            
            # Aguarda um tempo para garantir que a janela dos PDFs esteja ativa
            time.sleep(2)
            
            for _ in range(len(os.listdir())):
                keyboard.press(Key.ctrl)
                keyboard.press('p')
                keyboard.release('p')
                keyboard.release(Key.ctrl)
                time.sleep(DELAY_PRINT)
                
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(DELAY_ENTER)
                
                keyboard.press(Key.ctrl)
                keyboard.press('w')
                keyboard.release('w')
                keyboard.release(Key.ctrl)
                time.sleep(DELAY_CLOSE)
                
                # Move o cursor para a próxima posição de impressão
                mouse.move(0, 100)
                time.sleep(1)
    
if __name__ == "__main__":
    PDFPrinter()
