from requests.auth import _basic_auth_str as basic_http_auth
from simple_rest_client.api import API

from vindi import resource


def get_api_instance(token='', timeout=3):
    headers = {
        'Authorization': basic_http_auth(token, ''),
        'Content-Type': 'application/json'
    }
    import_batches_headers = {
        'Authorization': basic_http_auth(token, ''),
        'Content-Type': 'multipart/form-data'
    }
    api_root_url = 'https://app.vindi.com.br/api/v1/'
    api = API(
        api_root_url=api_root_url, headers=headers, json_encode_body=True,
        timeout=timeout
    )
    api.add_resource(
        resource_name='customers', resource_class=resource.CustomerResource
    )
    api.add_resource(
        resource_name='plans', resource_class=resource.PlanResource
    )
    api.add_resource(
        resource_name='products', resource_class=resource.ProductResource
    )
    api.add_resource(
        resource_name='payment_methods',
        resource_class=resource.PaymentMethodResource
    )
    api.add_resource(
        resource_name='discounts', resource_class=resource.DiscountResource
    )
    api.add_resource(
        resource_name='subscriptions',
        resource_class=resource.SubscriptionResource
    )
    api.add_resource(
        resource_name='product_items',
        resource_class=resource.ProductItemResource
    )
    api.add_resource(
        resource_name='periods', resource_class=resource.PeriodResource
    )
    api.add_resource(
        resource_name='bills', resource_class=resource.BillResource
    )
    api.add_resource(
        resource_name='bill_items', resource_class=resource.BillItemResource
    )
    api.add_resource(
        resource_name='charges', resource_class=resource.ChargeResource
    )
    api.add_resource(
        resource_name='transactions',
        resource_class=resource.TransactionResource
    )
    api.add_resource(
        resource_name='payment_profiles',
        resource_class=resource.PaymentProfileResource
    )
    api.add_resource(
        resource_name='usages', resource_class=resource.UsageResource
    )
    api.add_resource(
        resource_name='invoices', resource_class=resource.InvoiceResource
    )
    api.add_resource(
        resource_name='movements', resource_class=resource.MovementResource
    )
    api.add_resource(
        resource_name='messages', resource_class=resource.MessageResource
    )
    api.add_resource(
        resource_name='import_batches',
        resource_class=resource.ImportBatchResource,
        json_encode_body=False, headers=import_batches_headers
    )
    api.add_resource(
        resource_name='merchant', resource_class=resource.MerchantResource
    )
    api.add_resource(
        resource_name='issues', resource_class=resource.IssueResource
    )
    return api
