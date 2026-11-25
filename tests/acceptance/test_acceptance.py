from drivers.booking_driver import BookingDriver


def test_successful_booking():
    # Given
    driver = BookingDriver()
    driver.create_movie("The Batman", 20)
    driver.create_customer("John", 25)

    # When
    result = driver.book_tickets(2)

    # Then
    assert result["success"] is True
    assert driver.get_available_seats() == 18


def test_multiple_ticket_booking():
    # Given
    driver = BookingDriver()
    driver.create_movie("The Batman", 30)
    driver.create_customer("Alice", 20)

    # When
    result = driver.book_tickets(5)

    # Then
    assert result["success"] is True
    assert driver.get_available_seats() == 25


def test_underage_customer():
    # Given
    driver = BookingDriver()
    driver.create_movie("The Batman", 20)
    driver.create_customer("Tim", 12)

    # When
    result = driver.book_tickets(1)

    # Then
    assert result["success"] is False
    assert driver.get_available_seats() == 20


def test_invalid_ticket_quantity():
    # Given
    driver = BookingDriver()
    driver.create_movie("The Batman", 20)
    driver.create_customer("John", 25)

    # When
    result = driver.book_tickets(0)

    # Then
    assert result["success"] is False
    assert driver.get_available_seats() == 20


def test_insufficient_available_seats():
    # Given
    driver = BookingDriver()
    driver.create_movie("The Batman", 3)
    driver.create_customer("John", 25)

    # When
    result = driver.book_tickets(5)

    # Then
    assert result["success"] is False
    assert driver.get_available_seats() == 3


def test_sold_out_movie():
    # Given
    driver = BookingDriver()
    driver.create_movie("The Batman", 0)
    driver.create_customer("John", 25)

    # When
    result = driver.book_tickets(1)

    # Then
    assert result["success"] is False
    assert driver.get_available_seats() == 0