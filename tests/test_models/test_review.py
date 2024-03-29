#!/usr/bin/python3
'''
    test_review.py
    
    Unittest for class Review
'''
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''
        Class Review unittest
    '''

    def test_review_attributes(self):
        '''
            Class Review test cases
        '''
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
