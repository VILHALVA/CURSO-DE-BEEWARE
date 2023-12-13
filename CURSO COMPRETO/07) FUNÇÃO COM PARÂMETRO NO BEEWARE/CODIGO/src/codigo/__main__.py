from codigo.app import main
import toga

def build(app):
    # Criação de uma função com parâmetro
    def exibir_mensagem(widget, mensagem):
        app.info_dialog('Mensagem', mensagem)

    # Criação de um botão que chama a função com parâmetro
    button = toga.Button('Clique-me', on_press=lambda widget: exibir_mensagem(widget, 'Olá, Mundo!'))

    # Criação da caixa principal da janela
    box = toga.Box()
    box.add(button)

    # Criação da janela principal
    main_window = toga.MainWindow(title='Função com Parâmetro', size=(300, 200))
    main_window.content = box

    return main_window

if __name__ == '__main__':
    app = toga.App('Exemplo de Função com Parâmetro', 'org.example.parameterexample', startup=build)
    app.main_loop()
