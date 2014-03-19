import unittest

from pyiem.nws.products.lsr import _mylowercase
from pyiem.nws.products import lsr

class TestLSR(unittest.TestCase):
    
    def test_get_dbtype(self):
        ''' See what we get for a given LSR typetext '''
        l = lsr.LSR()
        l.typetext = "TORNADO"
        self.assertEqual(l.get_dbtype(), 'T')
    
    def test_lowercase(self):
        ''' Make sure we can properly convert cities to mixed case '''
        self.assertEqual(_mylowercase("1 N AMES"), "1 N Ames")
        self.assertEqual(_mylowercase("1 NNW AMES"), "1 NNW Ames")
                
