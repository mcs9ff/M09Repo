import unittest
import pandas as pd
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        Book1 = BookLover('Matt', 'mcs9ff@virginia.edu', 'Fantasy')
        Book1.add_book('Return of the King', 5)
        actual = Book1.book_list.to_dict()
        expected = {'book_name':{0: 'Return of the King'}, 'book_rating':{0: 5}}
        self.assertEqual(actual, expected)
        
    def test_2_add_book(self):
        Book2 = BookLover('Joe', 'joe@virginia.edu', 'Romance')
        Book2.add_book('Return of the King', 5)
        Book2.add_book('Return of the King', 5)
        actual = Book2.book_list.to_dict()
        expected  = {'book_name':{0: 'Return of the King'}, 'book_rating':{0: 5}}
        self.assertEqual(actual, expected)
        
    def test_3_has_read(self):
        Book3 = BookLover('Bob', 'bob@virginia.edu', 'History')
        Book3.add_book('Return of the King', 5)
        actual = Book3.has_read('Return of the King')
        expected = True
        self.assertEqual(actual, expected)
    
    def test_4_has_read(self):
        Book4 = BookLover('Amy', 'amy@virginia.edu', 'Comics')
        expression = Book4.has_read('Lord of the Flies')
        self.assertFalse(expression)
        
    def test_5_num_books_read(self):
        Book5 = BookLover('Meg', 'meg@virginia.edu', 'SciFi')
        Book5.add_book('Catcher in the Rye', 5)
        Book5.add_book('The Odyssey', 4)
        Book5.add_book('Moby Dick', 4)
        Book5.add_book('The Old Man and the Sea', 2)
        actual = Book5.num_books_read()
        expected = 4
        self.assertEqual(actual, expected)
        
    def test_6_fav_books(self):
        Book6 = BookLover('Kate', 'kate@virginia.edu', 'NonFiction')
        Book6.add_book('Return of the King', 5)
        Book6.add_book('The Odyssey', 4)
        Book6.add_book('Moby Dick', 4)
        Book6.add_book('The Old Man and the Sea', 2)
        
        fave_df = Book6.fav_books()
        actual = fave_df[fave_df.book_rating > 3].to_dict()
        expected = {'book_name':{0: 'Return of the King', 1: 'The Odyssey', 2: 'Moby Dick'},
                    'book_rating':{0: 5, 1: 4, 2: 4}}
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main(verbosity=3)