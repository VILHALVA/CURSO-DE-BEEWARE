# MANUAL:
## CRIANDO PROJETO:
Para criar um projeto utilizando o BeeWare, você pode seguir estes passos:

### PASSO 1: INSTALAR O BEEWARE:
Você pode instalar o BeeWare usando o pip (gerenciador de pacotes Python). Execute o seguinte comando em seu terminal ou prompt de comando:

```bash
pip install briefcase
```

### PASSO 2: INICIALIZAR UM NOVO PROJETO BEEWARE:
Depois de instalar o BeeWare, você pode inicializar um novo projeto BeeWare usando o Briefcase, que é uma ferramenta para construir, empacotar e distribuir aplicativos Python multiplataforma. No terminal, navegue até o diretório onde deseja criar seu projeto e execute o seguinte comando:

```bash
briefcase new
```

Isso iniciará um assistente interativo que o guiará na criação de um novo projeto BeeWare. Você precisará fornecer informações como o nome do projeto, o nome do aplicativo e o tipo de aplicativo (por exemplo, "console" para um aplicativo de console ou "gui" para um aplicativo com interface gráfica).

### PASSO 3: DESENVOLVER SEU APLICATIVO:
Após a criação do projeto, você encontrará uma estrutura de diretórios básica que contém os arquivos necessários para o seu aplicativo. Dependendo do tipo de aplicativo que você escolheu (console ou GUI), você poderá começar a desenvolver seu aplicativo Python dentro desses arquivos.

### EXEMPLO DE CÓDIGO:
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

### PASSO 4: COMPILAR E EXECUTAR SEU APLICATIVO:
Após desenvolver seu aplicativo, você pode usar o Briefcase para compilar e executar seu aplicativo para diferentes plataformas. Por exemplo, para compilar e executar um aplicativo GUI para Windows, você pode usar o seguinte comando:

```bash
briefcase dev
```

Este comando compilará e executará o aplicativo em sua plataforma local. 

### PASSO 5: EMPACOTAR E DISTRIBUIR PARA OUTRAS PLATAFORMAS:
Para distribuir o aplicativo para outras plataformas, como Windows, macOS, iOS ou Android, o Briefcase oferece suporte para criar pacotes e instaladores adequados para cada plataforma. Dependendo da plataforma de destino, você pode usar os comandos apropriados:

- **Para Windows:**
  ```bash
  briefcase package
  ```
  Este comando cria um instalador executável para Windows que pode ser distribuído e instalado em sistemas Windows.

- **Para macOS:**
  ```bash
  briefcase package
  ```
  Similar ao Windows, este comando cria um pacote de aplicativo `.app` que pode ser distribuído para usuários macOS.

- **Para iOS:**
  ```bash
  briefcase package --ios
  ```
  Este comando cria um pacote Xcode que pode ser compilado e instalado em dispositivos iOS.

- **Para Android:**
  ```bash
  briefcase package --android
  ```
  Este comando cria um pacote Android que pode ser instalado em dispositivos Android ou distribuído via Google Play Store.

