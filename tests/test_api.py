from vindi.api import get_api_instance


def test_get_api_instance():
    api = get_api_instance(token='')
    assert api.api_root_url == 'https://app.vindi.com.br/api/v1/'
    assert api.headers['Authorization'] == 'Basic Og=='
    assert api.headers['Content-Type'] == 'application/json'
    assert api.json_encode_body


def test_get_api_instance_with_api_root_url():
    api = get_api_instance(token='', api_root_url='https://sandbox-app.vindi.com.br/api/v1/')
    assert api.api_root_url == 'https://sandbox-app.vindi.com.br/api/v1/'
    assert api.headers['Authorization'] == 'Basic Og=='
    assert api.headers['Content-Type'] == 'application/json'
    assert api.json_encode_body
