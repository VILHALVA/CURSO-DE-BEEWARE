# SINTAXE:
Vou criar um exemplo simples de código usando o framework BeeWare. Neste exemplo, criaremos uma aplicação de desktop usando a biblioteca Toga para exibir uma janela com um botão. Quando o botão for clicado, exibiremos uma mensagem de saudação.

```python
import toga

def button_handler(widget):
    # Função chamada quando o botão é clicado
    print("Olá, Mundo!")

def build_app():
    # Criação da aplicação
    app = toga.App('Saudação', 'org.example.saudacao')

    # Definição da interface de usuário
    box = toga.Box()
    button = toga.Button('Clique-me!', on_press=button_handler)
    box.add(button)

    # Adiciona o widget à janela principal
    app.main_window.content = box

    return app

if __name__ == '__main__':
    # Inicializa e executa a aplicação
    app = build_app()
    app.main_loop()
```

Agora, vamos explicar o que cada parte deste código faz:

1. Importamos o módulo `toga`, que é parte do framework BeeWare, responsável por criar interfaces gráficas de usuário multiplataforma.

2. Definimos uma função `button_handler(widget)` que será chamada quando o botão for clicado. Neste exemplo, ela simplesmente imprime "Olá, Mundo!" no console.

3. Definimos a função `build_app()`, que é responsável por criar e configurar a aplicação. Dentro desta função:
   - Criamos uma instância da classe `toga.App`, que representa a aplicação.
   - Criamos uma caixa (`Box`) que será o contêiner principal para os widgets da interface de usuário.
   - Criamos um botão (`Button`) com o texto "Clique-me!" e atribuímos a função `button_handler` ao evento de pressionar o botão.
   - Adicionamos o botão à caixa.
   - Definimos a caixa como o conteúdo da janela principal da aplicação.

4. No bloco `if __name__ == '__main__':`, verificamos se o script está sendo executado como o programa principal. Se sim, criamos uma instância da aplicação chamando a função `build_app()` e iniciamos o loop principal da aplicação com o método `main_loop()`.

Ao executar este código, uma janela de aplicativo será exibida com um botão. Quando o botão for clicado, a mensagem "Olá, Mundo!" será exibida no console. Este é um exemplo simples de como criar uma aplicação de desktop usando o framework BeeWare.