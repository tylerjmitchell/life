import gpxpy
import gpxpy.gpx
import matplotlib.pyplot as plt

# Load GPX file
gpx_file = open('daily_run.gpx', 'r')
gpx = gpxpy.parse(gpx_file)

# Extract track points
points = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            points.append((point.latitude, point.longitude))

# Plot route
lats, lons = zip(*points)
plt.plot(lons, lats)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
