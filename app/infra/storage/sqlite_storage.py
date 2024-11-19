from datetime import datetime
import sqlite3

from abc import ABC, abstractmethod
from domain.book import Book

class BookRepository(ABC):
  @abstractmethod
  def add(self,book:Book)->int:
    pass
  @abstractmethod
  def delete(self,id):
    pass
  @abstractmethod
  def get(self)->list:
    pass
  
  class Sqlite_storageError(Exception):
    pass

class SQLiteStorage(BookRepository):
  def __init__(self, db_name):
    
    self.conn = sqlite3.connect(f'app/infra/databases/{db_name}',check_same_thread=False)
    self._create_table()
  
  def _create_table(self):
    try:
      with self.conn:
        self.conn.execute('''
                          CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                          title text,
                          description text,
                          publish_year integer,
                          pages_count integer,
                          created_at date
                          )
                          ''')
    except sqlite3.Error as e:
      raise self.Sqlite_storageError(f"Error creating table: {e}")
      
  def add(self, book: Book)->int:
    try:
      with self.conn:
        book.created_at=datetime.now()
        cursor=self.conn.execute(
          'insert into books (title,description,publish_year,pages_count,created_at) values (?,?,?,?,?)',
          (book.title,book.description,book.publish_year,book.pages_count,book.created_at)
        )
      return cursor.lastrowid
    except sqlite3.Error as e:
      raise self.Sqlite_storageError(f"Error adding book: {e}")
  
  def delete(self, id):
    with self.conn:
      cursor=self.conn.execute('delete from books where id=?', (id,))
  
  def get(self):
    with self.conn:
      cursor=self.conn.execute('select * from books')
      rows = cursor.fetchall() 
        
   
    books = []
    for row in rows:
        book = Book(
            title=row[1],
            description=row[2],
            publish_year=row[3],
            pages_count=row[4],
            created_at=row[5]  
        )
        books.append(book)
    return books
  