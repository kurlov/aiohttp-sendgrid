from aiohttp_sendgrid import Sendgrid
import pytest


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


def test_parse_from_wrong_input():
    no_email = {'hello': 'world'}
    with pytest.raises(TypeError):
        Sendgrid()._parse_from_email(no_email)
    integer = 1
    val_set = {1}
    with pytest.raises(ValueError):
        Sendgrid()._parse_from_email(integer)
        Sendgrid()._parse_from_email(val_set)
