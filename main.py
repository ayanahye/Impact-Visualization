# data taken from: https://www2.gov.bc.ca/gov/content/safety/wildfire-status/about-bcws/wildfire-statistics
# more data: https://cfs.nrcan.gc.ca/statsprofile/disturbance/CA

import plotly.express as px
import pandas as pd

# Load your forest fire data (replace "general_data_part.csv" with the correct filename)
print("Getting data...")
df = pd.read_csv("general_data_part.csv")

# Load the additional data (replace "additional_data.csv" with the correct filename)
additional_data = pd.read_csv("CO2_data.csv")

# Merge the forest fire data and additional data based on the common column (e.g., year)
merged_df = pd.merge(df, additional_data, on='Year')

# Create a scatter mapbox plot
fig = px.scatter_mapbox(merged_df,
                        lat='latitude',
                        lon='longitude',
                        color='Year',
                        color_continuous_scale='Reds',
                        size='Size',
                        animation_frame='Year',
                        zoom=4,
                        width=1000,
                        height=750,
                        title="Forest Fire Impact Map",
                        hover_name='Geographic',
                        hover_data={
                            'Size': ':.2f',
                            'Area of managed forests (hectares)': True,
                            'Total net emissions or removals to the atmosphere, all causes (CO2e/yr, megatonnes)': True,
                            'Net emissions or removals due to natural disturbances (CO2e/yr, megatonnes)': True,
                            'Net emissions or removals due to human forest management activities and from harvested wood products (CO2e/yr, megatonnes)': True,
                            'Transfers from the managed forest sector to the forest products sector due to harvesting (CO2e/yr, megatonnes)': True
                        }
                        )

fig.update_layout(mapbox_style="carto-darkmatter")
fig.update_layout(margin={"r": 0, "t": 50, "b": 10})
fig.show()

print("Plot complete.")
