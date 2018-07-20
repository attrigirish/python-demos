class Flight:
    flightno=0
    destination=''
    distance=0.0
    fuel=0.0

    def FeedInfo(self,flightno,destination,distance):
        self.flightno=flightno
        self.destination=destination
        self.distance=distance
        self.fuel=self.CalFuel()

    def ShowInfo(self):
        print("Flight Number : " + str(self.flightno))
        print("Destination : " + self.destination)
        print("Distance : " + str(self.distance))
        print("Fuel : " + str(self.fuel))

    def CalFuel(self):
        if(self.distance<=1000):
            return 500
        elif(self.distance<=1500):
            return 1000
        else:
            return 2000



f=Flight()
f.FeedInfo(12345,"Mumbai",1400)
f.ShowInfo()





        
