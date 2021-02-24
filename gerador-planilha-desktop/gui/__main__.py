"""
Arquivo executado ao chamar o comando
    $ python -m gui
"""
import PySimpleGUIQt as sg

from . import styles
from . import layout
from . import main_loop

sg.theme('Default1')

layout = layout.get_layout(styles, sg)
window = sg.Window('Gerador planilha', layout, size=(600,400), resizable = False, icon='gui/src/icon.png')
main_loop.main_loop(window)

window.close()