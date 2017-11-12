from geojsonio import display

with open('crbdist6.geojson') as f:
    contents = f.read()
    display(contents)
