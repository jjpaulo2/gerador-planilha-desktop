from typing import Any
import PySimpleGUIQt

def get_layout(styles: Any, sg: PySimpleGUIQt) -> list:
    """
    Função que retorna o layout utilizado na janela da aplicação.

    Argurments:
        styles (Any): módulo/arquivo com os atributos de estilo
        sg (PySimpleGUIQt): módulo PySimpleGUIQt

    Return:
        list: matriz com o layout do PySimpleGUI
    """
    return [
        [sg.Text(' Selecione o arquivo de planilha do Excel para análise', **styles.text_style)],
        [sg.InputText('C:\\', enable_events=True, **styles.file_name_input_style), sg.FileBrowse(**styles.file_browse_style)],
        [sg.Text('')],
        [sg.Text(' Selecione o lugar onde o novo arquivo será salvo', **styles.text_style)],
        [sg.InputText('C:\\planilha-final.xlsx', enable_events=True, **styles.file_name_output_style), sg.FileSaveAs(**styles.file_save_style)],
        [sg.Text(''), sg.Text(''), sg.Button('Gerar planilha', **styles.generate_button_style)],
        [sg.Text('')],
        [sg.Output()],
        [sg.Text('')],
        [sg.Text('gerador-planilha-desktop © 2021, desenvolvido por João Paulo Carvalho')]
    ]