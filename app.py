# 2023 wildfires data taken from: https://open.canada.ca/data/en/dataset/2790e3f7-6395-4230-8545-04efb5a18800
# 2015-2017 wildfires data taken from: https://www2.gov.bc.ca/gov/content/safety/wildfire-status/about-bcws/wildfire-statistics
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
    df = pd.read_csv("wildfires.csv")

    # Create a scatter mapbox plot
    fig = px.scatter_mapbox(df,
                            lat='Latitude',
                            lon='Longitude',
                            color='Year',
                            color_continuous_scale='Reds',
                            size='Size',
                            animation_frame='Year',
                            zoom=4,
                            height=750,
                            hover_name='Location',
                            )

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "b": 0})
    fig.update_layout(plot_bgcolor='white', paper_bgcolor='white')  

    # Set tickvals for the color bar legend to show only whole numbers for the year
    fig.update_coloraxes(colorbar_tickvals=sorted(df['Year'].unique(), reverse=True))

    fig.update_layout(coloraxis_colorbar_title_font_color='black')
    fig.update_layout(coloraxis_colorbar_tickfont_color='black')

    fig.update_layout(
        updatemenus=[
            dict(
                buttons=[
                    dict(
                        args=[{"frame": {"duration": 1000, "redraw": True},
                               "fromcurrent": True, "transition": {"duration": 500}}],
                        label="Pause",
                        method="animate",
                    ),
                    dict(
                        args=[None],
                        label="Play",
                        method="animate",
                    ),
                ],
                direction="left",
                pad={"r": 10, "t": 87},
                showactive=False,
                type="buttons",
                x=0.1,
                xanchor="right",
                y=0,
                yanchor="top",
                font_color='black'  
            )
        ],
        sliders=[
            dict(
                active=0,
                currentvalue={"prefix": "Year: ", "font": {"color": "black"}},  
                pad={"t": 50, "l":10},
                steps=[],
                font_color='black'  
            )
        ],
    )

    return fig
# emissions vs time

def create_line_graph():
    co2_data = pd.read_csv("CO2_data.csv")
    fig = go.Figure()
    categories = co2_data.columns[1:]
    for category in categories:
        fig.add_trace(go.Scatter(x=co2_data['Year'], y=co2_data[category], name=category))

    fig.update_layout(
        title=dict(
            text="Forest Emissions Over the Years",
            y=0.95,  
            xref="paper",
            yref="container",
            x=0.5,  
            font=dict(color="black"),  
        ),
        xaxis_title="Year",
        yaxis_title="CO2 Emissions (megatonnes)",
        legend=dict(
            x=0.5,
            xanchor='center',
            y=0.9,
            xref="paper",
            yref="container",
            bgcolor="white",
            title=dict(text="Emissions Categories", font=dict(color="black")),  
            font=dict(color="black"),  
        ),
        plot_bgcolor='white',  
        paper_bgcolor='white',  
        font=dict(color="black"),  
    )

    return fig



app.layout = html.Div(style={'margin':'0 0 0 0','backgroundColor': 'white', 'width': '100vw', 'height': '100vh'},
                      children=[
                          html.H1("Forest Fire Impact Map", style={'textAlign': 'center', 'color': 'black'}),
                          dcc.Graph(figure=create_plot(), style={'width': '100%'}),
                          html.H2("CO2 Data Summary", style={'backgroundColor': 'white', 'textAlign': 'center', 'color': 'black', 'margin': '80px 0 0 0'}),
                          dcc.Graph(figure=create_line_graph())
                      ])

if __name__ == '__main__':
    app.run_server(debug=True)

