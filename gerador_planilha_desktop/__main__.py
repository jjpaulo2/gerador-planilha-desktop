"""
Quando o módulo `gerador-planilha-desktop` for chamado
será executado o método __main__ do módulo `gui`.
"""
from .gui.__main__ import main

from .gui import layout
from .gui import styles
from .gui import main_loop

if __name__ == '__main__':
    # EXECUTANDO O MÓDULO
    main(styles, layout, main_loop)
