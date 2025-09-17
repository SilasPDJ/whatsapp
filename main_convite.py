import pandas as pd
import os
from time import sleep
from numpy import dot
import pywhatkit
import pyautogui as pg
from dotenv import load_dotenv


load_dotenv()


number_test = os.getenv("NUMBER_TEST")


df = pd.read_excel("data/Lista_Congregacao.xlsx",
                   sheet_name="tratada").drop(index=0)
print(df.head())
# input("ENTER para iniciar em 5 segundos...")

with open("data/message.txt", "r", encoding="utf-8") as f:
    message = f.read()


def trata_number(number: str) -> str:
    number = number.strip().replace(" ", "").replace(
        "-", "").replace("(", "+55").replace(")", "")
    return number

# Send a message instantly


for row in df.itertuples():
    name, number = row.Pastor, row.Telefone
    number = trata_number(number)

    number = number_test
    input(number)

    personalized_message = message.replace("[pastor]", name)
    print(f"Enviando para {name} no número {number}...")
    pywhatkit.sendwhatmsg_instantly(
        number, personalized_message, wait_time=20)
    pywhatkit.sendwhats_video_instantly(
        number, "data/convite-cruzada-evangelistica-semi.mp4", caption="Segue o vídeo!", wait_time=20, tab_close=True)
    sleep(5)


# Send a message to a group
# pywhatkit.sendwhatmsg_to_group("GroupName", "Group message!")
