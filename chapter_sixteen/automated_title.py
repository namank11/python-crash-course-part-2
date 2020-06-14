import chapter_sixteen.eq_explore_data

import json

from plotly.graph_objs import Scattergeo, Layout

from plotly import offline

from chapter_sixteen import eq_explore_data

my_data = [Scattergeo(lon=eq_explore_data.lons, lat=eq_explore_data.lats, text=eq_explore_data.hover_texts, marker={
        'size': [5*mag for mag in eq_explore_data.mags],
        'color': eq_explore_data.mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    })]
my_layout = Layout(title=eq_explore_data.meta_data_title)

fig = {'data': my_data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
