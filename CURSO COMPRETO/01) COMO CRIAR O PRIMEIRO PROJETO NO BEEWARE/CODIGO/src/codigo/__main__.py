from codigo.app import main

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
    main().main_loop()
