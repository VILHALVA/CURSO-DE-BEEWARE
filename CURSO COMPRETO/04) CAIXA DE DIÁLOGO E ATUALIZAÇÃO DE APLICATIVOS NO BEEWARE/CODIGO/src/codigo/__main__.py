from codigo.app import main
import toga

def show_dialog(widget):
    # Cria uma janela secundária
    window = toga.Window('Minha Caixa de Diálogo', size=(300, 200))

    # Adiciona um botão de fechar à janela secundária
    button = toga.Button('Fechar', on_press=window.close)
    window.content = button

    # Mostra a janela secundária
    window.show()

def build(app):
    box = toga.Box()

    # Cria um botão que mostra a caixa de diálogo
    button = toga.Button('Mostrar Caixa de Diálogo', on_press=show_dialog)
    box.add(button)

    return box

if __name__ == '__main__':
    app = toga.App('MeuApp', 'org.example.meuapp', startup=build)
    app.main_loop()
