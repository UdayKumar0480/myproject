import folium
folium_map=folium.Map(location=[17.4061,78.3765],zoom_start=5,tiles="cartoDB dark_matter")
folium_map.save("map.html")
