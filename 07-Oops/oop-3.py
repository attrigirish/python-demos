class FLIGHT:
    flight_number=''
    destination=''
    distance=0
    fuel=0

    def FEEDINFO(self):
        self.flight_number=int(input('enter the flight number'))
        self.destination=input('enter the destination')
        self.distance=int(input('enter the distance'))
        self.fuel=self.CALFUEL()

    def CALFUEL(self):
        if (self.distance<=1000):
            return 500
        else:
            if (self.distance>1000 and self.distance<=2000):
                return 1100
            else:
                return 2200

    def SHOWINFO(self):
        print('Flight Number : '+str(self.flight_number))
        print('Destination : '+self.destination)
        print('Distance : '+str(self.distance))
        print('Fuel Charges : '+str(self.CALFUEL()))
        
        

    
f=FLIGHT()
f.FEEDINFO()
f.SHOWINFO()
     
    
