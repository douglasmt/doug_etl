import pytest


# import row_to_list

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"


def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]


def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }

#
# def test_for_clean_row():
#     assert row_to_list("2,081\t314,942\n") == ["2,081", "314,942" ]
#
#
# def test_missing_area():
#     assert row_to_list("\t293,410\n") is none
#
# def test_for_missing_tab():
#     assert row_to_list("1,463238,765\n") is none
