"""
Script que executa o módulo `gerador_planilha_desktop`.
"""
from gerador_planilha_desktop.gui.__main__ import main

from gerador_planilha_desktop.gui import layout
from gerador_planilha_desktop.gui import styles
from gerador_planilha_desktop.gui import main_loop

if __name__ == '__main__':
    # EXECUTANDO O MÓDULO
    main(styles, layout, main_loop)