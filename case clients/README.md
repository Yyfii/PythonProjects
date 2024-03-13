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


Python Insights: Analisando Dados com Python [Aula 2]

#Análise e Tratamento de dados

link aula

link arquivos

Python Insights - Analisando Dados com Python

Case - Cancelamento de Clientes

projeto de dados - usar as bases de dados para encontrar respostas para os problemas.

notebook: mais usados para projetos de dados

--

#Por que os clientes cancelaram o serviço da empresa?

--

#planejar codigo - passo a passo

- step1: Importar a base de dados de clientes

- step2: Visualizar a base de dados(formatação, colunas, para ver se nessa base de dados tem as informações necessárias para o projeto; prepara o passo 3)

- step3: Fazer a limpeza/correção da base de dados

- step4: Analise os cancelamentos

- step5: Analise da causa de cancelamento



bibliotecas : pacotes de código que ajudam a resolver os desafios

#trabalhar com base de dados -> pandas

#graficos a dashboards -> plotly

pip install pandas numpy openpyxl nbformat ipykernel ploty

executar o jupyter notebook - o arquivo deve ser um arq.ipynb

Quando for selecionar o kernel, tenha certeza de escolher a versão atual que vocÊ utiliza.

google colab ou python notebook

pandas - base de dados, algumas funções usa o numpy, pois ele fica mais otimizado

openpyx1 - excel

plotly - gráficos

#importar a base de dados do cliente

#usando o pandas

import pandas as pd



#pandas lê traz para uma var

tabela = pd.read_csv("cancelamentos.csv")

#visualizar a base de dados

print(tabela)

#no vscode

display(tabela)

#display mostra a tabela visualmente melhor

#oque temos na base de dados

#id, nome, total_gasto,..,cancel_yes_no, informações sobre o cliente.

#Identificar colunas inúteis

- Que é inútil para a análise(motivo do cancel do cliente)

- Id do cliente(nº unico do cliente, como se fosse o cpf do cliente, se o cliente tem um id diferente ele vai ter mais chance de cancel or no)

- Informações que não te ajudam, te atrapalham, que não te ajuda a análisar exatamente nda, ela astá te atrapalhando, torna a base de dados mais pesada, pode te cconfudir, te desviar do objetivo principal.

#deletar coluna inútil.

tabela = tabela.drop(colums="CustumerID")

display(tabela)

#se fosse mais de uma

#tabela = tabela.drop(colums=["CustumerID","Idade","Sexo")

display(tabela)

#Valores vazios, erros de preenchimento, Informações vazias, se a informação está vazia, é inútil, é necessário tratar os valores vazios.

#Ex se a idade estivesse vazia, eu não conseguiria dizer se# a idade influenciou no cancelamento.



#correção da base de dados - problemas

#valores vazios erros de preenchimento

display(tabela.info())

# o cod acima diz quantos valores  preenchidos em cada coluna.

# no caso 5 linhas de 50000 não estão preenchidas, é uma pequena qtd, então não influencia na análise.

#excluir linhas vazias

tabela = tabela.dropna()

display(tabela.info())

#nan-not a number, olha a base de dados e exclui

m linhas vazias.

#todas as colunas terão a mesma qtd de numeros.

#analisar o cancelamento

#0-cancel 1-não cancelou

#Quantos clientes são 0? E quantos clientes são 1?

#contar os valores da coluna cancelou

#passo 4: Analise os cancelamentos

tabela["cancelou"] - coluna cancelou

tabela["cancelou"].value_counts()#conta os valores da coluna

display(tabela["cancelou"].value_counts())

#mostra qtd de clientes que cancel e não cancel

# e se eu quisesse em percentual:

#processo chamado de normalizar

display(tabela["cancelou"].value_counts(normalize=True))

#mostra o percentual agora, proporção

#normalize, se não colocar ele é falso, se colocar True, ele exibe um percentual, proporção.

#pode ser usado para qualquer coluna

#exemplo se fosse a coluna "assinatura"

#Ele exibiria, quantas pessoas possuem a assinatura premium, Standard e Basic. E o percentual de pessoas que possuem as assinaturas.

#Se preocupe com aformatação numérica, arredondamento de números no final do projeto

#aplicar uma função nos valores

display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}")

#aplica uma formatação, que vai ter uma casa decimal e vai ser em percentual

#agora aparece em casa decimal e com porcentagem

display(tabela["cancelou"].value_counts(normalize=True).map("{:.0%}")

#agora apareceria sem casa decimal, 50%,40%..

display(tabela["cancelou"].value_counts(normalize=True).map("{:.3%}")

#agora 3 casas decimais, 56.791%..

#enfm, deixe para o final.

-----------------------------------------------------------------

#última etapa do projeto

#analisar a causa de cancelamento do cliente

#Como que a coluna de dur do contrato afeta no cancel

#A galera do contrato anual cancela mais ou menos que a galera do contrato mensal?

#A galera da assinatura standard cancela mais ou menos que a da assinatura premium?

#Assinatura basic, cancela mais ou menos?

#Comparar cada coluna da minha base de dados com o meu cancelamento.

#Para saber se uma característica influencia na decisão de cancelar ou não.

#E com essas respostas será possível identificar as principais causas de cancelamentos.

#contando colunas, valores, também dá certo.

#Entretanto, utilizar gráficos facilitam visualmente.

importar plotly.express as px

#é legal olhar a documentação, por que possui as funcionalidades.

#passo 1: criação de gráfico

grafico = px.histogram(tabela, x = "idade")

#as faixas etárias, e quantos clientes tem uma determinada faixa etária.

#mostra a qtd de valores de cada uma das faixas, a qtd de clientes que possuem uma caracteristica.

#quero saber quantos cluentes com menos de 5o anos cancelam, quero fazer uma diferenciação de cor de acordo com a coluna canccel, quem canccelou uma cor e quem não cancelou outra cor.

grafico = px.histogram(tabela, x = "idade", color="cancelou")

grafico.show()

#não coloque muitas informações, pois dificultará a análise. Simples é melhor.

#grafico -> eixo x e eixo y, y qtd de valores, x o que queremos exibir, qualo coluna da tabela vc quer ver.

#passar outos padrões de cores

grafico = px.histogram(tabela, x = "idade", color="cancelou", color_discrete_sequence="")

#e se queisesse fazer com outras

coluna = "assinatura"

grafico = px.histogram(tabela, x = coluna, color="cancelou")

#de forma dinâmica

#para cada coluna nas colunas da minha tabela

#tabela.columns lista de colunas da tabela

for coluna in tabela.columns:

      grafico = px.histogram(tabela, x = coluna          color="cancelou")

#ccria todos os gráficos

#passo 2: Exibir gráfico

grafico. show()

#analise das causas de cancelamentos

#olhar todos os gráficos e buscar informações que saltam aos olhos. Exemplo ligações cancelar, o gráfico mostra qtd de clientes e ligações em relação aos que cancelaram ou não, todos os clientes que fizeram mais de 4 ligações cancelaram o serviço.

#Dias de atraso de pagamento:

Se o cliente atrasa  o pagamento 3, 4 ou cinco dias, normal, mas se o cliente atrasa o pagamento 20 dias, todos cancelam.

#duracao_contrato

O pessoal do contrato anual, metade cancelou, metade não cancelou. Trimestral pouco mais da metade cancelou e vice versa, e a dos contratos mensais, absolutamente todos os clientes cancelaram.

#analise das causas de cancelamento

#Se um cliente ligar mais de 4 vezes para o call center, ele  cancela.

      #criar um processo que se um cliente ligou 3 vezes, a gente faz de tudo para resolver o  problema.

#Se um cliente atrasar o pagamento mais de cinco dias, ele cancela.

     #Criar um processo para não deixar o cliente atrasar o pagamento por mais de 20 dias. Se ele atrasar mais de 10, ainda existe uma margem de segurança. Todos os atrasos de pagamentos tem que ser resolvidos em até 10 dias.

#Todos os clientes do contrato mensal cancelam

      #Oferecer descontos no planos anuais e trimestrais, para evitar o uso do mensal e evitar os cancelamentos.

--------------

#Testes

--

O quanto essas informações impactam efetivamente?

---

Se eu não tivesse mais nenhum cliente ligando mais de 4 vezes para o call center, como iria ficar o meu percentual de cancelamento?
Se eu não tivesse nenhum cliente que atrasou 20 dias no pagamento, como teria ficado meu percentual de cancelamento?
Se eu não tivesse nenhum cliente no contrato mensal, como teria ficado o percentual de cancelamento?
Se eu resolver os problemas, como fica o percentual de cancelamento?
tabela = tabela #sem duração do contrato mensal

tabela = tabela #sem ligação do call center acima de 4  vezes

tabela = tabela #sem atraso de pag maior que 20 dias

#como filtrar a tabela?

tabela = tabela[condicao_de_filtramento]

#sem duração do contrato mensal

tabela = tabela[tabela["duracao_contrato"] != "Monthly"]

#tabela sem ligação do call center acima de 4  vezes

tabela = tabela[tabela["ligacoes_callcenter"] <= 4]

#tabela sem atraso de pag maior que 20 dias

tabela = tabela[tabela["dias_atraso"] <= 20]

display(tabela["cancelou"].value_counts(normalize=True)

#Mostra o percentual/taxa de cancelamentos sem esses problemas. "Olha, se resolvermos esses problemas, a taxa de cancelamentos cairia de (valor_anterior) para apenas 18%."





#Interpretando os gráficos:

- qtd de cancelamentos por sexo:

     existe uma qtd maior de assinantes do sexo masculino, e metade cancelou e metade não. No caso dos assinantes do sexo feminino. Mais da metade não cancelou, mais ou menos 1/3 cancelou.

- Tempo como cliente e cancelamento:

     #1-  cancel 0- não cancelou

     #Não há uma mudança drática.

- Frquencia de uso influencia no cancelamento?

    #Sem dados saltantes

-Numero de Ligações ao call center influencia no cancelamento?

    #Quando passa de 4 ligações, todos cancelam

- Dias de atraso de pag. Influência no cancel.?

   #A partir de 20 dias de atraso, todos cancelam.

- A assinatura influência no cancelamento?

   #Não possui dados saltantes.

- A duração de contrato influência no cancelamento?

  #Todos que possuem duração de contrato Mensal, cancelam.

- Os meses de ultima interação influenciam no cancelamento?

  #Mais de 15 meses começam a cancelar mais.

display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))




















































