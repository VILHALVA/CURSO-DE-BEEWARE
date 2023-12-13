# SLIDER NO BEEWARE
Para adicionar um controle deslizante (slider) em um aplicativo BeeWare usando a biblioteca Toga, você pode utilizar o widget `Slider`. Aqui está um exemplo básico:

```python
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
```

Neste exemplo:

- Importamos a classe `toga.Slider` para criar um controle deslizante.
- Criamos uma função chamada `on_valor_alterado` que será chamada quando o valor do controle deslizante for alterado.
- Criamos uma instância de `toga.Slider` chamada `slider` e a adicionamos à caixa principal da janela.
- Ao alterar o valor no controle deslizante, a função `on_valor_alterado` será chamada e exibirá uma caixa de diálogo informativa com o novo valor.

Ao executar este exemplo, você verá uma janela com um controle deslizante. Ao mover o controle deslizante, a função associada ao evento de alteração será chamada, e uma caixa de diálogo informativa exibirá o novo valor.

Este é apenas um exemplo básico, e você pode personalizar ainda mais o comportamento e a aparência do controle deslizante conforme necessário para atender às suas necessidades específicas.