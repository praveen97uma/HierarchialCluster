from exceptions import NotImplementedError
from random import randint

class AbstractHierarchialCluster(object):
    """This is an abstract object that represents a HierarchialCluster.
    
    This methods of this class must be overriden to specify the stopping
    criteria and the metric.
    """

    def __init__(self, clusterItems):
        self.cluster_items = clusterItems
        self.clusters = {}   
        self.__initializeClustersDict()

    def __initializeClustersDict(self):
        for item in self.cluster_items:
            uid = self.__generateUniqueId()
            item.setUniqueId(uid)
            self.clusters[uid] = item

    def __generateUniqueId(self):
        """
        Returns a unique id not yet used.
        """    
    
        next_id = randint(0, 100000)
        if self.clusters.has_key(next_id):
            self.__generateUniqueId()
        return next_id

    

    def stoppingConditionMet(self):
        raise NotImplementedError()

    def getNextSetOfClosestClusters(self):
        """
        Returns the ClusterItem objects which are nearest to each other
        based on the metric implemented by AbstractItem object.
        """

		minDistance = 99999
		cluster1 = None
		cluster2 = None
		currentClusters = self.clusters.values()

		noOfClusters = len(currentClusters)
		for i in xrange(0, noOfClusters ):
			for j in xrange(i+1,noOfClusters):
				dist = currentClusters[i].getDistanceFromCluster(currentClusters[j])
				if (dist<minDistance):
					minDistance = dist
					cluster1 = currentClusters[i]
					cluster2 = currentClusters[j]
		return (cluster1, cluster2)

    def cluster(self):
        return self.__cluster()

    def __cluster(self):

        if self.stoppingConditionMet():
            return self.clusters.items()

       	(cluster1, cluster2) = self.getNextSetOfClosestClusters()# (self.cluster_items[0], self.cluster_items[0]) #
        self.__mergeClusters(cluster1, cluster2)

        return self.__cluster()

    def __mergeClusters(self, cluster1, cluster2):
        mergedCluster = cluster1.mergeWithCluster(cluster2)
        mergedCluster.setUniqueId(self.__generateUniqueId())
    
        self.clusters.pop(cluster1.getUniqueId())
        self.clusters.pop(cluster2.getUniqueId())
        self.clusters[mergedCluster.getUniqueId()] = mergedCluster


	def display(self):
		raise NotImplementedError()


class HierArchialCluster(AbstractHierarchialCluster):
    def __init__(self, cluster_items, no_of_clusters = 2):
        super(HierArchialCluster, self).__init__(cluster_items)
        self.no_of_clusters =  no_of_clusters       

    def stoppingConditionMet(self):
        if len(self.clusters)==self.no_of_clusters:
            return True
        return False

    def display(self):
        for cluster in self.clusters.values():
            cluster.display()
            print



            


