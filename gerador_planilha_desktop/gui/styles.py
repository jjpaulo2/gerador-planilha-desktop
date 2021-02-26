"""
Arquivo com dicionários contendo valores de estilo para serem
desempacotados nos widgets da tela.
"""

# BOTÃO QUE SELECIONA ARQUIVO DE ENTRADA
file_browse_style = {
    'button_text': 'Navegar',
    'font': 'Arial 11',
    'size': (15, 1),
    'file_types': (("Planilha do Excel [.xlsx]", "*.xlsx"),),
    'target': '_FILE_INPUT_'
}

# BOTÃO QUE SELECIONA ONDE SERÁ SALVO O ARQUIVO DE SAÍDA
file_save_style = {
    'button_text': 'Navegar',
    'font': 'Arial 11',
    'size': (15, 1),
    'file_types': (("Planilha do Excel [.xlsx]", ".xlsx"),),
    'target': '_FILE_OUTPUT_'
}

# BOTÃO QUE GERA O ARQUIVO DE SAÍDA
generate_button_style = {
    'font': 'Arial 11',
    'size': (15, 1)
}

# CAMPO QUE MOSTRA O CAMINHO DO ARQUIVO DE ENTRADA
file_name_input_style = {
    'size': (50, 1),
    'font': 'Arial 11',
    'key': '_FILE_INPUT_'
}

# CAMPO QUE MOSTRA O CAMINHO DO ARQUIVO DE SAÍDA
file_name_output_style = {
    'size': (50, 1),
    'font': 'Arial 11',
    'key': '_FILE_OUTPUT_'
}

# TEXTO GERAL DA JANELA
text_style = {
    'font': 'Arial 11'
}