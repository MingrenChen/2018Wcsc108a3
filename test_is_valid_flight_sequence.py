import unittest
from flight_functions import *

# You can use this data in your tests if you want to
SMALL_ROUTES_DICT = {'AA1': {'AA2', 'AA3'}}
TEST_AIRPORTS_DICT = {
    'AA1': ['1', 'Apt1', 'Cty1', 'Cntry1', 'AA1', 'AAA1', '-1', '1', '1', '1', '1', 'D1', 'Typ1', 'Src1'],
    'AA2': ['2', 'Apt2', 'Cty2', 'Cntry2', 'AA2', 'AAA2', '-2', '2', '2', '2', '2', 'D2', 'Type2', 'Src2'],
    'AA3': ['3', 'Apt3', 'Cty3', 'Cntry3', 'AA3', 'AAA3', '-3', '3', '3', '3', '3', 'D3', 'Type3', 'Src3'],
    'AA4': ['4', 'Apt4', 'Cty4', 'Cntry4', 'AA4', 'AAA4', '-4', '4', '4', '4', '4', 'D4', 'Type4', 'Src4']
    }
# You can (and should) also create and use other RouteDicts for your tests

class TestIsValidFlightSequence(unittest.TestCase):

    def test_valid_direct_flight(self):
        expected = True
        sequence = ['AA1', 'AA2']
        actual = is_valid_flight_sequence(sequence, SMALL_ROUTES_DICT)
        self.assertEqual(actual, expected)
        
    # Add tests below to create a complete set of tests without redundant tests
    # Redundant tests are tests that would only catch bugs that another test
    # would also catch.

    def test_get_airport_info(self):
        expected = 'Apt1'
        self.assertEqual(expected, get_airport_info(TEST_AIRPORTS_DICT, 'AA1', 'Name'))


if __name__ == '__main__':
    unittest.main(exit=False)
