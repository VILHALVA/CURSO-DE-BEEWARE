from codigo.app import main
import toga
from datetime import datetime

def build(app):
    # Função para lidar com a mudança de data no seletor de data
    def on_data_selecionada(widget, data):
        app.info_dialog('Data Selecionada', f'Data Selecionada: {data}')

    # Criação do seletor de data
    seletor_de_data = toga.DatePicker('Seletor de Data', on_select=on_data_selecionada)

    # Criação da caixa principal da janela
    box = toga.Box()

    # Adição do seletor de data à caixa
    box.add(seletor_de_data)

    # Criação da janela principal
    main_window = toga.MainWindow(title='Seletor de Data no BeeWare', size=(300, 200))
    main_window.content = box

    return main_window

if __name__ == '__main__':
    app = toga.App('Exemplo de Seletor de Data', 'org.example.datepickerexample', startup=build)
    app.main_loop()
