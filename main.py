import plotly.express as px
import pandas as pd

print("getting data...")
df = pd.DataFrame({
    'longitude': [-122.5, -123.4, -122.9],
    'latitude': [45.5, 45.2, 45.7],
    'burned_area': [500, 1000, 750],
    'year': [2010, 2015, 2020],
    'temperature': [20, 22, 25]
})

print(df.head(10))
print(df.tail(10))

# Create a scatter mapbox plot
fig = px.scatter_mapbox(df, 
                        lat=df['latitude'], 
                        lon=df['longitude'], 
                        color=df['burned_area'],
                        color_continuous_scale='Reds', 
                        size=df['burned_area'], 
                        animation_frame='year',
                        zoom=9, 
                        width=800, 
                        height=750, 
                        title="Forest Fire Impact Map"
                        )


fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0, "t":50, "b":10})
fig.show()

print("plot complete.")

