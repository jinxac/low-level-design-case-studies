class BookReservation():
  def __init__(self, creation_date, status, book_item_barcode, member_id):
    self.__creation_date = creation_date
    self.__status = status
    self.__book_item_barcode = book_item_barcode
    self.__member_id = member_id

  def fetch_reservation_details(self, book_item):
    pass

  def get_member_id(self):
    return self.__member_id;

  def update_reservation_status(self, status):
    self.__status = status

class BookLending():
  def __init__(self, creation_date, status, book_item_barcode, member_id, return_date):
    self.__creation_date = creation_date
    self.__status = status
    self.__book_item_barcode = book_item_barcode
    self.__member_id = member_id
    self.__return_date = return_date

  # Check why sending parameters is need
  def lend_book(self, book_item_barcode, member_id):
    pass

  def fetch_lending_details(self):
    pass

class Fine():
  def __init__(self, creation_date, book_item_barcode, member_id):
    self.__creation_date = creation_date
    self.__book_item_barcode = book_item_barcode
    self.__member_id = member_id

  def collect_fine(self, member_id, days):
    pass
