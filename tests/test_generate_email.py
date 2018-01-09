from aiohttp_sendgrid import Sendgrid


def test_generate_email_no_name():
    email = 'name@example.com'
    generated_email = Sendgrid._generate_email(email=email)
    assert generated_email == {'email': 'name@example.com'}


def test_generate_email_with_name():
    email = 'name@example.com'
    name = 'Ivan'
    generated_email = Sendgrid._generate_email(email=email, name=name)
    assert generated_email == {'email': 'name@example.com',
                               'name': 'Ivan'}
