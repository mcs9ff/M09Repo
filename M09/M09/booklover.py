import unittest
import pandas as pd

class BookLover:
    num_books = 0
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        #self.num_books = num_books
        #self.book_list = book_list
        
    def add_book(self, book_name, rating):
        if book_name not in self.book_list['book_name'].unique():
            new_book = pd.DataFrame({'book_name': [book_name],
                                     'book_rating': [rating]
                                    })
            self.book_list = pd.concat([self.book_list, new_book],
                                       ignore_index=True)
        else:
            print('This book has already been added to the list.')
            
    def has_read(self, book_name):
        if book_name not in self.book_list['book_name'].unique():
            return False
        else:
            return True
        
    def num_books_read(self):
        return len(self.book_list.index)
    
    def fav_books(self):
        return self.book_list[self.book_list.book_rating >3]