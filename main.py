from item import IntegerItem
from clusteritem import ClusterItem
from hierarchialclustering import HierArchialCluster

def cluster():
    testIntegers = [1, 2, 3, 5, 72, 1000, 100000]
    items = [IntegerItem(i) for i in testIntegers]
    clusterItems = [ClusterItem([item]) for item in items]

    hCluster = HierArchialCluster(clusterItems, 3)
    clusters = hCluster.cluster()
    print "The Clusters are "
    hCluster.display()


if __name__=='__main__':
    cluster()

