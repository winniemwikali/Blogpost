import unittest
from app.models import Movie



class QuoteTest(unittest.TestCase):
    def setUp(self):
        self.new_quote = Quote(12, 'Python or Javascript?', 'Winnie')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote, Quote))
