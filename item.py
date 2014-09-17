from exceptions import NotImplementedError


class AbstractItem(object):
	def getDistance(item):
		raise NotImplementedError()
	def display():
		raise NotImplementedError()
		

class IntegerItem(AbstractItem):
    def __init__(self, myid):
        self.id = myid 	

    def getDistance(self, item):
        return abs(item.id - self.id)

    def display(self,):
        print self.id,

    def __str__(self):
        return str(self.id)




	
