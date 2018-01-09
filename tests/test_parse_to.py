from aiohttp_sendgrid import Sendgrid


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
