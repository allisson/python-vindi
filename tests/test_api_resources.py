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


@vcr.use_cassette()
def test_product_create(api, product_data):
    body = {
        'name': product_data['product']['name'],
        'code': product_data['product']['code'],
        'status': product_data['product']['status'],
        'pricing_schema': {
            'price': product_data['product']['pricing_schema']['price'],
            'schema_type': product_data['product']['pricing_schema']['schema_type'],
        }
    }
    response = api.products.create(body=body)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.body['product']['id'] == product_data['product']['id']


@vcr.use_cassette()
def test_product_list(api):
    response = api.products.list()
    assert response.status_code == status.HTTP_200_OK
    assert 'products' in response.body


@vcr.use_cassette()
def test_product_retrieve(api, product_data):
    response = api.products.retrieve(product_data['product']['id'])
    assert response.status_code == status.HTTP_200_OK
    assert response.body['product']['id'] == product_data['product']['id']


@vcr.use_cassette()
def test_product_update(api, product_data):
    body = {
        'name': 'Product 1',
        'code': 'product-1',
    }
    response = api.products.update(product_data['product']['id'], body=body)
    assert response.status_code == status.HTTP_200_OK
    assert response.body['product']['id'] == product_data['product']['id']
    assert response.body['product']['name'] == body['name']
    assert response.body['product']['code'] == body['code']


@vcr.use_cassette()
def test_payment_methods_list(api):
    response = api.payment_methods.list()
    assert response.status_code == status.HTTP_200_OK
    assert 'payment_methods' in response.body


@vcr.use_cassette()
def test_payment_methods_retrieve(api, payment_method_data):
    response = api.payment_methods.retrieve(payment_method_data['payment_method']['id'])
    assert response.status_code == status.HTTP_200_OK
    assert response.body['payment_method']['id'] == payment_method_data['payment_method']['id']
