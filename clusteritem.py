


class ClusterItem(object):
    def __init__(self, items=[]):
        self.cluster_id = None
        self.items = items

    def getDistanceFromCluster(self, otherCluster):
        otherClusterItems = otherCluster.items
        
        minDistance = 999999
        for other_item in otherClusterItems:
            for  item in self.items:
                minDistance = min(minDistance, other_item.getDistance(item))

        return minDistance

    def __str__(self):
        return repr(",".join(self.items))

    def mergeWithCluster(self, otherCluster):
        newCluster = ClusterItem(self.items + otherCluster.items)
        return newCluster

    def setUniqueId(self, uid):
        self.cluster_id = uid

    def getUniqueId(self):
        return self.cluster_id

    def display(self):
        for item in self.items:
            print "%s, "%(item),
        print 
    
