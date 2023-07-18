# data taken from: https://www2.gov.bc.ca/gov/content/safety/wildfire-status/about-bcws/wildfire-statistics


import plotly.express as px
import pandas as pd

#using different colors or symbols to differentiate between different animal species.

print("Getting data...")
df = pd.read_csv("general_data_part.csv")

print(df.head(10))
print(df.tail(10))

# create a scatter mapbox plot
fig = px.scatter_mapbox(df,
                        lat='latitude',
                        lon='longitude',
                        color='Year',
                        color_continuous_scale='Reds',
                        size='Size',
                        animation_frame='Year',
                        zoom=4,
                        width=1000,
                        height=750,
                        title="Forest Fire Impact Map"
                        )


fig.update_layout(mapbox_style="carto-darkmatter")
fig.update_layout(margin={"r": 0, "t": 50, "b": 10})
fig.show()

print("Plot complete.")

