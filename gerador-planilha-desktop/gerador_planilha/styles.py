from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font, Fill

border_side_thin = Side(style='thin')
border_side_dashed = Side(style='dashed')

# *
# Objetos de estilo do conteúdo formatado
# *

content_align_center = Alignment(
    wrap_text=True,
    horizontal='center',
    vertical='center'
)

content_align_no_center = Alignment(
    wrap_text=True
)

content_border = Border(
    top=None,
    left=border_side_dashed,
    right=border_side_dashed,
    bottom=border_side_dashed
)


# *
# Objetos de estilo dos títulos das colunas
# *

title_columns = (
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

title_column_font = Font(
    name='Arial',
    size=11,
    bold=True,
    vertAlign='baseline',
    italic=False,
    underline=None,
)

title_column_alignment = Alignment(
    horizontal='center',
    vertical='center'
)

title_column_fill = PatternFill(
    fill_type = 'solid',
    start_color='ffff87',
    end_color='ffff87'
)

title_column_border = Border(
    left=border_side_thin,
    right=border_side_thin,
    top=border_side_thin,
    bottom=border_side_thin
)
