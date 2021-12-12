# help data frame can show side by side 
from IPython.display import display,HTML
import pandas as pd

# let data frame display flexible, show whole value in cell
def grid_df_display(list_df, list_df_name, list_number_of_data, row = 1, col=1, fill = 'cols'):
    html_table = "<table style='width:100%; border:0px'>{content}</table>"
    html_row = "<tr style='border:0px'>{content}</tr>"
    html_cell = "<td style='width:{width}%;vertical-align:top;border:0px'>{{content}}</td>"
    html_cell = html_cell.format(width=100/col)
    
    li = []
    for i in range(len(list_df)):
        li.append(list_df[i].head(list_number_of_data[i]).
                  style.set_table_attributes("style='display:inline'").
                  set_caption(f'<b><H2>{list_df_name[i]}<H2></b>')
                 )
    
    
    cell = [ html_cell.format(content=df.render()) for df in li[:row*col] ]
    cell += col * [html_cell.format(content="")] # pad

    if fill == 'row': #fill in rows first (first row: 0,1,2,... col-1)
        grid = [ html_row.format(content="".join(cell[i:i+col])) for i in range(0,row*col,col)]

    if fill == 'col': #fill columns first (first column: 0,1,2,..., rows-1)
        grid = [ html_row.format(content="".join(cell[i:row*col:row])) for i in range(0,row)]
    
    display(HTML(html_table.format(content="".join(grid))))
    
    
def check_nan_by_row(df: pd.DataFrame, col):
    """
    input:
    df -- dataframe
    col -- col we want to check
    output:
    dataframe -- each row which value cantains NaN or None
    """
    is_nan = df[col].isnull()
    row_has_nan = is_nan.any(axis=1)
    if sum(row_has_nan)==0:
        print('There is no NaN in dataframe.')
    else:
        return df[col][row_has_nan]