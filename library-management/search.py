class Search():
  def search_by_title(self, title):
    pass

  def search_by_author(self, author):
    pass

  def search_by_subject(self, subject):
    pass

  def search_by_publication_date(self, publication_date):
    pass


class Catalog(Search):
  def __init__(self):
    self.__book_titles={}
    self.__book_authors={}
    self.__book_subjects={}
    self.__book_publication_dates={}

  def search_by_title(self, query):
    return self.__book_titles.get(query)

  def search_by_author(self, query):
    return self.__book_authors.get(query)

  def search_by_subject(self, query):
    return self.__book_subjects.get(query)

  def search_by_pulication_date(self, query):
    return self.__book_publication_dates.get(query)

