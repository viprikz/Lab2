import Sortstest
import unittest 
class Test_Quicksort(unittest.TestCase):
    def test_QuickOk(self):
        self.assertEqual(Sortstest.QuickSort([10, 7, 8, 9, 1, 5, 6 ,2, 8 ,1, 1100]).start() ,[1, 1, 2, 5, 6, 7, 8, 8, 9, 10, 1100])
    def test_QuickBad(self):
        self.assertEqual(Sortstest.QuickSort([10, 7, 8, 9, 1, 5, 6 ,2, 8 ,1, 1100, "Frog"]).start() ,("wrong array"))
if __name__ == '__main__':
    unittest.main()


    
