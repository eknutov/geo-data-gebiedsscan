## readme

### structure
* data-geojson - GeoJSON files
* scripts - python data transformation scripts
  * csv_to_geojson.py - transforming CSV into Geo-JSON for specific applications

#### data-geojson
The following two files were read in `espg:7415` format and then convereted to `espg:4326` format and exported to geojson.
* `Grenzen_project_epsg_4326.geojson`
* `Grenzen_subproject_epsg_4326.geojson`
These files were used in the [Gebiedsscan project](https://github.com/PDOK/Gebiedsscan)
