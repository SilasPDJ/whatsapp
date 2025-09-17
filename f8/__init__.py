from time import sleep
import tkinter as tk
import threading
from typing import Callable
import keyboard


class WaitPressF8:
    def __init__(self, script: Callable, use_gui: bool = True):
        self.script = script
        self.use_gui = use_gui
        self.should_exit = False

        if self.use_gui:
            self.create_gui()
        else:
            self.monitor_key_forever()

    def on_f8_press(self, event):
        self.script()
        print("Script Executado")

    def on_esc_press(self, event):
        print("Tecla ESC pressionada. Encerrando...")
        self.should_exit = True
        if self.use_gui:
            # fecha janela
            if hasattr(self, "root"):
                self.root.quit()

    def monitor_key(self):
        """
        Registra funções para chamadas nas teclas F8 e ESC
        """
        keyboard.on_press_key("f8", self.on_f8_press)
        keyboard.on_press_key("esc", self.on_esc_press)

    def monitor_key_forever(self):
        """
        Inicia o monitoramento da tecla F8 em foreground,
        sem interface gráfica e bloqueando a thread principal.
        ESC encerra o loop.
        """
        self.monitor_key()
        print("Monitorando tecla F8 (executa script) e ESC (encerra).")
        try:
            while not self.should_exit:
                sleep(0.1)
        except KeyboardInterrupt:
            pass
        print("Encerrando monitoramento.")

    def create_gui(self):
        """
        Função que cria a interface gráfica usando Tkinter.
        """

        self.root = tk.Tk()
        self.root.title("Pressione F8 (ESC para sair)")

        label = tk.Label(
            self.root,
            text="Pressione 'F8' para executar o script.\nPressione 'ESC' para sair.",
            font=("Arial", 14),
            justify="center",
        )
        label.pack(pady=20)

        # Iniciar a thread para monitorar tecla
        thread = threading.Thread(target=self.monitor_key, daemon=True)
        thread.start()

        # Fecha a aplicação se ESC for pressionado
        self.root.protocol("WM_DELETE_WINDOW", self.root.quit)

        self.root.mainloop()
