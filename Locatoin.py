import folium
folium_map = folium.Map()
LOCATION_DATA = [("18.619974","73.748202"),("19.063453","74.696520")]

for cords in LOCATION_DATA:
    folium.Marker(location=[cords[0], cords[1]]).add_to(folium_map)

folium_map = folium.Map(location=[LOCATION_DATA[0][0], LOCATION_DATA[0][1]], zoom_start=8)
south_west_corner = min(LOCATION_DATA)
north_east_corner = max(LOCATION_DATA)
folium_map.fit_bounds([south_west_corner, north_east_corner])

marker_text = ["JSPM's RSCOE","Home"]
for coords, text in zip(LOCATION_DATA, ["JSPM's RSCOE", "Home"]):
    folium.Marker(location=coords, tooltip=text).add_to(folium_map)
folium_map.save("FoliumMap.html")
