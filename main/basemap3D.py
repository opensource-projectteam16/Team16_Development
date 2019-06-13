
from mpl_toolkits.basemap import Basemap
from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style

import matplotlib.pyplot as plt
import numpy as np
''' This class is to draw 3D map using Basemap '''
# reference : https://buildmedia.readthedocs.org/media/pdf/basemaptutorial/latest/basemaptutorial.pdf

'''
class mpl_toolkits.basemap.Basemap
(llcrnrlon=None, llcrnrlat=None, urcrnrlon=None, urcrnrlat=None, llcrnrx=None,
llcrnry=None, urcrnrx=None, urcrnry=None, width=None, height=None, projection='cyl',
resolution='c', area_thresh=None, rsphere=6370997.0, ellps=None,
lat_ts=None, lat_1=None, lat_2=None, lat_0=None, lon_0=None, lon_1=None, lon_2=None,
o_lon_p=None, o_lat_p=None, k_0=None, no_rot=False, suppress_ticks=True, satellite_height=35786000,
boundinglat=None, fix_aspect=True, anchor='C', celestial=False, round=False, epsg=None, ax=None)
'''


class Map3D:

    def __init__(self, userdata):

        style.use('fivethirtyeight')
        self.userdata = userdata
        self.extent = [124.5, 129.7, 38.7, 33.1]

    def draw3dMap(self):

        fig = plt.figure()
        # ax = Axes3D(fig)
        ax = fig.gca(projection='3d')

        map = Basemap(projection='cyl',  # 'gall',

                      llcrnrlon=self.extent[0],            # left longitude

                      urcrnrlon=self.extent[1],            # right longitude

                      urcrnrlat=self.extent[2],              # upper latitude

                      llcrnrlat=self.extent[3],                # lower latitude

                      resolution='l',

                      area_thresh=200,

                      fix_aspect=False,

                      ax=ax
                      )

        # Arrange polygons

        polys = []
        for polygon in map.landpolygons:
            polys.append(polygon.get_coords())

        lc = PolyCollection(polys, edgecolor='black',
                            facecolor='#DDDDDD', closed=False)

        # Data handling

        lons = list()
        lats = list()
        values = list()

        for eachUserdata in self.userdata:
            lons.append(eachUserdata[0])
            lats.append(eachUserdata[1])
            values.append(eachUserdata[2])

        lons = np.array(lons)
        lats = np.array(lats)
        values = np.array(values)

        print(lons, lats, values)

        # axis setup

        ax.set_axis_on()
        ax.azim = 270
        ax.dist = 7
        ax.add_collection3d(lc)
        ax.add_collection3d(map.drawcoastlines(linewidth=0.25))
        ax.add_collection3d(map.drawcountries(linewidth=0.35))

        ax.view_init(azim=230, elev=50)
        ax.set_xlabel('Longitude (°E)', labelpad=20)
        ax.set_ylabel('Latitude (°N)', labelpad=20)
        ax.set_zlabel('Altitude (km)', labelpad=20)

        ax.set_yticks(parallels)
        ax.set_yticklabels(parallels)
        ax.set_xticks(meridians)
        ax.set_xticklabels(meridians)
        ax.set_zlim(0., 1000.)

        # TODO NEED TO TEST
        # scatter map based on lons, lats, and values
        p = ax.scatter(lons, lats, values, c=tec_cal, cmap='jet')

        # Add a colorbar to reference the intensity
        fig.colorbar(p, label='Vamap')
        plt.show()

        # x, y = map(lons, lats)

        # ax.set_xlabel('Latitude')
        # ax.set_ylabel('Longitude')
        # ax.set_zlabel('Value')

        # ax.bar3d(x, y, values,
        #          2, 2, 2, color='r', alpha=0.8)
