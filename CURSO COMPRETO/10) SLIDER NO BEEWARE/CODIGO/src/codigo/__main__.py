from codigo.app import main
import toga

def build(app):
    # Função para lidar com a mudança de valor no controle deslizante
    def on_valor_alterado(widget, valor):
        app.info_dialog('Valor Alterado', f'Novo Valor: {valor}')

    # Criação do controle deslizante
    slider = toga.Slider(on_change=on_valor_alterado)

    # Criação da caixa principal da janela
    box = toga.Box()

    # Adição do controle deslizante à caixa
    box.add(slider)

    # Criação da janela principal
    main_window = toga.MainWindow(title='Controle Deslizante no BeeWare', size=(300, 200))
    main_window.content = box

    return main_window

if __name__ == '__main__':
    app = toga.App('Exemplo de Controle Deslizante', 'org.example.sliderexample', startup=build)
    app.main_loop()
