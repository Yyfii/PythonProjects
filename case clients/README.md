#PythonProjects

link anotações: https://pt.anotepad.com/notes/njw6qepn

Automação de Tarefas | Jornada Python [Aula 1]

        Automatizar processos com python. Adicionar o arquivo python. codigo.py. Extensão dos arquivos python.

Por onde começo?🙋

      Escrever o paço a passo do seu projeto em pt-br.

      Traduzir para python.

   #passo a passo do projeto.

step1: Entrar no sistema da empresa.

  link: linkempresa.com

step2: Fazer Login

step3:  Importar a base de dados - produtos.csv

step4: Cadastrar um produto

step5: repetir o processo de cadastro até acabar

A lógica do programa.

 

Biblioteca: pacote de código que permite fazer alguma coisa especifica.

pyautogui - automatiza qualquer tarefa de mouse teclado e tela do computador.

pip install pyautogui - terminal

  pyautogui.click -> clicar em alguma coisa

                .write-> escrever um texto

                 .press-> pressionar 1 tecla do teclado

#abrir o navegador(chrome)

tecla windows - digitar chrome - enter

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

        pyautogui.hotkey("ctrl", "space") -> pressiona as duas teclas

pyautogui python - acesse a documentação.

linkemp = "linkempresa.com"-> use uma variavel, já que esse link pode precisar ser mudado no futuro. Boas práticas.

pyautogui.write(linkemp)

Entretanto, vai dar um erro. Não dá tempo, é muito rapido para ele escrever, do chrome abrir e ele não escreve o link em lugar nenhum. 

Ele digita no lugar certo automaticamente, com alguma exceções.

Passe no inicio, antes do import:

pyautogui.PAUSE = 0.5 -> a cada comando ele faz uma pausa de 1s

#entrar no site

pyautogui.write(linkemp)

pyautogui.press("Enter")

#dar uma pausa um pouco maior, no caso da internet estar lenta, neste lugar especifico

import time

time.sleep(5)-> esperar 5s😀

#logar

clicar para escrever - como clicar?😥

esse formato de automatização não dá praa fazer atividades em segundo plano. Existem formas.

# Programar a hora que ele vai fazer isso toda vez

a janela carregou, como clicar no campo de e-mail?

sorry but, não é o pyautogui.click(), pq ele precisa passar o lugar que vai clicar na tela do seu computador.

(x,y) -> indica a distancia da reta x e da reta y

 

#criar arquivo auxiliar.py

print(pyautogui.position()) -> posição do mouse no momento em que vc moveu o mouse

import time 

time.sleep(5)-> durante os cinco segundos a gente vai colocar o mouse na posição do email.

# vá no codigo e no click coloque a posição achada

pyautogui.click(x=714, y=465)

pyautogui.click(x=714, y=465, clicks= qtd_clicks, button=which_button)

x e y vão depender da resolução da tela

#digitar o email

payautogui.write("user23@gmai.com")

#passar para o campo da senha

payautogui.press("tab")

payaoutogui.write("senha")

#clicar no botão de logar

payautogui.click("x=89, y=78)

time.sleep(3) #pq depois ele tem que carregar uma página depois, garantir que o site carregou

roda o ar aux e ache a posição

o time e sleep somam-se, só que o PAUSE é apenas para comandos do payautogui.

#cadastrar produto

#importar a base de dados

utilizar outro pacote de código do python, que permita importar base de dados, a mais utilizada para importar bases de dados é o pandas.E instala logo o numpy e openpyxl1 pq pode precisar.

pip install pandas numpy  openpyx1

import pandas

pandas, lê a base de dados e armazenar dentro de uma variavel.

tabela = pandas.read_csv("produtos.csv")

print(tabela)

#cadastrar podutro no formulario

cod_produto, marca_produto, tipo_produto, cat_produto, preco_unit_prod, custo_produto, Obs.

#clicar no primeiro campo

payautogui.click(x=,y=)

#o codigo acima cadastra um unico produto

#como cadastramos todos os produtos da tabela?

#repetimos essa ação para cada linha da tabela

#para cada linha da minha tabela - tabela.index(linhas da tabela)

for linha in tabela.index:

#pegar informação de cod da tabela

#clicar no primeiro campo

payautogui.click(x=,y=)

#codigo do produto

payautogui.write("Codigo do produto")

payautogui.press("tab")

#marca

payautogui.write("marca")

payautogui.press("tab")

#tipo

payautogui.write("tipo")

payautogui.press("tab")

#categoriua

payautogui.write("categoria")

payautogui.press("tab")

#preco

payautogui.write("preco")

payautogui.press("tab")

#custo

payautogui.write("custo")

payautogui.press("tab")

#obs

payautogui.write("obs")

payautogui.press("tab")

#enviar

payautogui.press("tab")

payautogui.press("enter")

pyautogui.scroll(5000)#sobe -150-desce

#codigo do produto

#loc na tab a linh e col, lista de informações, toda lista em opython é entre colchetes- linha 1 - 0,1,2 -coluna- coluna codigo

#tem que passar em formato de texto os .write, tem que passar dentro de uma função str() -> texto

codigo = tabela.loc[linha,"codigo"]

payautogui.write(codigo)

payautogui.press("tab")

#marca

marca = tabela.loc[linha, "marca"]

payautogui.write(marca)

payautogui.press("tab")

#tipo

tipo = tabela.loc[linha, "tipo"]

payautogui.write(tipo)

payautogui.press("tab")

#categoriua

catego = tabela.loc[linha, "categoria"]

payautogui.write(catego)

payautogui.press("tab")

#preco

preco = str(tabela.loc[linha, "preco"])

payautogui.write(preco)

payautogui.press("tab")

#custo

custo = str(tabela.loc[linha, "custo"])

payautogui.write(custo)

payautogui.press("tab")

#obs, na tabela, existem algumas vazias, dá erro

#precisa-se tratar essa condição, verificar se está vazia

obs = tabela.loc[linha, "obs"]

if not pandas.isna(obs):#isna verifica se está vazia, is na - é vazio NaN - Not a Number

      payautogui.write(obs)# se não for vazio ele pega a info, se não ele passa        com o tab

payautogui.press("tab")

#enviar

payautogui.press("tab")

payautogui.press("enter")

pyautogui.scroll(5000)#sobe -150-desce

#Pronto! agora ele consegue cadastrar o produto!
