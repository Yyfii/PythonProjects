import flet as ft
#passo a passo
#- Titulo

# Botão de iniciar chat

# - clicou no botão

#--pop-up/modal

#---Titulo: Bem vindo

#---Campo escreva seu no chat

#----Botão entrar no chat
#-Chat

#-embaixo do chat:

#--campo de Digite sua msg

#--botão de enviar


def main(pagina):
    texto = ft.Text("ChinguHi!")
    chat = ft.Column()


    def enviar_msg_tunel(msg):
        text_msg = ft.Text(msg)
        chat.controls.append(text_msg)
        pagina.update()


    pagina.pubsub.subscribe(enviar_msg_tunel)

    def enviar_msg(evento):
        pagina.pubsub.send_all(f"{nome_usuario.value} : {campo_msg.value}")
        texto_msg = ft.Text(campo_msg.value)
        #chat.controls.append(texto_msg)
        campo_msg.value = ""
        pagina.update()

    campo_msg = ft.TextField(label="Digite sua mensagem", on_submit=enviar_msg)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_msg) 
    linha_enviar = ft.Row([campo_msg, botao_enviar])

    def entrar_chat(evento):
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.add(chat)       
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        pagina.add(linha_enviar)
 
        pagina.update()

    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    titulo_popup = ft.Text(f"Bem vindo ao {texto.value}")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()


    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)


ft.app(target=main, view=ft.WEB_BROWSER)
