import status

from tests.vcr import vcr


@vcr.use_cassette()
def test_customer_create(api, customer_data):
    body = {
        'name': customer_data['customer']['name'],
        'email': customer_data['customer']['email']
    }
    response = api.customers.create(body=body)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.body['customer']['id'] == customer_data['customer']['id']


@vcr.use_cassette()
def test_customer_list(api):
    response = api.customers.list()
    assert response.status_code == status.HTTP_200_OK
    assert 'customers' in response.body


@vcr.use_cassette()
def test_customer_retrieve(api, customer_data):
    response = api.customers.retrieve(customer_data['customer']['id'])
    assert response.status_code == status.HTTP_200_OK
    assert response.body['customer']['id'] == customer_data['customer']['id']


@vcr.use_cassette()
def test_customer_update(api, customer_data):
    body = {
        'name': 'Jane Doe',
        'email': 'jane@doe.com'
    }
    response = api.customers.update(customer_data['customer']['id'], body=body)
    assert response.status_code == status.HTTP_200_OK
    assert response.body['customer']['id'] == customer_data['customer']['id']
    assert response.body['customer']['name'] == body['name']
    assert response.body['customer']['email'] == body['email']


@vcr.use_cassette()
def test_customer_destroy(api, customer_data):
    response = api.customers.destroy(customer_data['customer']['id'])
    assert response.status_code == status.HTTP_200_OK
    assert response.body['customer']['id'] == customer_data['customer']['id']
    assert response.body['customer']['status'] == 'archived'
