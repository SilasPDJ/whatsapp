# WhatsApp Broadcast Automation

Projeto simples em Python para enviar mensagens e vídeos pelo WhatsApp a partir de uma lista do Excel.

## Descrição

Este script lê uma planilha Excel com contatos (nome e telefone), personaliza uma mensagem a partir de um template em `data/message.txt` e envia mensagens e um vídeo via WhatsApp usando a biblioteca `pywhatkit`.

## Estrutura do projeto

-   `main_convite.py` - script principal que faz a leitura da planilha e envia as mensagens e vídeos.
-   `data/` - arquivos de dados usados pelo script:

## Requisitos

-   Python 3.8+
-   Pacotes Python (instale com pip):
    -   pandas
    -   numpy
    -   python-dotenv
    -   pywhatkit
    -   pyautogui

## Instalação

Recomenda-se criar um ambiente virtual e instalar dependências:

```powershell
# Cria e ativa um venv no PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instala dependências
python -m pip install --upgrade pip
python -m pip install pandas numpy python-dotenv pywhatkit pyautogui
```

## Configuração

```env
# Exemplo .env
NUMBER_TEST=+5511999999999
```

## Melhorias sugeridas

-   Implementar um modo "dry-run" que apenas mostre as mensagens sem enviá-las.
-   Adicionar logs e tratamento de exceções para falhas de envio.
-   Remover a sobrescrição de `number` por `number_test` para permitir envio real.
-   Adicionar um `requirements.txt` para fixar dependências.
