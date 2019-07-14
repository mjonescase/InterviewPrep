from hamcrest import assert_that, equal_to, none

from .main import find_smallest_index

def test_find_smallest_index_empty():
    """
    Document the behavior when an empty list is sent in.
    """
    assert_that(
        find_smallest_index([]),
        none()
    )

# def test_find_smallest_index_happy():
#     """
#     Make sure `find_smallest_index` finds the
#     array index with the smallest value with a
#     straightforward, small, typical example input.
#     """
#     assert_that(
#         find_smallest_index([4, 7, 3, 9]),
#         equal_to(2)
#     )
