"""
Arquivo principal do módulo, invocado quando se executa
    $ python -m gerador_planilha
"""
from .reader import read_and_format_workbook_to_row_list
from . import writer
from pprint import pprint

formated = read_and_format_workbook_to_row_list('arquivo-utilizavel.xlsx')
writer.generate_workbook_file(formated, 'teste.xlsx')