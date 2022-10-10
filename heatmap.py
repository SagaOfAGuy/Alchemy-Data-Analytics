import typer
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from pylab import savefig
from rich import print

app = typer.Typer(rich_markup_mode="rich")

@app.command(help="[bold green]Creates[/bold green] Full Correlation Heatmap by GWP\n\nThis requires [bold red]FILENAME[/bold red] and [bold red]PICNAME[/bold red]")
def full_gwp_heatmap(
filename:str = typer.Argument(...,help="CSV Data File"), 
picname:str = typer.Argument(...,help="Correlation Matrix PNG image")):
    print("Processing Data...")
    # Pull in imputed dataset
    data = pd.read_csv(f'{filename}')

    # Exclude broker_id 
    data = data.loc[:, data.columns!='broker_id_id']
    data = data.loc[:, data.columns!='broker_name']


    # get the column values
    row_values = list(data.columns)

    # Grab column values that don't have GWP in the tick string
    not_gwp_rows = [i for i in row_values if "GWP -" not in i]

    # Create correlation matrix
    corr_matrix = data.corr()

    # Drop the row values that don't have GWP in tick string
    corr_matrix.drop(index=not_gwp_rows,axis=0,inplace=True)

    # Create the heatmap 
    fig, ax = plt.subplots(figsize=(21,6))
    svm = sn.heatmap(corr_matrix, vmin=-1, vmax=1, annot=True, linewidth=.5, fmt='.2f',center=0, cmap='RdYlGn', ax=ax,square=True)
    ax.set_title('Correlation Heatmap')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    sn.set(font_scale=0.0125)


    # Grab figure
    figure = svm.get_figure()

    # Save figure    
    figure.savefig(f'{picname}', dpi=1700)
    print("PNG Generated!")

@app.command(help="[bold green]Creates[/bold green] Correlation Heatmap PNG by GWP with correlations >= [bold green]0.8[/bold green]\n\nThis requires [bold red]FILENAME[/bold red] and [bold red]PICNAME[/bold red]")
def high_corr_heatmap(
filename:str = typer.Argument(...,help="CSV Data File"), 
picname:str = typer.Argument(...,help="Correlation Matrix PNG image")

):
    # Pull in imputed dataset
    data = pd.read_csv(f'{filename}')

    # Exclude broker_id 
    data = data.loc[:, data.columns!='broker_id_id']
    data = data.loc[:, data.columns!='broker_name']


    # get the column values
    row_values = list(data.columns)

    # Grab column values that don't have GWP in the tick string
    not_gwp_rows = [i for i in row_values if "GWP -" not in i]

    # Create correlation matrix
    corr_matrix = data.corr()

    # Drop the row values that don't have GWP in tick string
    corr_matrix.drop(index=not_gwp_rows,axis=0,inplace=True)

    # Filter out nulls in dataset
    mask = pd.isnull(True)

    # Filter highly correlated matrix values 0.7 < x < 1.00 
    corr_matrix = corr_matrix[abs(corr_matrix) >= 0.80]
    corr_matrix = corr_matrix[abs(corr_matrix) < 1.00]

    # Find columns that are motly empty
    empty_columns = corr_matrix.columns[21:]

    # Drop areas of correlation matrix with majority empty columns
    corr_matrix.drop(empty_columns, inplace=True,axis=1)


    # Create the heatmap 
    fig, ax = plt.subplots(figsize=(11,6))
    #plt.tight_layout()
    svm = sn.heatmap(corr_matrix, vmin=-1, vmax=1, annot=True, linewidth=.5, fmt='.2f',center=0, cmap='RdYlGn', mask=mask, ax=ax,square=True)



    # Set axis 
    ax.set_title('Correlation Heatmap (High Values > 0.80)')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    sn.set(font_scale=0.125)


    # Grab figure
    figure = svm.get_figure()

    # Save figure    
    figure.savefig(f'{picname}', dpi=1700)




if __name__=="__main__":
    app()
