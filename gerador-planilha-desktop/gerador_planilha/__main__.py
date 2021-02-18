"""
Arquivo principal do módulo, invocado quando se executa
    $ python -m gerador_planilha
"""
from .reader import read_and_format_workbook
from pprint import pprint

formated = read_and_format_workbook('arquivo-utilizavel.xlsx')
