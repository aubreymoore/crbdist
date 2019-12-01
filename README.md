# crbdist

# Visualizing invasion history of the coconut rhinoceros beetle

This project generates an interactive, online map to visualize the invasion history of the coconut rhinoceros beetle, *Oryctes rhinoceros*, a major pest of coconut and oil palms. The map can be seen on [this GitHub page](http://aubreymoore.github.io/crbdist/mymap.html).

[Japan](http://aubreymoore.github.io/crbdist/Japan/Oshiro1980.html).

This project was inspired by Steve Bennet's blog post entitled [Super lightweight map websites with Github](https://stevebennett.me/2014/02/13/super-lightweight-map-websites/).

All data are stored in a GEOJSON text file, **map.geojson**. Note that longitudes must be in the range of 0 to 360 degrees (i.e. 170.0E is entered as 190.0 degrees).

# Japanese data

## Occurrence Records Extracted from Oshiro 1980

Data saved in the **Japan** directory. if you open [Japan/Oshiro.geojson](https://github.com/aubreymoore/crbdist/blob/master/Japan/Oshiro1980.geojson) in this repo, you will see an interactive web point map of the extracted occurrence records.

* Distribution records were transcribed into a CSV file (**Japan/Oshito1980.csv**). Column headings correspond to Darwin core fields.
* Latitude and longitude were found using locality names to search Google Maps.
* **Japan/Oshito1980.csv** was transformed to **Japan/Oshito1980.geojson** using http://geojson.io simply by dragging the CSV file onto the geojson.io web page and then copying the resulting geojson representation of the CSV table.

