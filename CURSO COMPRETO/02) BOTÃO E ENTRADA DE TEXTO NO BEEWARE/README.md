# BOTÃO E ENTRADA DE TEXTO NO BEEWARE
## INTRODUÇÃO:
No BeeWare, especialmente quando você está trabalhando com o Toga para criar interfaces de usuário, adicionar botões e entradas de texto é relativamente simples. Aqui está um exemplo básico que demonstra como criar uma janela com um botão e uma entrada de texto usando o Toga:

```python
import toga

def button_handler(widget):
    entrada_texto.value = "Olá, " + entrada_texto.value

def build(app):
    # Cria uma caixa para organizar os widgets
    box = toga.Box()

    # Cria um campo de entrada de texto
    global entrada_texto
    entrada_texto = toga.TextInput()

    # Cria um botão com um manipulador de evento associado
    button = toga.Button('Clique-me', on_press=button_handler)

    # Adiciona os widgets à caixa
    box.add(entrada_texto)
    box.add(button)

    # Retorna a caixa como a principal janela do aplicativo
    return box

if __name__ == '__main__':
    # Cria o aplicativo
    app = toga.App('MeuApp', 'org.example.meuapp', startup=build)

    # Inicia o loop principal do aplicativo
    app.main_loop()
```

Explicação do código:

- `toga.TextInput()`: Cria um campo de entrada de texto.
- `toga.Button('Clique-me', on_press=button_handler)`: Cria um botão com o rótulo "Clique-me" e associa o manipulador de evento `button_handler` ao evento de pressionar o botão.
- `box.add(entrada_texto)`: Adiciona o campo de entrada de texto à caixa (contêiner).
- `box.add(button)`: Adiciona o botão à caixa.
- `entrada_texto.value`: Acessa ou define o valor atual do campo de entrada de texto.
- `on_press=button_handler`: Define a função `button_handler` como o manipulador de eventos quando o botão é pressionado.

Este é um exemplo muito simples. Você pode estilizar e organizar os widgets de acordo com as necessidades do seu aplicativo. O Toga fornece uma variedade de widgets e layouts para criar interfaces de usuário mais complexas. Consulte a documentação oficial do Toga para obter informações mais detalhadas e recursos adicionais: [Documentação do Toga](https://toga.readthedocs.io).

## TIPOS E PROPRIEDADES:
No Toga, um framework dentro do projeto BeeWare para criar interfaces de usuário multiplataforma em Python, existem vários tipos de botões com diferentes propriedades. Vamos explorar alguns dos tipos comuns e suas propriedades associadas.

### Tipos Comuns de Botões no Toga:
1. **toga.Button:**
   - **Propriedades Relevantes:**
     - `label`: O rótulo exibido no botão.
     - `on_press`: Um manipulador de eventos chamado quando o botão é pressionado.
     - `enabled`: Indica se o botão está habilitado ou desabilitado.

   ```python
   button = toga.Button('Clique-me', on_press=button_handler, enabled=True)
   ```

2. **toga.Command:**
   - É um botão especializado usado para representar comandos em uma aplicação.

   ```python
   command = toga.Command('Salvar', action=save_action)
   ```

### Propriedades Gerais dos Botões no Toga:
1. **`label` (rótulo):**
   - Define o texto exibido no botão.

   ```python
   button.label = 'Novo Texto'
   ```

2. **`enabled` (habilitado):**
   - Controla se o botão está habilitado ou desabilitado. Quando desabilitado, o botão não responde a eventos.

   ```python
   button.enabled = False
   ```

3. **`on_press` (ao pressionar):**
   - Um manipulador de eventos chamado quando o botão é pressionado.

   ```python
   def button_handler(widget):
       print("Botão pressionado!")

   button = toga.Button('Clique-me', on_press=button_handler)
   ```

4. **`style` (estilo):**
   - Permite a definição de estilos específicos para o botão, como cor de fundo, margens, etc.

   ```python
   button.style.set(background_color='red', padding_left=10)
   ```

5. **`icon` (ícone):**
   - Permite adicionar um ícone ao botão.

   ```python
   button.icon = 'path/do/seu/icone.png'
   ```

6. **`tooltip` (dica de ferramenta):**
   - Adiciona uma dica de ferramenta ao botão.

   ```python
   button.tooltip = 'Clique aqui para fazer alguma coisa'
   ```

Essas são apenas algumas das propriedades mais comuns associadas aos botões no Toga. A documentação oficial do Toga fornecerá detalhes mais abrangentes sobre as propriedades e métodos disponíveis: [Documentação do Toga](https://toga.readthedocs.io).