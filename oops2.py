class driver:
    def __int__(self,id,name,vehicle):
        self.id=id 
        self.name=name 
        self.history=[]
        self.location=None 
        self.status="Avaliable"
    def getInfo(self):
        return (f'name: {self.name}, driver id: {self.id},location:{self.location}, status: {self.status}')

    def setstatus(self,status):
        old_status=self.status 
        self.status=status 
        print(f'The status of the driver is change from {old_status}--->{self.status}')
    def getHistory(self):
        print(self.history)
d1 = driver(1,"Sai")
d2 = driver(2,"Saranya")
d3 = driver(3,"krishna")
d4 = driver(4,"radha")
drivers=[d1,d2,d3,d4]
for div in drivers:
    div.getInfo()
    print("-------------------------------------------------")


