import unittest
from aikidsapp.models import even_number_of_evens

class TestModel(unittest.TestCase):
    
    def test_function_returns_True(self):
        self.assertTrue(even_number_of_evens([]))

    


unittest.main()