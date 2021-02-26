from .reader import read_and_format_workbook_to_row_list
from . import writer


def generate_worksheet(input_file: str, output_file: str, window=None):
    """
    Função que executa o procedimento do módulo em ordem lógica.
    É o método chamado no arquivo `__main__.py`.

    Arguments:
        input_file (str): string com o caminho do arquivo de entrada
                          que será lido
        output_file (str): string com o caminho do arquivo de saída que 
                           conterá os dados extraídos do arquivo inicial
    """
    formated = read_and_format_workbook_to_row_list(input_file, window=window)
    writer.generate_workbook_file(formated, output_file, window=window)