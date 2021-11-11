import unittest
from ..basic_info import hello_robert_smith

class TestBasics(unittest.TestCase):

    def test_robert(self):
        self.assertEqual("hello robert smith", hello_robert_smith())

    def test_not_robert(self):
        self.assertEqual("hello michael dempsey", hello_robert_smith())
