from .constants import AccountStatus, Constants, ReservationStatus, BookStatus
from .reservation import BookReservation, BookLending, Fine

from datetime import datetime

class Account():
  def __init__(self, id, password, status):
    self.__id = self.id
    self.__password = self.password
    self.__status = self.status

  def reset_password(self):
    pass

  def get_id(self):
    return self.__id;

class Librarian(Account):
  def __init__(self, id, password, status=AccountStatus.ACTIVE):
    super().__init__(id, password, status)

  def register_account(self):
    pass

  def block_member(self):
    pass

  def unblock_member(self):
    pass

  def add_book_item(self):
    pass

  def remove_book_item(self):
    pass

  def update_book_item(self):
    pass

  def issue_book(self):
    pass



class Member(Account):
  def __init__(self, id, password, status=AccountStatus.ACTIVE):
    super().__init__(id, password, status)
    self.__total_number_of_books_checkout_out = 0

  def checkout_book_item(self, book_item):
    if self.__total_number_of_books_checkout_out >= Constants.MAX_BOOKS_ISSUED_TO_USER:
      print("Max number of books already issued to user")
      return False

    book_reservation = BookReservation.fetch_reservation_details(book_item)

    if book_reservation != None and book_reservation.get_member_id != self.get_id():
      print("Book is reserved by another user")
      return False

    elif book_reservation != None:
      book_reservation.update_reservation_status(ReservationStatus.COMPLETED)

    if not book_item.checkout():
      return False

    self.__total_number_of_books_checkout_out += 1

  def check_for_fine(self, book_item_barcode):
    book_lending = BookLending.fetch_lending_details(book_item_barcode)
    due_date = book_lending.get_due_date()
    today = datetime.date.today()

    if today > due_date:
      diff = today - due_date
      diff_days = diff.days
      Fine.collect_fine(self.get_member_id(), diff_days)
    pass

  def reserve_book_item(self, book_item):
    pass

  def renew_book_item(self, book_item):
    self.check_for_fine(book_item.get_barcode())
    book_reservation = BookReservation.fetch_reservation_details(book_item)

    if book_reservation != None and book_reservation.get_member_id != self.get_id():
      print("Book is reserved by another user")
      self.__total_number_of_books_checkout_out -= 1
      book_item.update_status(BookStatus.RESERVED)
      return False
    elif book_reservation != None:
      book_reservation.update_status(ReservationStatus.COMPLETED)
      book_item.lend_book(book_item.get_barcode(), self.get_member_id())
      book_item.update_due_date(
      datetime.datetime.now().AddDays(Constants.MAX_LENDING_DAYS))
      return True

  def return_book_item(self, book_item):
    self.check_for_fine(book_item.get_barcode())
    book_reservation = BookReservation.fetch_reservation_details(book_item)

    if book_reservation != None:
      book_item.update_status(BookStatus.RESERVED)
    else:
      book_item.update_status(BookStatus.AVAILABLE)
