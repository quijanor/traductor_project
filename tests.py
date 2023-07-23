import unittest

from machinetranslation.translator import english_to_french, french_to_english


class TestSquare(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test when Bonjour is given as input the output is Hello.
        self.assertNotEqual(french_to_english("souris"), "home")  # test when souris is given as input the output is not home .
        

class TestDouble(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("mouse"), "souris") # test when mouse is given as input the output is souris.
        self.assertNotEqual(english_to_french("home"), "Bonjour") # test when home is given as input the output is Bonjour.
        
unittest.main()