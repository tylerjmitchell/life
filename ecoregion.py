# import modules and connect to GIS
from arcgis.gis import GIS
gis = GIS()

# add map
map1 = gis.map('Concord, NC, USA')
map1.basemap = 'osm'
map1.zoom = 7.5

map1

# get ecoregion layer, select ecoregion level IV labels, lines, polygons (5,6,7), and add visualization
ecoregion = gis.content.get('3cc13a1b3b8c4f57827f29c09a55b4a9')
map1.add_layer(ecoregion.layers[5])
map1.add_layer(ecoregion.layers[6])
map1.add_layer(ecoregion.layers[7], {'opacity':0.55})

map1.embed(output_in_cell=True, set_as_preview=True)
