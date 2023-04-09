import os
import gpxpy
import gpxpy.gpx
import matplotlib.pyplot as plt

os.chdir('')

# load GPX file
gpx_file = open('activity.gpx', 'r')
gpx = gpxpy.parse(gpx_file)

# extract track points
points = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            points.append((point.latitude, point.longitude))

# plot route
lats, lons = zip(*points)
plt.plot(lons, lats)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
