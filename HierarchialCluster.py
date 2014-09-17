from exceptions import NotImplementedError
from random import randint

class AbstractHierarchialCluster(object):
    def __init__(self, clusterItems):
        self.cluster_items = clusterItems
        self.clusters = {}       

    def __initializeClustersDict(self):
        for item in cluster_items:
            uid = self.__generateUniqueId()
            item.setUniqueId(uid)
            self.clusters[uid] = item

    def __generateUniqueId(self):
        next_id = randint(0, 99999)
        if self.clusters.has_key(next_id):
            self.__generateUniqueId()
        return next_id

    

    def stoppingConditionMet(self):
        raise NotImplementedError()

    def cluster(self):
        self.__cluster()

    def __cluster(self):
        
        if stoppingConditionMet():
            return self.cluster_items

        (cluster1, cluster2) = self.getNextSetOfNearestClusters()
        self.__mergeClusters(cluster1, cluster2)

        self.__cluster()

    def __mergeClusters(self, cluster1, cluster2):
        mergedCluster = cluster1.mergeWithCluster(cluster2)
        mergedCluster.setUniqueId(self.__generateUniqueId())
        self.clusters.pop(cluster1.getUniqueId())
        self.clusters.pop(cluster2.getUniqueId())
        self.clusters[mergedCluster.getUniqueId()] = mergedCluster


class HierArchialCluster(AbstractHierarchialCluster):
    def __init__(self, cluster_items):
        super(self, HierArchialCluster).__init__(cluster_items)

    def stoppingConditionMet(no_of_clusters = 5):
        if len(self.cluster_items)==no_of_clusters:
            return true
        return false



            


