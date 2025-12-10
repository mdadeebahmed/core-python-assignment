def book_seat(total_seats, booked_seats, seat_to_book):
    if seat_to_book in booked_seats:
        print(f"Seat {seat_to_book} is already booked.")
    elif seat_to_book < 1 or seat_to_book > total_seats:
        print(f"Seat {seat_to_book} is invalid.")
    else:
        booked_seats.append(seat_to_book)
        print(f"Seat {seat_to_book} booked successfully.")
    return booked_seats


def cancel_seat(total_seats, booked_seats, seat_to_cancel):
    if seat_to_cancel in booked_seats:
        booked_seats.remove(seat_to_cancel)
        print(f"Seat {seat_to_cancel} cancelled successfully.")
    else:
        print(f"Seat {seat_to_cancel} is not booked.")
    return booked_seats
        
        


total_seats = 10
booked_seats = [2, 5, 7]


book_seat(total_seats, booked_seats, 3)


cancel_seat(total_seats, booked_seats, 5)

print('Available seats:', [seat for seat in range(1, total_seats + 1) if seat not in booked_seats])