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


@vcr.use_cassette()
def test_payment_profiles_create(api, payment_profile_data):
    body = payment_profile_data
    response = api.payment_profiles.create(body=body)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.body['payment_profile']['id'] == payment_profile_data['id']


@vcr.use_cassette()
def test_payment_profiles_list(api):
    response = api.payment_profiles.list()
    assert response.status_code == status.HTTP_200_OK
    assert 'payment_profiles' in response.body


@vcr.use_cassette()
def test_payment_profiles_retrieve(api, payment_profile_data):
    response = api.payment_profiles.retrieve(payment_profile_data['id'])
    assert response.status_code == status.HTTP_200_OK
    assert response.body['payment_profile']['id'] == payment_profile_data['id']


@vcr.use_cassette()
def test_payment_profiles_verify(api, payment_profile_data):
    response = api.payment_profiles.verify(payment_profile_data['id'])
    assert response.status_code == status.HTTP_201_CREATED
    assert 'transaction' in response.body


@vcr.use_cassette()
def test_payment_profiles_destroy(api, payment_profile_data):
    response = api.payment_profiles.destroy(payment_profile_data['id'])
    assert response.status_code == status.HTTP_200_OK
    assert response.body['payment_profile']['id'] == payment_profile_data['id']
    assert response.body['payment_profile']['status'] == 'inactive'


@vcr.use_cassette()
def test_bill_create(api, bill_data):
    body = bill_data
    response = api.bills.create(body=body)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.body['bill']['id'] == bill_data['id']


@vcr.use_cassette()
def test_bill_list(api):
    response = api.bills.list()
    assert response.status_code == status.HTTP_200_OK
    assert 'bills' in response.body


@vcr.use_cassette()
def test_bill_retrieve(api, bill_data):
    response = api.bills.retrieve(bill_data['id'])
    assert response.status_code == status.HTTP_200_OK
    assert response.body['bill']['id'] == bill_data['id']


@vcr.use_cassette()
def test_bill_update(api, bill_data):
    body = {
        'code': 'first-bill'
    }
    response = api.bills.update(bill_data['id'], body=body)
    assert response.status_code == status.HTTP_200_OK
    assert response.body['bill']['id'] == bill_data['id']
    assert response.body['bill']['code'] == body['code']


@vcr.use_cassette()
def test_bill_destroy(api):
    id = 7071692
    response = api.bills.destroy(id)
    assert response.status_code == status.HTTP_200_OK
    assert response.body['bill']['id'] == id
    assert response.body['bill']['status'] == 'canceled'


@vcr.use_cassette()
def test_charge_list(api):
    response = api.charges.list()
    assert response.status_code == status.HTTP_200_OK
    assert 'charges' in response.body


@vcr.use_cassette()
def test_charge_retrieve(api, charge_data):
    response = api.charges.retrieve(charge_data['id'])
    assert response.status_code == status.HTTP_200_OK
    assert response.body['charge']['id'] == charge_data['id']


@vcr.use_cassette()
def test_charge_update(api, charge_data):
    body = {
        'installments': 2
    }
    response = api.charges.update(charge_data['id'], body=body)
    assert response.status_code == status.HTTP_200_OK
    assert response.body['charge']['id'] == charge_data['id']
    assert response.body['charge']['installments'] == body['installments']


@vcr.use_cassette()
def test_charge_destroy(api):
    id = 6814889
    response = api.charges.destroy(id)
    assert response.status_code == status.HTTP_200_OK
    assert response.body['charge']['id'] == id
    assert response.body['charge']['status'] == 'canceled'


@vcr.use_cassette()
def test_charge_charge(api, charge_data):
    response = api.charges.charge(charge_data['id'])
    assert response.status_code == status.HTTP_201_CREATED
    assert response.body['charge']['id'] == charge_data['id']
    assert response.body['charge']['status'] == 'paid'
