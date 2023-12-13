from codigo.app import main
import toga

def button_handler(widget):
    entrada_texto.value = "Olá, " + entrada_texto.value

def build(app):
    # Cria uma caixa para organizar os widgets
    box = toga.Box()

    # Cria um campo de entrada de texto
    global entrada_texto
    entrada_texto = toga.TextInput()

    # Cria um botão com um manipulador de evento associado
    button = toga.Button('Clique-me', on_press=button_handler)

    # Adiciona os widgets à caixa
    box.add(entrada_texto)
    box.add(button)

    # Retorna a caixa como a principal janela do aplicativo
    return box

if __name__ == '__main__':
    # Cria o aplicativo
    app = toga.App('MeuApp', 'org.example.meuapp', startup=build)

    # Inicia o loop principal do aplicativo
    app.main_loop()


