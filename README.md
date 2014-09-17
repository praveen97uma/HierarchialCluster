HierarchialCluster
==================

Creates a Hierarchial cluster of items supplied:

Eg.

If you have a set of integer points(x1, x2, ...) on  a 1 dimensional line and 
want to clusterize it using the metric |xi - xj|.

```
main.py
----------

from item import IntegerItem
from clusteritem import ClusterItem
from hierarchialclustering import HierArchialCluster

def cluster():
    testIntegers = [1, 2, 3, 5, 72, 1000, 100000]
    items = [IntegerItem(i) for i in testIntegers]
    clusterItems = [ClusterItem([item]) for item in items]
    noOfClusters = 3
    hCluster = HierArchialCluster(clusterItems, noOfClusters)
    clusters = hCluster.cluster()
    print "The Clusters are "
    hCluster.display()

```

Running this code prints:
```
python main.py

The Clusters are 
100000, 

1,  2,  3,  5,  72, 

1000, 
```



