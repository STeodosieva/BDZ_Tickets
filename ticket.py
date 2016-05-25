class Ticket:
    def __init__(self, seat_number, train_class, passenger, worker, destination, price):
        self.seat_number = seat_number # вместо class Seat
        self.train_class = train_class # вместо class Seat
        self.passenger = passenger
        self.worker = worker
        self.destination = destination
        #if self.destination in list_of_stops (нещо от базата)
        #--> да се генерира коя е композицията
        self.price = price # трябва ли да се подава или да се вземе от базата
                            # и да се сметне discount 
        #self.price = check_for_discount, ако променя check_for_discount да върне price

    def check_for_discount():
        if self.passenger.age < 6:
            print('Discount: 100% Price: $0')
            self.price = 0
            return True
        elif self.passenger.age < 18 or self.passenger.age > 65:
            print('Discount: 50% Price: ${}'.format(self.price / 2))
            self.price /= 2
            return True
        else:
            print('No discount offered')
            return False
