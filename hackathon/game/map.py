import math
import operator


class Map(dict):
    def __init__(self):
        super().__init__(self)
        self.noisemaps = {}

    def dist(self, robot1, robot2):
        coords1 = self[robot1]
        coords2 = self[robot2]
        dist = []
        for coor1, coor2 in zip(coords1, coords2):
            dist.append(coor1 - coor2)

        return math.hypot(*dist)

    def dist_loc(self, robot1, *loc):
        coords1 = self[robot1]
        dist = []
        for coor1, coor2 in zip(coords1, loc):
            dist.append(coor1 - coor2)

        return math.hypot(*dist)

    def in_circle(self, *coors, rad=1):
        coors = tuple(coors)
        return map(operator.itemgetter(0),
                   filter(lambda item: self.dist_loc(item[0], *coors) < rad, self.items()))

    def add_noisemap(self, name, noisemap):
        self.noisemaps[name] = noisemap

    def set_noisemap(self, name, noisemap):
        self.add_noisemap(name, noisemap)

    def del_noisemap(self, name):
        del self.noisemaps[name]

    def get_noise(self, *coors):
        noise = {}
        for k, v in self.noisemaps.items():
            noise[k] = v[coors]

        return noise
