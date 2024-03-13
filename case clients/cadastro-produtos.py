#Entrar no sistema da empresa
#Fazer login
#Importar a basa de dados - produtos.csv
#Cadastrar um produto
#Repetir o processo de cadastro até acabar

import pyautogui
import time


pyautogui.PAUSE = 0.5

#abrir o navegador windows
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#pausa maior, como uma garantia para problemas na internet
time.sleep(5)

#logar
pyautogui.click(x=686, y=424)

#digitar o email
pyautogui.write("gerente@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha")

pyautogui.click(x=741, y=504)
time.sleep(3)
pyautogui.click(x=961, y=562)
time.sleep(2)
pyautogui.press("enter")


import pandas
#importar base de dados
tabela = pandas.read_csv("produtos.csv")

#cadastrar produto no formulario

#clicar no primeiro campo

for linha in tabela.index:
    pyautogui.click(x=774, y=290)

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #categoria
    catego = str(tabela.loc[linha, "categoria"])
    pyautogui.write(catego)
    pyautogui.press("tab")

    #preco
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    #obs
    #é necessário uma condição de verificação pois existem campos NaN
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write("obs")
    pyautogui.press("tab")

    #enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)