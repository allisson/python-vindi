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
