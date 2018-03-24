"""Functions for CSC108 Assignment 3 to read in the airport and route data.
"""

from typing import TextIO

# Note about "from io import StringIO" in the docstrings:
# We can use StringIO to pretend that a string is the contents of a file.
# We are only using it for the examples below, to help you understand what
# the functions will do. 
# You do NOT have to use it yourself.

from flight_types_constants_and_test_data import AIRPORT_DATA_INDEXES, \
    ROUTE_DATA_INDEXES, AirportDict, RouteDict


def read_airports(airports_source: TextIO) -> AirportDict:
    """Return a dictionary containing the information in airports_source.
    Skip entries that have no IATA code.

    >>> from io import StringIO
    >>> airports_src = StringIO(TEST_AIRPORTS_SRC)
    >>> airports_res = read_airports(airports_src)
    >>> airports_res['AA1'][0], airports_res['AA1'][1]
    ('1', 'Apt1')
    >>> airports_res['AA4'][0], airports_res['AA4'][1]
    ('4', 'Apt4')
    >>> len(airports_res)
    4
    >>> airports_res == TEST_AIRPORTS_DICT
    True
    """
    new_dict = {}
    for line in airports_source:
        if "\\N" not in line:
            line = line[:-1]
            line_list = line.split(",")
            for i in range(len(line_list)):
                line_list[i] = line_list[i].strip("\"")
            new_dict[line_list[4]] = line_list
    return new_dict


def read_routes(routes_source: TextIO, airports: AirportDict) -> RouteDict:
    """Return the flight routes from routes_source, including only the ones
    that have an entry in airports. If there are multiple routes between
    routes_source and a destination (on different airlines for example),
    include the destination only once. Routes that include null airport IDs
    should still be included, but routes that have empty IATA should be
    excluded.

    >>> from io import StringIO
    >>> routes_src = StringIO(TEST_ROUTES_SRC)
    >>> actual = read_routes(routes_src, TEST_AIRPORTS_DICT)
    >>> actual == TEST_ROUTES_DICT_FOUR_CITIES
    True
    """

    routes = {}
    src_index = ROUTE_DATA_INDEXES['Source airport']
    dst_index = ROUTE_DATA_INDEXES['Destination airport']
    for line in routes_source:
        line = line[:-1].split(",")
        src = line[src_index]
        dst = line[dst_index]
        if src not in routes:
            routes[src] = {dst}
        else:
            routes[src].add(dst)
    return routes

    # Complete this function. 
    # Note that each value in the resulting dictionary is a set of IATA codes.


if __name__ == '__main__':
    """Uncommment the following as needed to run the doctests"""
    from flight_types_constants_and_test_data import TEST_AIRPORTS_DICT
    from flight_types_constants_and_test_data import TEST_AIRPORTS_SRC
    from flight_types_constants_and_test_data import TEST_ROUTES_DICT_FOUR_CITIES
    from flight_types_constants_and_test_data import TEST_ROUTES_SRC

    from io import StringIO

    airports_src = StringIO(TEST_AIRPORTS_SRC)
    airports_res = read_airports(airports_src)
