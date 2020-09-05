# ==============================================================================
# convert CSV into GeoJSON
# to be used with the CSV input
# (was intended to be used with GoeSPARQL endpoint CSV serialization)
# all WKT coortinates (Polygon) should be in WKT format and in "wkt" column
# of the input CSV file
# ==============================================================================

import csv
import json
import geojson
import sys
import shapely.wkt

#-------------------------------------------------------------------------------
input_csv_file = str(sys.argv[1])
output_geojson_file = input_csv_file.replace(".csv",".geojson")

print("--------------------- Convert Input CSV file into GeoJSON -----------------------------\n")
print("--- converting CSV file : ", input_csv_file  )
print("\n--- output GeoJSON:  " , output_geojson_file )
print("\n---------------------------------------------------------------------------------------\n")


# initiate geojson data
json_properties = [{}]
geoJson = {
	"type": "FeatureCollection",
	"features": []
}

with open(input_csv_file) as csv_file:
	csv_data = csv.reader(csv_file, delimiter=',', skipinitialspace=True, quoting=csv.QUOTE_MINIMAL)
	csv_list = list(csv_data)
	feature_list = csv_list[0]
	csv_list.pop(0)		# remove 0 row in the CSV list
	for rows in csv_list:
		g1 = shapely.wkt.loads(rows[0])
		jdata= {}
		# ======================================================
		for feature, row in zip(feature_list[1:], rows[1:]):		# iterate on a feature list and the current row of the csv list
			jdata[feature] = row
			#print ("\n current properties object JDATA: ", jdata)

		g2 = geojson.Feature(geometry=g1, properties=jdata)
		geoJson["features"].append(g2)

with open(output_geojson_file, 'w') as geojson_file:
    json.dump(geoJson, geojson_file)
