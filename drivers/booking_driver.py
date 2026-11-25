
from movie_booking.movie import Movie
from movie_booking.customer import Customer
from movie_booking.booking_system import BookingSystem


class BookingDriver:
    def __init__(self):
        self.system = BookingSystem()
        self.movie = None
        self.customer = None
        self.result = None

    def create_movie(self, title, seats):
        self.movie = Movie(title, seats)

    def create_customer(self, name, age):
        self.customer = Customer(name, age)

    def book_tickets(self, count):
        if self.movie is None or self.customer is None:
            raise ValueError("Movie and customer must be created before booking")

        self.result = self.system.book_ticket(
            self.customer,
            self.movie,
            count
        )
        return self.result

    def get_available_seats(self):
        if self.movie is None:
            raise ValueError("Movie has not been created")

        return self.movie.available_seats

    def booking_succeeded(self):
        return self.result is not None and self.result["success"]
