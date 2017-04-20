import os

import pytest

from vindi.api import get_api_instance


@pytest.fixture
def api():
    return get_api_instance(token=os.getenv('API_TOKEN', ''))


@pytest.fixture
def customer_data():
    return {
        'customer': {
            'id': 2481112,
            'name': 'John Doe',
            'email': 'john@doe.com',
            'registry_code': None,
            'code': None,
            'notes': None,
            'status': 'inactive',
            'created_at': '2017-04-19T13:08:51.795-03:00',
            'updated_at': '2017-04-19T13:08:51.795-03:00',
            'metadata': {},
            'address': {
                'street': None,
                'number': None,
                'additional_details': None,
                'zipcode': None,
                'neighborhood': None,
                'city': None,
                'state': None,
                'country': None
            },
            'phones': []
        }
    }


@pytest.fixture
def product_data():
    return {
        'product': {
            'id': 82534,
            'name': 'Product One',
            'code': 'product-one',
            'unit': None,
            'status': 'active',
            'description': None,
            'invoice': 'always',
            'created_at': '2017-04-20T08:27:28.000-03:00',
            'updated_at': '2017-04-20T08:27:28.000-03:00',
            'pricing_schema': {
                'id': 1196727,
                'short_format': 'R$ 100,00',
                'price': '100.0',
                'minimum_price': None,
                'schema_type': 'flat',
                'pricing_ranges': [],
                'created_at': '2017-04-20T08:27:28.000-03:00'
            },
            'metadata': {}
        }
    }


@pytest.fixture
def payment_method_data():
    return {
        'payment_method': {
            'id': 17293
        }
    }


@pytest.fixture
def payment_profile_data():
    return {
        'id': 2284520,
        'holder_name': 'John Doe',
        'card_expiration': '12/2020',
        'card_number': '5555555555555557',
        'card_cvv': '123',
        'payment_method_code': 'credit_card',
        'payment_company_code': 'mastercard',
        'customer_id': 2481258
    }
