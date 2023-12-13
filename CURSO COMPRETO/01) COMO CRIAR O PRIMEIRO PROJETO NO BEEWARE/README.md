# COMO CRIAR O PRIMEIRO PROJETO NO BEEWARE?
Para criar o seu primeiro projeto no BeeWare usando o Toga, você pode seguir os passos abaixo. Este guia assume que você já tenha o Python e o pip instalados na sua máquina. Caso não tenha, é recomendável instalá-los antes de começar.

**Passo 1: Instalação do Toga e Briefcase**

Abra o terminal e execute os seguintes comandos para instalar o Toga e o Briefcase:

```bash
pip install toga
pip install briefcase
```

**Passo 2: Criação de um Novo Projeto**

Para criar um novo projeto Toga, execute o seguinte comando no terminal:

```bash
briefcase new
```

Você será solicitado a fornecer informações sobre o novo projeto, como nome, descrição e autor. Siga as instruções no terminal para concluir a configuração do projeto.

**Passo 3: Desenvolvimento do Aplicativo**

Navegue até o diretório do seu novo projeto:

```bash
cd SeuNomeDoProjeto
```

Abra o arquivo `main.py` no seu editor de texto favorito. Este arquivo contém o código inicial do seu aplicativo. Você pode começar a adicionar lógica ao seu aplicativo nesse arquivo.

Aqui está um exemplo básico de um aplicativo Toga:

```python
import toga

def build(app):
    box = toga.Box()

    button = toga.Button('Hello World!', on_press=button_handler)
    button.style.set(margin=20)
    box.add(button)

    return box

def button_handler(widget):
    print("Hello, World!")

if __name__ == '__main__':
    app = toga.App('MyFirstApp', 'org.example.myfirstapp', startup=build)
    app.main_loop()
```

**Passo 4: Execução do Aplicativo em Ambiente de Desenvolvimento**

Para testar seu aplicativo no ambiente de desenvolvimento, execute o seguinte comando no terminal dentro do diretório do seu projeto:

```bash
briefcase dev
```

Isso compilará seu aplicativo e o executará em uma janela de teste.

**Passo 5: Empacotamento e Distribuição**

Quando estiver pronto para distribuir seu aplicativo, você pode usar o Briefcase para empacotá-lo para a plataforma desejada (Windows, macOS, Linux, etc.). Execute o seguinte comando no terminal:

```bash
briefcase package
```

Os pacotes gerados podem ser distribuídos aos usuários finais.

Lembre-se de consultar a documentação oficial do BeeWare para obter informações mais detalhadas e personalizações específicas: [Documentação BeeWare](https://docs.beeware.org/en/latest/index.html).