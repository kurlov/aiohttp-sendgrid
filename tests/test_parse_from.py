from aiohttp_sendgrid import Sendgrid


def test_parse_from_str():
    data = 'name@example.com'
    parsed_email = Sendgrid()._parse_from_email(data)
    assert parsed_email == {'email': 'name@example.com'}


def test_parse_from_dict():
    data = {'email': 'name@example.com', 'name': 'Ivan'}
    parsed_email = Sendgrid()._parse_from_email(data)
    assert parsed_email == {'email': 'name@example.com', 'name': 'Ivan'}


def test_parse_from_dict_no_name():
    data = {'email': 'name@example.com'}
    parsed_email = Sendgrid()._parse_from_email(data)
    assert parsed_email == {'email': 'name@example.com'}
