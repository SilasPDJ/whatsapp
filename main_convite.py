import pandas as pd
import os
from time import sleep
from numpy import dot
from pyperclip import paste
import pywhatkit
import pyautogui as pg
from dotenv import load_dotenv

from file_to_clipboard import copy_file_to_clipboard, paste_file
from pywhatkit.core import core


# Inicializa variáveis
load_dotenv()
number_test = os.getenv("NUMBER_TEST")

# carrega planilha de contatos
df = pd.read_excel("data/Lista_Congregacao.xlsx",
                   sheet_name="tratada").drop(index=0)

# declara mensagem
with open("data/message.txt", "r", encoding="utf-8") as f:
    message = f.read()


def trata_number(number: str, ddd: str = "+55") -> str:
    """Formata o número de telefone para o padrão brasileiro.

    Args:
        number (str): O número de telefone a ser formatado.
        ddd (str, optional): O código do país a ser adicionado. Padrão é "+55".

    Returns:
        str: O número de telefone formatado.
    """
    number = number.strip().replace(" ", "").replace(
        "-", "").replace("(", ddd).replace(")", "")
    return number


def main(is_test: bool = True):
    copy_file_to_clipboard(os.path.abspath(
        'data/convite-cruzada-evangelistica-semi.mp4'))

    print(df.head())

    for row in df.itertuples():
        name, number = row.Pastor, row.Telefone
        number = trata_number(number)
        if is_test:
            number = number_test

        personalized_message = message.replace("[pastor]", name)
        print(f"Enviando para {name} no número {number}...")

        def enviar_video():
            paste_file()
            print("Vídeo enviado.")

        pywhatkit.sendwhatmsg_instantly(
            number, personalized_message, wait_time=15, tab_close=True, action=lambda: enviar_video())
        break
        sleep(5)


if __name__ == "__main__":
    main()
