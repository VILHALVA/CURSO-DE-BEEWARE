# FUNÇÃO COM PARÂMETRO NO BEEWARE
Para criar uma função com parâmetros no BeeWare usando a biblioteca Toga, você pode seguir uma abordagem semelhante à criação de funções em Python padrão. Aqui está um exemplo simples:

```python
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
```

Neste exemplo:

- Criamos uma função chamada `exibir_mensagem` que recebe dois parâmetros (`widget` e `mensagem`).
- Dentro da função, usamos `app.info_dialog` para exibir uma caixa de diálogo informativa com a mensagem fornecida.
- Criamos um botão chamado 'Clique-me' que, quando pressionado, chama a função `exibir_mensagem` e passa a mensagem 'Olá, Mundo!' como um parâmetro.

Ao executar este exemplo, você verá uma janela com um botão. Quando você clicar no botão, uma caixa de diálogo será exibida com a mensagem 'Olá, Mundo!'.

Você pode adaptar essa estrutura para criar funções com quantos parâmetros forem necessários para as suas necessidades específicas. Certifique-se de ajustar os parâmetros da função e os argumentos passados ao chamar a função conforme necessário para o seu aplicativo.