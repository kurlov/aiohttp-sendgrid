from aiohttp_sendgrid import Sendgrid
import pytest


def test_parse_to_str():
    data = 'name@example.com'
    parsed_email = Sendgrid()._parse_to_emails(data)
    assert parsed_email == [{'email': 'name@example.com'}]


def test_parse_to_dict():
    data = {'email': 'name@example.com', 'name': 'Ivan'}
    parsed_email = Sendgrid()._parse_to_emails(data)
    assert parsed_email == [{'email': 'name@example.com', 'name': 'Ivan'}]


def test_parse_to_dict_no_name():
    data = {'email': 'name@example.com'}
    parsed_email = Sendgrid()._parse_to_emails(data)
    assert parsed_email == [{'email': 'name@example.com'}]


def test_parse_to_list_tuple_of_str():
    data = ['name1@example.com', 'name2@example.com', 'name3@example.com']
    result = [{'email': 'name1@example.com'},
              {'email': 'name2@example.com'},
              {'email': 'name3@example.com'}]
    parsed_list = Sendgrid()._parse_to_emails(data)
    assert parsed_list == result
    data_tuple = tuple(data)
    parsed_tuple = Sendgrid()._parse_to_emails(data_tuple)
    assert parsed_tuple == result


def test_parse_to_list_tuple_of_dict():
    data = [{'email': 'name1@example.com', 'name': 'Ivan1'},
            {'email': 'name2@example.com', 'name': 'Ivan2'},
            {'email': 'name3@example.com', 'name': 'Ivan3'}]
    result = [{'email': 'name1@example.com', 'name': 'Ivan1'},
              {'email': 'name2@example.com', 'name': 'Ivan2'},
              {'email': 'name3@example.com', 'name': 'Ivan3'}]
    parsed_list = Sendgrid()._parse_to_emails(data)
    assert parsed_list == result
    data_tuple = tuple(data)
    parsed_tuple = Sendgrid()._parse_to_emails(data_tuple)
    assert parsed_tuple == result


def test_parse_to_list_tuple_heterogeneous():
    data = [{'email': 'name1@example.com', 'name': 'Ivan1'},
            {'email': 'name2@example.com'},
            {'email': 'name3@example.com', 'name': 'Ivan3'}]
    result = [{'email': 'name1@example.com', 'name': 'Ivan1'},
              {'email': 'name2@example.com'},
              {'email': 'name3@example.com', 'name': 'Ivan3'}]
    parsed_list = Sendgrid()._parse_to_emails(data)
    assert parsed_list == result
    data_tuple = tuple(data)
    parsed_tuple = Sendgrid()._parse_to_emails(data_tuple)
    assert parsed_tuple == result


def test_parse_to_wrong_input():
    no_email = {'hello': 'world'}
    with pytest.raises(TypeError):
        Sendgrid()._parse_to_emails(no_email)
    integer = 1
    val_set = {1}
    invalid_list = ['name@example.com', 1]
    invalid_tuple = ('name@example.com', 1)
    with pytest.raises(ValueError):
        Sendgrid()._parse_to_emails(integer)
        Sendgrid()._parse_to_emails(val_set)
        Sendgrid()._parse_to_emails(invalid_list)
        Sendgrid()._parse_to_emails(invalid_tuple)
