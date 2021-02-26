"""
Arquivo executado ao chamar o comando
    $ python -m gui
"""
import PySimpleGUIQt as sg

from typing import Any

from . import styles
from . import layout
from . import main_loop

def main(styles: Any, layout: Any, main_loop: Any):
    """
    Método principal do módulo.

    Arguments:
        styles (file): python file containing style variables
        layout (file): python file containing layout constructors
        main_loop (file): python file containing window main loop
    """
    sg.theme('Default1')

    layout = layout.get_layout(styles, sg)
    window = sg.Window('Gerador planilha', layout, size=(600,400), resizable=True, icon='gui/src/icon.png')
    main_loop.main_loop(window)

    window.close()


if __name__ == '__main__':
    # EXECUTANDO O MÓDULO
    main(styles, layout, main_loop)