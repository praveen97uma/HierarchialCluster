


class ClusterItem(object):
    """
    This class represents a single Cluster.

    A ClusterItem can be composed of many AbstractItem objects.
    """
    
    def __init__(self, items=[]):
        self.cluster_id = None
        self.items = items

    def getDistanceFromCluster(self, otherCluster):
        """
        Gets the distance between the other cluster.

        We compute the minimum distance between all the items in this cluster
        with the items in the second cluster.            
        """

        otherClusterItems = otherCluster.items
        
        minDistance = 999999
        for other_item in otherClusterItems:
            for  item in self.items:
                minDistance = min(minDistance, other_item.getDistance(item))

        return minDistance

    def __str__(self):
        return repr(",".join(self.items))

    def mergeWithCluster(self, otherCluster):
        """
        Returns a new ClusterItem object with the concatenated copies
        of AbstractItem objects from the given two ClusterItem objects.
        """

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
    
