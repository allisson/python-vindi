Python Vindi
============

|TravisCI Build Status| |Coverage Status| |Requirements Status|
|Scrutinizer Code Quality| |Code Climate|

----

Integração com API da Vindi (Python 3.5+).


Como instalar
-------------

.. code:: shell

    pip install vindi


Tutorial
--------

.. code:: python
    
    >>> # import inicial
    >>> from vindi.api import get_api_instance
    >>> # criando uma nova instância da api
    >>> api = get_api_instance(token='seu-token-da-vindi')
    >>> # listando todos os resources disponíveis
    >>> api.get_resource_list()
    ['customers', 'plans', 'products', 'payment_methods', 'discounts', 'subscriptions', 'product_items', 'periods', 'bills', 'bill_items', 'charges', 'transactions', 'payment_profiles', 'usages', 'invoices', 'movements', 'messages', 'import_batches', 'merchant', 'issues']
    >>> # listando todas as ações disponíveis para o resource customers
    >>> api.customers.actions
    {'list': {'method': 'GET', 'url': 'customers'}, 'create': {'method': 'POST', 'url': 'customers'}, 'retrieve': {'method': 'GET', 'url': 'customers/{}'}, 'update': {'method': 'PUT', 'url': 'customers/{}'}, 'destroy': {'method': 'DELETE', 'url': 'customers/{}'}}
    >>> # executando ação list com todos os parâmetros possíveis
    >>> response = api.customers.list(body=None, params={}, headers={})
    >>> # trabalhando com uma instância response
    >>> response.url
    'https://app.vindi.com.br/api/v1/customers'
    >>> response.method
    'GET'
    >>> response.headers
    {'Cache-Control': 'max-age=0, private, must-revalidate', 'Content-Type': 'application/json; charset=UTF-8', 'Date': 'Fri, 21 Apr 2017 15:30:11 GMT', 'ETag': 'W/"0cbcb8ab8eb167a7525bdc61c7b89ba3"', 'Per-Page': '25', 'Rate-Limit-Limit': '120', 'Rate-Limit-Remaining': '119', 'Rate-Limit-Reset': '1492788671', 'Server': 'nginx', 'Total': '2', 'Vindi-Merchant-Id': '5963', 'X-Request-Id': 'd155bf74-df8e-4803-8281-8f1fe0373814', 'X-Runtime': '0.034142', 'Content-Length': '773', 'Connection': 'keep-alive'}
    >>> response.body
    {'customers': [{'id': 2481112, 'name': 'Jane Doe', 'email': 'jane@doe.com', 'registry_code': None, 'code': None, 'notes': None, 'status': 'archived', 'created_at': '2017-04-19T13:08:51.000-03:00', 'updated_at': '2017-04-19T13:25:57.000-03:00', 'metadata': {}, 'address': {'street': None, 'number': None, 'additional_details': None, 'zipcode': None, 'neighborhood': None, 'city': None, 'state': None, 'country': None}, 'phones': []}, {'id': 2481258, 'name': 'John Doe', 'email': 'john@doe.com', 'registry_code': None, 'code': None, 'notes': None, 'status': 'inactive', 'created_at': '2017-04-19T13:27:35.000-03:00', 'updated_at': '2017-04-19T13:27:35.000-03:00', 'metadata': {}, 'address': {'street': None, 'number': None, 'additional_details': None, 'zipcode': None, 'neighborhood': None, 'city': None, 'state': None, 'country': None}, 'phones': []}]}
    >>> response.status_code
    200
    >>> # fim \o/

Verifique a documentação da `API Vindi`_.

.. _`API Vindi`: https://vindi.github.io/api-docs/dist/

.. |TravisCI Build Status| image:: https://travis-ci.org/allisson/python-vindi.svg?branch=master
   :target: https://travis-ci.org/allisson/python-vindi
.. |Coverage Status| image:: https://coveralls.io/repos/github/allisson/python-vindi/badge.svg?branch=master
   :target: https://coveralls.io/github/allisson/python-vindi?branch=master
.. |Requirements Status| image:: https://requires.io/github/allisson/python-vindi/requirements.svg?branch=master
   :target: https://requires.io/github/allisson/python-vindi/requirements/?branch=master
.. |Scrutinizer Code Quality| image:: https://scrutinizer-ci.com/g/allisson/python-vindi/badges/quality-score.png?b=master
   :target: https://scrutinizer-ci.com/g/allisson/python-vindi/?branch=master
.. |Code Climate| image:: https://codeclimate.com/github/allisson/python-vindi/badges/gpa.svg
   :target: https://codeclimate.com/github/allisson/python-vindi
