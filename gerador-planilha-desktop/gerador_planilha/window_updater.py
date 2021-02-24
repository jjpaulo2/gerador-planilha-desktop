def update(window=None):
    """
    Função que atualiza a tela, caso o objeto de janela
    seja passado como parâmetro.

    Arguments:
        window: objeto de janela do PySimpleGUI
    """
    if window is not None:
        window.refresh()