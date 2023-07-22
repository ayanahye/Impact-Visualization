# data taken from: https://www2.gov.bc.ca/gov/content/safety/wildfire-status/about-bcws/wildfire-statistics
# more data: https://cfs.nrcan.gc.ca/statsprofile/disturbance/CA
# carbon data
#https://cfs.nrcan.gc.ca/statsprofile/carbon
import plotly.express as px
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html, dcc, dash_table

app = dash.Dash(__name__)

def create_plot():
    print("Getting data...")
    df = pd.read_csv("general_data_part.csv")

    # Create a scatter mapbox plot
    fig = px.scatter_mapbox(df,
                            lat='latitude',
                            lon='longitude',
                            color='Year',
                            color_continuous_scale='Reds',
                            size='Size',
                            animation_frame='Year',
                            zoom=4,
                            height=750,
                            title="Forest Fire Impact Map",
                            hover_name='Geographic',
                            )

    fig.update_layout(mapbox_style="carto-darkmatter")
    fig.update_layout(margin={"r": 0, "t": 50, "b": 10})
    fig.update_layout(plot_bgcolor='grey', paper_bgcolor='grey')  

    # Set tickvals for the color bar legend to show only whole numbers for the year
    fig.update_coloraxes(colorbar_tickvals=sorted(df['Year'].unique(), reverse=True))

    return fig

def create_table():
    co2_data = pd.read_csv("CO2_data.csv")
    return dash_table.DataTable(
        id='co2-table',
        columns=[{'name': col, 'id': col} for col in co2_data.columns],
        data=co2_data.to_dict('records'),
        style_table={
            'height': '400px',  # Set the table height
            'width': '100%',
            'overflowY': 'auto',  # Add scrollbars when content overflows
            'margin': '0 auto',  # Center the table horizontally
            'backgroundColor': 'grey',  
        },
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',  
            'fontWeight': 'bold'  
        },
        style_cell={
            'textAlign': 'center',  
            'minWidth': '100px',  
            'backgroundColor': 'grey'  
        }
    )


app.layout = html.Div(style={'backgroundColor': 'darkgrey', 'width': '100vw', 'height': '100vh'},
                      children=[
                          html.H1("Forest Fire Impact Map", style={'textAlign': 'center', 'color': 'white'}),
                          dcc.Graph(figure=create_plot(), style={'width': '100%'}),  
                          html.H2("CO2 Data Summary", style={'backgroundColor': 'darkgrey','textAlign': 'center', 'color': 'white'}),
                          create_table()
                      ])

if __name__ == '__main__':
    app.run_server(debug=True)

