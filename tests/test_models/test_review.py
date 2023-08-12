#!usr/bin/python3
'''Module for testing the review class'''
import unittest
from models.review import Review
from tests.test_models.test_base_model import TestBase


class TestReview(TestBase):
    '''Tests for the Review class'''
    def setUp(self):
        '''Set up method'''
        super().setUp()
        self.cls = Review

    def test_class_attributes_exist(self):
        '''Test for class attributes'''
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertTrue(hasattr(Review, 'text'))

    def test_class_attributes_type(self):
        '''Test for class attributes'''
        self.assertTrue(type(Review.place_id) is str)
        self.assertTrue(type(Review.user_id) is str)
        self.assertTrue(type(Review.text) is str)

    def test_class_attributes_default(self):
        '''Test for class attributes'''
        self.assertEqual(Review.place_id, '')
        self.assertEqual(Review.user_id, '')
        self.assertEqual(Review.text, '')


if __name__ == '__main__':
    unittest.main()
