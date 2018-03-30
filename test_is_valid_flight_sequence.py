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

    def test_invalid_flight_sequence(self):
        expected = False
        sequence = ['AA1', 'AA7', 'AA3']
        actual = is_valid_flight_sequence(sequence, SMALL_ROUTES_DICT)
        self.assertEqual(actual, expected)


class TestGetAirportInfo(unittest.TestCase):

    def test_get_airport_info(self):
        expected = 'Apt1'
        actual = get_airport_info(TEST_AIRPORTS_DICT, 'AA1', 'Name')
        self.assertEqual(expected, actual)


class TestCountOutGoingFlight(unittest.TestCase):

    def test_find_outgoing_num(self):
        expected = 2
        actual = count_outgoing_flights('AA1')
        self.assertEqual(expected, actual)


class TestInComingGoingFlight(unittest.TestCase):

    def test_find_incoming_num(self):
        expected = 1
        actual = count_outgoing_flights('AA2')
        self.assertEqual(expected, actual)


class TestReachableDestination(unittest.TestCase):
    def test_two_transfer(self):
        from flight_types_constants_and_test_data import TEST_ROUTES_DICT_FOUR_CITIES
        expected = [{'AA1'}, {'AA2', 'AA4'}, {'AA3'}]
        actual = reachable_destinations("AA1", 3, TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(expected, actual)

    def test_another_source(self):
        from flight_types_constants_and_test_data import TEST_ROUTES_DICT_FOUR_CITIES
        expected = [{'AA2'}, {'AA3'}, {'AA1', 'AA4'}]
        actual = reachable_destinations("AA2", 3, TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(expected, actual)


class TestBusiestAirport(unittest.TestCase):

    def test_all_airports(self):
        from flight_types_constants_and_test_data import TEST_ROUTES_DICT_FOUR_CITIES
        expected = [('AA1', 4), ('AA4', 3), ('AA3', 3), ('AA2', 2)]
        actual = find_busiest_airports(TEST_ROUTES_DICT_FOUR_CITIES, 4)
        self.assertEqual(expected, actual)

    def test_two_airports(self):
        from flight_types_constants_and_test_data import TEST_ROUTES_DICT_FOUR_CITIES
        expected = [('AA1', 4)]
        actual = find_busiest_airports(TEST_ROUTES_DICT_FOUR_CITIES, 2)
        self.assertEqual(expected, actual)

    def test_three_airports(self):
        from flight_types_constants_and_test_data import TEST_ROUTES_DICT_FOUR_CITIES
        expected = [('AA1', 4), ('AA4', 3), ('AA3', 3)]
        actual = find_busiest_airports(TEST_ROUTES_DICT_FOUR_CITIES, 3)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)
