# SELETOR DE DATA NO BEEWARE
Para adicionar um seletor de data (date picker) em um aplicativo BeeWare usando a biblioteca Toga, você pode utilizar o widget `DatePicker`. Aqui está um exemplo básico:

```python
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
```

Neste exemplo:

- Importamos a classe `toga.DatePicker` para criar um seletor de data.
- Criamos uma função chamada `on_data_selecionada` que será chamada quando a data for selecionada no seletor.
- Criamos uma instância de `toga.DatePicker` chamada `seletor_de_data` e a adicionamos à caixa principal da janela.
- Ao selecionar uma data no seletor, a função `on_data_selecionada` será chamada e exibirá uma caixa de diálogo informativa com a data selecionada.

Ao executar este exemplo, você verá uma janela com um seletor de data. Quando você seleciona uma data, a função associada ao evento de seleção será chamada.

Este é apenas um exemplo básico, e você pode personalizar ainda mais o comportamento e a aparência do seletor de data conforme necessário para atender às suas necessidades específicas.