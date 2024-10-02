class Customer:  # Parent class
    def __init__(self, cust_id, cust_name, ship_addr, ship_city, ship_country, bill_addr, bill_city, bill_country):

        self.cust_id = cust_id
        self.cust_name = cust_name
        self.ship_addr = self.Address(ship_addr, ship_city, ship_country) # Inner class is used to define an attribute of a Parent class
        self.bill_addr = self.Address(bill_addr, bill_city, bill_country) # Inner class is used to define an attribute of a Parent class


    class Address: # Inner class
        def __init__(self, addr, city, country):
            self.addr = addr
            self.city = city
            self.country = country

        def show_address(self):
            print(self.addr)
            print(self.city)
            print(self.country)


c1 = Customer( 1234, 'John', 'Ship address', 'Ship City', 'Ship Country', 'Bill address', 'Bill City', 'Bill Country' )

c1.ship_addr.show_address()
c1.bill_addr.show_address()


            
