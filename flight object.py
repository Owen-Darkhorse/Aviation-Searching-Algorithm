##*********************************************************
##Aviation Searching Algorithm
##By Owen and Alan
##
##Flight object for passenger
##********************************************************

class luggage:
    def __init__(self, length, width, height, weight, portable, checked, direct):
        '''
        Fields: length(Float) width(Float) height(Float) weight(Float)
                portable(Int) checked(Int) direct(Bool)
        '''
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.portable = portable
        self.checked = checked
        self.direct = direct    





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


