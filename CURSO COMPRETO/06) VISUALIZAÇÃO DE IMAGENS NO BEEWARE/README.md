# VISUALIZAÇÃO DE IMAGENS NO BEEWARE
Para exibir imagens em uma aplicação BeeWare usando o Toga, você pode usar o widget `toga.Image`. Aqui está um exemplo simples de como exibir uma imagem em uma janela:

```python
import toga

def build(app):
    # Caminho para a imagem (substitua pelo caminho real da sua imagem)
    image_path = 'caminho/para/sua/imagem.jpg'

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
```

Neste exemplo:

- Substitua `'caminho/para/sua/imagem.jpg'` pelo caminho real da sua imagem.
- Um botão é criado na janela principal, e quando você pressiona o botão, ele chama a função `display_image`, que cria uma nova janela contendo a imagem usando `toga.ImageView`.

Certifique-se de substituir o caminho da imagem pelo caminho real da imagem que você deseja exibir.

Lembre-se de que a exibição de imagens pode variar dependendo do backend gráfico que você está usando. Se você estiver enfrentando problemas específicos ou precisar de mais funcionalidades, consulte a documentação do Toga para obter detalhes específicos do widget de imagem e possíveis considerações de compatibilidade: [Documentação do Toga](https://toga.readthedocs.io).