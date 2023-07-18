# data taken from: https://www2.gov.bc.ca/gov/content/safety/wildfire-status/about-bcws/wildfire-statistics


import plotly.express as px
import pandas as pd

#using different colors or symbols to differentiate between different animal species.

print("Getting data...")
df = pd.read_csv("data_part.csv")

# convert latitude and longitude from degrees and minutes to decimal degrees
df['latitude'] = df['latitude'].apply(lambda x: int(x.split()[0]) + float(x.split()[1]) / 60)
df['longitude'] = df['longitude'].apply(lambda x: -(int(x.split()[0]) + float(x.split()[1]) / 60))  # Multiply by -1 to make longitudes negative

# save the updated dataframe back to the CSV file
df.to_csv("updated_data_part.csv", index=False)

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
                        zoom=9,
                        width=800,
                        height=750,
                        title="Forest Fire Impact Map"
                        )


fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 50, "b": 10})
fig.show()

print("Plot complete.")

