class AccountStatus(Enum):
  ACTIVE, CLOSED, BLOCKED, CANCELLED, NONE = 1, 2, 3, 4, 5

class ReservationStatus(Enum):
  COMPLETED, PENDING, CANCELLED, NONE = 1, 2, 3, 4

class BookStatus(Enum):
  AVAILABLE, RESERVED, LOANED, LOST = 1, 2, 3, 4

class Constants:
  self.MAX_BOOKS_ISSUED_TO_USER = 5