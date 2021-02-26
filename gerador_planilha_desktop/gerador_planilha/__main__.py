"""
Arquivo principal do módulo, invocado quando se executa
    $ python -m gerador_planilha
"""
from . import generate_worksheet

generate_worksheet('arquivo-utilizavel.xlsx', 'arquivo-final.xlsx')