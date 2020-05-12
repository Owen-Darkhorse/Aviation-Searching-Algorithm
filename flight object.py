##*********************************************************
##Aviation Searching Algorithm
##By Owen and Alan
##
##Flight object for passenger
##********************************************************

class flight:
    def __init__(flight_No, date, departure, landing, compartment, luggage):
        '''
        departure stands for departure city,
        landing stands for landing city,
        date refers to date of departure,
        compartment determines price level,
        luggage specifies luggage restrictions
        '''
        self.flight_No = flight_No
        self.date = date
        self.departure = departure
        self.landing = landing
        self.compartment = compartment
        self.luggage = luggage


