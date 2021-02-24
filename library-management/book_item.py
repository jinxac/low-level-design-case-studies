from .reservation import BookReservation

from .constants import BookStatus

class BookItem():
  def __init__(self, barcode, is_reference_only, borrowed, due_date, price, book_format, status, purchase_date, publication_date, placed_at):
    self.__barcode = barcode
    self.__is_reference_only = is_reference_only
    self.__borrowed = borrowed
    self.__due_date = due_date
    self.__price = price
    self.__format = book_format
    self.__status = status
    self.__purchase_date = purchase_date
    self.__publication_date = publication_date
    self.__placed_at = placed_at

  def checkout(self, id, member_id):
    if self.get_is_reference_only():
      print("reference only book, cannot checkout")
      return False

    if BookReservation.lend_book(self.__barcode, member_id):
      return False

    self._status = BookStatus.LOANED
    return True

  def update_status(self, status):
    self.__status = status
