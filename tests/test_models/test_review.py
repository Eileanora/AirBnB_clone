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

    def test_class_attributes(self):
        '''Test for class attributes'''
        r = Review()
        self.assertTrue(hasattr(r, 'place_id'))
        self.assertTrue(hasattr(r, 'user_id'))
        self.assertTrue(hasattr(r, 'text'))
        self.assertTrue(type(r.place_id) is str)
        self.assertTrue(type(r.user_id) is str)
        self.assertTrue(type(r.text) is str)
        self.assertEqual(r.place_id, '')
        self.assertEqual(r.user_id, '')
        self.assertEqual(r.text, '')


if __name__ == '__main__':
    unittest.main()
