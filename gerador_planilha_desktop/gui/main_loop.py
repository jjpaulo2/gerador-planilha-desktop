import PySimpleGUIQt as sg
from ..gerador_planilha import generate_worksheet

def main_loop(window: sg.Window):
    """
    Função que executa o loop principal da janela da aplicação.

    Arguments:
        window (sg.Window): objeto de janela do PySimpleGUI
    """
    while True:
        event, values = window.read()

        if event == 'Gerar planilha':
            input_file = values['_FILE_INPUT_']
            output_file = values['_FILE_OUTPUT_']

            try:
                if output_file[-5:] != '.xlsx':
                    output_file += '.xlsx'

                generate_worksheet(input_file, output_file, window=window)
                print()
                window.refresh()

            except Exception as exc:
                sg.Popup(str(exc), title='Erro ao tentar executar')
                sg.Popup('Garanta que você tenha selecionado uma planilha no formato\ncorreto e tenha selecionado um local adequado para salvar a\nplanilha que será gerada.', title='Dica')

        
        if (event == sg.WINDOW_CLOSED) or (event == 'Quit'):
            break

        window.refresh()