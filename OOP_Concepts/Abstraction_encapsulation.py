# Database program to understand the encapsulation

class database:
    def __init__(self):
        self.storage={} # public
        # self._storage={}  protected
        # self.__storage={}  private
    
    def write(self,key,value):
        self.storage[key]=value

    def read(self,key):
        if key in self.storage:
            print(self.storage[key])
        else:
            print("Not available")
    
db=database()
db.write("Chandan","11k")
db.read("Chandan")
print(db.storage)