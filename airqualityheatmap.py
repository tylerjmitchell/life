# import module and connect to GIS
from arcgis.gis import GIS
gis = GIS()

# add map
map1 = gis.map('Concord, NC, USA')
map1.basemap = 'osm'
map1.zoom = 10
map1

# get air quality layer and add visualization
airquality = gis.content.get('8dcf5d4e124f480fa8c529fbe25ba04e')
map1.add_layer(airquality, {'renderer':'HeatmapRenderer',
                            'field':'value',
                            'colors':'jet',
                            'opactiy:':0.75})
