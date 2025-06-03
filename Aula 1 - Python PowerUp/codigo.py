import pyautogui
import time

pyautogui.PAUSE = 0.5 

# Windows + 9 (Como tengo Google Chrome anclado a la barra de tareas, lo selecciono y creo una pestaña nueva)
pyautogui.hotkey('win', '9') # 
time.sleep(1)
pyautogui.hotkey('ctrl', 't')

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.press("tab") # passando pro próximo campo
# escrever o seu email
pyautogui.write("pythontest1@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.press("enter") # apertar enter para fazer o login
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

time.sleep(1)

# contador para cortar antes las pruebas y no tener que comerse toda la carga
contador = 0

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    contador += 1
    # clicar no campo de código
    pyautogui.hotkey("tab")
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    pyautogui.click(x=322, y=236)
    if contador == 3:
        break
    # Passo 5: Repetir o processo de cadastro até o fim

