from codigo.app import main
import os
import toga

def build(app):
    # Caminho para a imagem (substitua pelo caminho real da sua imagem)
    image_filename = 'BeeWare.png'
    image_path = os.path.abspath(image_filename)

    # Cria um widget de imagem
    image = toga.Image(image_path)

    # Cria um botão que exibe a imagem ao ser pressionado
    button = toga.Button('Exibir Imagem', on_press=lambda widget: display_image(image))

    # Cria a caixa principal da janela
    box = toga.Box()
    box.add(button)

    # Cria a janela principal
    main_window = toga.MainWindow(title='Exibição de Imagem', size=(300, 200))
    main_window.content = box

    return main_window

def display_image(image):
    # Cria uma nova janela para exibir a imagem
    image_window = toga.Window('Imagem', size=(400, 400))

    # Adiciona a imagem à nova janela
    image_view = toga.ImageView(image)
    image_window.content = image_view

    # Exibe a nova janela
    image_window.show()

if __name__ == '__main__':
    app = toga.App('Exemplo de Imagem', 'org.example.imageexample', startup=build)
    app.main_loop()
