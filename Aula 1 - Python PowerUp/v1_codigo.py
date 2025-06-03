import pyautogui
import time

pyautogui.PAUSE = 0.5 

# Windows + 1 (Como tengo Google Chrome anclado a la barra de tareas, lo selecciono y creo una pestaña nueva)
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

# Passo 4: Cadastrar um produto
# codigo,marca,tipo,categoria,preco_unitario,custo,obs
# MOLO000251,Logitech,Mouse,1,25.95,6.50,

# clicar no campo de código
pyautogui.hotkey("tab")
# pegar da tabela o valor do campo que a gente quer preencher
codigo = "MOLO000251"
# preencher o campo
pyautogui.write(str(codigo))
# passar para o proximo campo
pyautogui.press("tab")
# preencher o campo
pyautogui.write("Logitech")
pyautogui.press("tab")
pyautogui.write("Mouse")
pyautogui.press("tab")
pyautogui.write("1")
pyautogui.press("tab")
pyautogui.write("25.95")
pyautogui.press("tab")
pyautogui.write("6.50")
pyautogui.press("tab")
# obs = tabela.loc[linha, "obs"]
# if not pd.isna(obs):
#     pyautogui.write(str(tabela.loc[linha, "obs"]))
pyautogui.press("tab")
pyautogui.press("enter") # cadastra o produto (botao enviar)
# dar scroll de tudo pra cima
pyautogui.scroll(5000)
pyautogui.click(x=322, y=236)

# Passo 5: Repetir o processo de cadastro até o fim