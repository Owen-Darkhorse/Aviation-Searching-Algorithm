##*********************************************************
##Aviation Searching Algorithm
##By Owen and Alan
##
##Flight object for passenger
##********************************************************

class compartment:
    def __init__(self, name, price, catering):
        '''
        Compartment has 4 classes: economic, econpremium, business
        and first class;
        
        name is a Str
        price is a Int;
        catering is Bool
        '''
        self.name = name
        self.price = price
        self.catering = catering 
        
    def __repr__(self):
        return "Compartment class: {0.name}\n Price: {0.price}\n Catering: {0.catering}".format(self)


class luggage:
    def __int__(self, length, width, height, weight, checked, portable, direct):
        '''
        Specifies luggage restrictions;
        
        luggage(Float, Float, Float, Float, Float, Bool),
        the first 3 field specifies length, width and height of the checked
        luggage, in cm;
        the 4th field specifies the quantity of checked baggages;
        the 5th field specifies the quantity of portable ;beggages
        the 6th field  whether direct baggage or not;
        '''
        self.length = length   
        self.width = width
        self.height = height
        self.weight = weight
        self.checked = checked
        self.portable = portable
        self.direct = direct
    

class flight:
    def __init__(self, flight_No, date, departure, landing, compartment, luggage):
        '''
        flight_No consists of 2 capitalized letters and 4 digits
        departure stands for departure city,
        landing stands for landing city,
        date refers to date of departure,
        compartment determines price level (refer to compartment class),
        luggage specifies luggage restrictions (refer to luggage class)
        '''
        self.flight_No = flight_No
        self.date = date
        self.departure = departure
        self.landing = landing
        self.compartment = compartment
        self.luggage = luggage
        
    def __repr__(self):
        '''
        Display all info about the flight to customers
        '''
        
        return "{0.flight_No}\n\
        {0.departure} ---> {0.landing}\n\
        date of departure: {0.date}\n\
        {0.compartment}\n\
        {0.luggage}".format(self)


##compartment tests**********************************
economic = compartment("economic", 338, True)
print(economic)