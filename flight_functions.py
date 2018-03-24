"""Starter code for CSC108 Assignment 3"""

from typing import Dict, List, Set, Tuple
from flight_reader import AirportDict, RouteDict, AIRPORT_DATA_INDEXES


def get_airport_info(airports: AirportDict, iata: str, info: str) -> str:
    """Return the airport information for airport with IATA code iata for
    column info from AIRPORT_DATA_INDEXES.

    >>> get_airport_info(TEST_AIRPORTS_DICT, 'AA1', 'Name')
    'Apt1'
    >>> get_airport_info(TEST_AIRPORTS_DICT, 'AA4', 'IATA')
    'AA4'
    """
    return airports[iata][AIRPORT_DATA_INDEXES[info]]


def is_direct_flight(iata_src: str, iata_dst: str, routes: RouteDict) -> bool:
    """Return whether there is a direct flight from the iata_src airport to
    the iata_dst airport in the routes dictionary. iata_src may not
    be a key in the routes dictionary.

    >>> is_direct_flight('AA1', 'AA2', TEST_ROUTES_DICT_FOUR_CITIES)
    True
    >>> is_direct_flight('AA2', 'AA1', TEST_ROUTES_DICT_FOUR_CITIES)
    False
    """
    return iata_dst in routes[iata_src]
    # Complete the function body


def is_valid_flight_sequence(iata_list: List[str], routes: RouteDict) -> bool:
    """Return whether there are flights from iata_list[i] to iata_list[i + 1]
    for all valid values of i. IATA entries may not appear anywhere in routes.

    >>> is_valid_flight_sequence(['AA3', 'AA1', 'AA2'], TEST_ROUTES_DICT_FOUR_CITIES)
    True
    >>> is_valid_flight_sequence(['AA3', 'AA1', 'AA2', 'AA1', 'AA2'], TEST_ROUTES_DICT_FOUR_CITIES)
    False
    """
    for i in range(len(iata_list)-1):
        if iata_list[i] not in routes:
            return False
        if not is_direct_flight(iata_list[i], iata_list[i+1], routes):
            return False
    return True


# Write the rest of the data analysis functions + your helper functions here
def count_outgoing_flights(iata_src: str, routes: RouteDict) -> int:
    """
    Return the number of outgoing flights for the airport with the
    IATA code in the given route information.

    >>> count_outgoing_flights('AA1', TEST_ROUTES_DICT_FOUR_CITIES)
    2
    >>> count_outgoing_flights('AA3', TEST_ROUTES_DICT_FOUR_CITIES)
    2
    """
    if iata_src not in routes:
        return False
    return len(routes[iata_src])


def count_incoming_flights(iata_dst: str, routes: RouteDict) -> int:
    """
    Return the number of incoming flights for the airport with the
    IATA code in the given route information.

    >>> count_incoming_flights('AA1', TEST_ROUTES_DICT_FOUR_CITIES)
    2
    >>> count_incoming_flights('AA3', TEST_ROUTES_DICT_FOUR_CITIES)
    1
    """
    count = 0
    for dsts in routes.values():
        if iata_dst in dsts:
            count += 1
    return count


def reachable_destinations(iata_src: str, flight_num:int, routes: RouteDict) -> List[Set[str]]:
    """
    Return a list of the sets of IATA codes reachable from the first
    parameter in steps from 0 up to (and including) the maximum number of hops.

    >>> [{'AA1'}, {'AA2', 'AA4'}, {'AA3'}] == \
    reachable_destinations("AA1", 2, TEST_ROUTES_DICT_FOUR_CITIES)
    True
    """
    result = [{iata_src}]
    for i in range(flight_num):
        srcs = result[i]
        dsts = set()
        for airport in srcs:
            if airport in routes:
                dsts = dsts.union(routes[airport])
        dsts = dsts - result[i]
        result.append(dsts)
    clear_lst(result)
    return result


def clear_lst(airlines: List[Set])->List[Set[str]]:
    """

    >>> result = [{'AA1'}, {'AA2', 'AA4'}, {'AA3'}]
    >>> result == clear_lst([{'AA1'}, {'AA4', 'AA2'}, {'AA1', 'AA3'}])
    True
    """
    current = len(airlines) - 1
    while current != 0:
        for i in range(current):
            airlines[current] = airlines[current] - airlines[i]
        current -= 1
    return airlines


def find_busiest_airports(routes: RouteDict, airport_num: int) -> List[Tuple[str, int]]:
    """
    Find the n busiest airports in terms of air traffic volume.

    >>> find_busiest_airports(TEST_ROUTES_DICT_FOUR_CITIES, 2)
    [('AA1', 4)]
    >>> find_busiest_airports(TEST_ROUTES_DICT_FOUR_CITIES, 3)
    [('AA1', 4), ('AA4', 3), ('AA3', 3)]
    """
    lst = []
    for i in routes:
        lst.append((count_incoming_flights(i, routes) + count_outgoing_flights(i, routes), i))
    lst.sort(reverse=True)
    if airport_num == len(lst):
        return lst
    if lst[airport_num - 1][0] == lst[airport_num][0]:
        limit = lst[airport_num][0] + 1
    else:
        limit = lst[airport_num - 1][0]
    return find_limit(lst, limit)


def find_limit(original: List[Tuple[int, str]], limit: int) -> List[Tuple[str, int]]:
    """


    """
    result = []
    for i in original:
        if i[0] >= limit:
            result.append((i[1], i[0]))
    return result


if __name__ == '__main__':
    """Uncommment the following as needed to run your doctests"""
    from flight_types_constants_and_test_data import TEST_AIRPORTS_DICT
    from flight_types_constants_and_test_data import TEST_AIRPORTS_SRC
    from flight_types_constants_and_test_data import TEST_ROUTES_DICT_FOUR_CITIES
    from flight_types_constants_and_test_data import TEST_ROUTES_SRC

    import doctest
    doctest.testmod()

