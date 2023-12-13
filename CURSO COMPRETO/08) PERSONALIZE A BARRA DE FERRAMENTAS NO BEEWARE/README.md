# PERSONALIZE A BARRA DE FERRAMENTAS NO BEEWARE
A personalização da barra de ferramentas no BeeWare, usando a biblioteca Toga, envolve a criação de uma instância da classe `toga.Group` e a adição de botões a essa instância. Aqui está um exemplo básico de como personalizar a barra de ferramentas:

```python
import toga

def build(app):
    # Função para manipular a ação do botão 1
    def acao_botao1(widget):
        app.info_dialog('Ação do Botão 1', 'Botão 1 pressionado!')

    # Função para manipular a ação do botão 2
    def acao_botao2(widget):
        app.info_dialog('Ação do Botão 2', 'Botão 2 pressionado!')

    # Criação da barra de ferramentas
    barra_de_ferramentas = toga.Group('Minha Barra de Ferramentas')

    # Criação de botões para adicionar à barra de ferramentas
    botao1 = toga.Button('Botão 1', on_press=acao_botao1)
    botao2 = toga.Button('Botão 2', on_press=acao_botao2)

    # Adição dos botões à barra de ferramentas
    barra_de_ferramentas.add(botao1)
    barra_de_ferramentas.add(botao2)

    # Criação da caixa principal da janela
    box = toga.Box()

    # Adição da barra de ferramentas à caixa
    box.add(barra_de_ferramentas)

    # Criação da janela principal
    main_window = toga.MainWindow(title='Personalizando Barra de Ferramentas', size=(300, 200))
    main_window.content = box

    return main_window

if __name__ == '__main__':
    app = toga.App('Exemplo de Barra de Ferramentas', 'org.example.toolbarcustomization', startup=build)
    app.main_loop()
```

Neste exemplo:

- Criamos duas funções (`acao_botao1` e `acao_botao2`) que serão chamadas quando os botões 1 e 2, respectivamente, forem pressionados.
- Criamos uma instância da classe `toga.Group` chamada `barra_de_ferramentas`.
- Criamos dois botões (`botao1` e `botao2`) e os adicionamos à `barra_de_ferramentas` usando o método `add`.
- Adicionamos a `barra_de_ferramentas` à caixa principal da janela.

Quando você executa este exemplo, verá uma janela com uma barra de ferramentas contendo dois botões. Quando você pressiona um dos botões, a função associada a esse botão é chamada.

Você pode personalizar ainda mais a barra de ferramentas adicionando mais botões, agrupando-os ou usando outros widgets conforme necessário para atender às necessidades específicas do seu aplicativo.