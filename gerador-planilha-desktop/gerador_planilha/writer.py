
from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from typing import List


# *
# Funções que povoam/escrevem partes do arquivo de planilha
# *

def write_column_titles(workbook: Workbook) -> Workbook:
    """
    Função que escreve os títulos das colunas no objeto
    de livro de planilhas.

    Arguments:
        workbook (Workbook): objeto de livro de planilhas

    Return:
        Workbook: livro de planilhas com os títulos das colunas
    """
    sheet = workbook.active
    col_titles = (
        'nº',
        'GRUPO', 
        'OBRA', 
        'ANO', 
        'TIPO',
        'NÍVEL DA POLÍTICA',
        None, 
        'TIPO DE AVALIAÇÃO',
        'TIPO DE INDICADOR',
        'PERSPECTIVA DO INDICADOR',
        'VARIÁVEIS RELACIONADAS'
        )

    print('Gravando os títulos das colunas....')
    for col, col_title in enumerate(col_titles):
        sheet.cell(1, col + 1).value = col_title

    return workbook


def write_formated_data(workbook: Workbook, row_list: List[tuple]) -> Workbook:
    """
    Função que escreve os dados já no formato padrão no objeto
    de livro de planilhas.

    Arguments:
        workbook (Workbook): objeto de livro de planilhas
        row_list (List[tuple]): lista com as linhas formatadas

    Return:
        Workbook: livro de planilhas com os dados gravados
    """
    sheet = workbook.active

    print('Inserindo os dados no arquivo...')
    for row, row_content in enumerate(row_list):
        sheet.cell(row + 2, 1).value = row + 1

        for col, col_content in enumerate(row_content):
            sheet.cell(row + 2, col + 2).value = col_content

    return workbook


# *
# Funções que aplicam estilos ao arquivo de planilhas
# *

def style(workbook: Workbook) -> Workbook:
    """
    Função que aplica estilos nas células do objeto
    de livro de planilhas.

    Arguments:
        workbook (Workbook): objeto de livro de planilhas

    Return:
        Workbook: livro de planilhas estilizado
    """
    pass


# *
# Funções que aplicam preparam e geram o arquivo de planilhas
# *

def create_new_workbook_from_row_list(row_list: List[tuple]) -> Workbook:
    """
    Função que cria o objeto de livro de planilhas e executa as funções
    de povoamento e estilização em ordem lógica antes de exportar para um 
    arquivo.

    Arguments:
        row_list (List[tuple]): lista com as linhas formatadas

    Return:
        Workbook: livro de planilhas com os dados gravados e estilizados
    """
    workbook = Workbook()

    write_column_titles(workbook)
    write_formated_data(workbook, row_list)

    return workbook


def save_workbook_file(workbook: Workbook, filename: str):
    """
    Função que exporta um livro de planilhas para um arquivo
    no sistema de arquivos.

    Arguments:
        workbook (Workbook): livro de planilhas com os dados gravados e estilizados
        filename (str): caminho absoluto para o arquivo ou apenas nome,
                        caso o arquivo esteja na raiz do projeto
    """
    print('Salvando arquivo no sistema...')
    workbook.save(filename=filename)
    print('Arquivo salvo com sucesso!')


# *
# Funções que executam os passos de escrita em ordem lógica
# *

def generate_workbook_file(row_list: List[tuple], filename: str):
    """
    Função que executa todos os passos para gerar o arquivo
    de planilhas no sistema. Os passos são:
        - criar um objeto de planilha
        - gravar os dados no objeto
        - salvar o arquivo da planilha no sistema

    Arguments:
        row_list (List[tuple]): lista com as linhas formatadas
        filename (str): caminho absoluto para o arquivo ou apenas nome,
                        caso o arquivo esteja na raiz do projeto
    """
    workbook = create_new_workbook_from_row_list(row_list)
    save_workbook_file(workbook, filename)
